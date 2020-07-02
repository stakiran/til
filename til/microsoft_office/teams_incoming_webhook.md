# Incoming Webhook

## Incoming Webhook is 何？
他サービスで起きたイベントを Teams のチーム内に通知させる（ために必要な専用 URL）。

- 1: Incoming Webhook アプリをチームに設置すると専用 URL が発行される
    - この URL に POST リクエストを飛ばすと、チーム内にメッセージとして表示される
- 2: 他のサービス A の Integration 機能などから 1: の URL を指定する
    - すると **サービス A で何かイベントが起きた時に、併せて、1: で指定した URL にもイベント情報を POST する** という挙動をする

## 手順

### 1: incoming webhook の設置
- アプリ > incoming webhook > チームに追加 から適当なチームに追加
- cookie なんたらでエラーが出るので別窓で開く、設定画面出るはずなので、続く
- 設定
    - 名前は適当に(例: `test-webhook`
    - 着信 Web フックはスルーしていい
- URL が発行されるのでコピーしておく
    - こんなの → `https://outlook.office.com/webhook/XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX@……/IncomingWebhook/……`
    - めっちゃ長い。192文字くらいある


### 2: 連携先の設定
たとえば GitLab だと、

- リポジトリの設定 > General > Integration
- 通知したいイベントをチェックで選択
   - たとえば push と new issues にしたいならこれら二つにチェック
- OK

## ローカルツイートみたいなことする

### incoming_webhook_test.py
```python
# encoding: utf-8

import json
import os

import requests

proxies = {
  "http": os.environ['HTTP_PROXY'],
  "http": os.environ['HTTPS_PROXY']
}

url = os.environ['TEST_MS365_TEAMS_INCOMING_WEBHOOK_URL']

headers = {}
data = {
    "Text": "Textフィールドに詳細メッセージ",
    "Summary": "Summaryフィールドに要約メッセージ",
}
r = requests.post(url, data=json.dumps(data), proxies=proxies, headers=headers)
print(r.text)
```

### terminal
現時点では表示されるのは Text のみ。Summary は使えない。

データ不正時:

```terminal
$ python incoming_webhook_test.py
Summary or Text is required.
```

成功時:

```terminal
$ python incoming_webhook_test.py
1
```
