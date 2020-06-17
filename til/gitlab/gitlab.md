# GitLab
GitLab Community Edition 9.1.3 ベース

## :x: 指定 Issue を削除する
:scream: move しても move 元からは消えません……

- **ゴミ箱リポジトリをテキトーにつくる**
    - デフォでは issues 機能が disabled なので settings から有効にすること
- 消したい issue を開いて editし、**move にてゴミ箱リポジトリに移す**
- ……
- ゴミ箱リポジトリを削除する

## GitLab Edition Plan 種類
CE(Community Edition) → EE(Enterprise Edition) Starter → EE Premium → EE Ultimate

CE は Core とも呼ばれる。

参考: [セルフホスト: 各種プランの機能比較 - GitLab.JP](https://www.gitlab.jp/pricing/self-hosted/feature-comparison/)

## issue template
- `.gitlab/issue_templates/xxxx.md` をつくる
- a) new issues 時は title の Choose a template から選ぶ

ちなみに a) を略してデフォのテンプレを選ばせるのは無理。[GitLab Starter](https://docs.gitlab.com/ee/user/project/description_templates.html#setting-a-default-template-for-merge-requests-and-issues--starter) 以上が必要（ここは CE なので無理）。

## export した project を import するには
new project 画面から行う。**一度つくった project に注入するわけではない**。

- project name 入れる
- GitLab Export ボタン
- DL しておいた tar.gz を選んでアップロード

所感:

- repo のファイルも公開設定も、コミット履歴も、 **全部漏れなくインポートできてる感じ** :+1:

## repo の rename
- Settings からできる
- **clone URL 自体は変わらず、表示名が変わるだけ**
- なのに **repo 新規時は変更後の名前が使えない**

単に clone URL への反映が遅いだけの可能性？挙動がいまいち的を得ない。

## export 時の仕様
- tar.gz でエクスポート

```
$ cd
2019-12-06_14-07-379_(Username)_me_export

D:.
│  project.bundle
│  project.json
│  VERSION
│  
└─uploads
    └─e1ea7614798fa7e56c5c0c577708e4b4
            policy.JPG
            
```

- project.json
    - Issues 系データがずらずらと入ってる
- project.bundle
    - **バイナリデータ**
    - repo 内のファイル

## export 時の挙動 > project.json のデータ構造

```json
{
  "description": "",
  "visibility_level": 0,
  "archived": false,
  "labels": [
    {
      "id": xx,
      "title": "...",
      "color": "#FF0000",
      ...
    },
    ...
  ],
  "milestones": [],
  "issues": [
    {
      "id": xx,
      "title": "...",
      ...
      "description": "あああ\r\nあああ\r\n改行はwindows区切りかー",
      "events": [
        {
          "id": xx,
          "target_type": "Issue",
          ...
        }
      ],
      "timelogs": [],
      ...
    },
    ...
  ],
  "snippets": [],
  "releases": [],
  "project_members": [
    {
      "id": xx,
      "access_level": xx,
      ...
    },
    ...
  ],
  "merge_requests": [],
  "pipelines": [],
  "triggers": [],
  "deploy_keys": [],
  "services": [
    {
      "id": xxx,
      "title": null,
      "project_id": xxx,
      ...
    }
  ],
  "hooks": [],
  "protected_branches": [
    {
      ...
    }
  ],
  "protected_tags": [],
  "project_feature": {
    "id": xxx,
    "project_id": xxx,
    ...
    "merge_requests_access_level": 20,
    "issues_access_level": 20,
    "wiki_access_level": 0,
    "snippets_access_level": 0,
    "builds_access_level": 0,
    ...
    "repository_access_level": 20
  }
}
```

## Keyboard shortcuts キーボードショートカット
[GitLab keyboard shortcuts - GitLab](https://docs.gitlab.com/ee/user/shortcuts.html)

使うものを一つずつ着実に……。

| キー | 効果 |
| ---- | ---- |
| <kbd>t</kbd> | Find file / キャンセルは入力ボックスフォーカスからのesc / **Project 画面ならどのページからでもいけます** |
| <kbd></kbd> |  |

## REST API
- [API Docs - GitLab](https://docs.gitlab.com/ee/api/README.html)
- [API resources - GitLab](https://docs.gitlab.com/ee/api/api_resources.html)

ただし 9.1.3 はやや古いので、当該 GitLab の Help ページから辿れる API Docs を読んだ方が良い（たとえば 9.1.3 では /events がサポートされてない）。

以下 python requests による get 例:

```python
proxies = {
  "http" : os.environ['HTTP_PROXY'],
  "https": os.environ['HTTPS_PROXY']
}
# From UserSettings > Access Tokens > Add a personal access Token.
# Usually need scope both 'api' and 'read_user'.
token = os.environ['GITLAB_ACCESS_TOKEN']
headers = {
    'PRIVATE-TOKEN' : token
}

url = 'https://(GitLabURL)/api/v4/issues'
params = {
    'state' : 'opened'
}
# set your cer/cer file fullpath to REQUESTS_CA_BUNDLE envvar if needed.
r = requests.get(url, proxies=proxies, verify=True, headers=headers, params=params)
print(r.text)
```

## Project の ID を確認する
Settings から見れる。

## 自分の GitLab User ID を確認する
- 右上の三本線 > Issues とか Merge Requests を開く
- URL 見る

dashboard/merge_requests?assignee_id=143 ← こんな感じでわかる。

## 指定リポジトリの更新をウォッチしたい
Star をつけた後に Activity > Starred Projects を見る。

- https://(GitLab-URL)/dashboard/activity?filter=starred

GitHub みたいに「Follow してる人たちの更新を見る」は無いし、GitLab 上の全員の更新一覧を見るなんて仕組みもない。

## clone
アドレスバーに表示されてる **リポジトリのトップページ** の URL を git clone すれば良い。

## Wiki を clone する
**リポジトリトップページの** URL 末尾に `.wiki` をつけたものを git clone する。

- `https://……repo1/wikis/home`
- ↓
- :o: `https://……repo1.wiki`

## 最近ログインしたユーザー
https://(Address-of-GitLab)/groups/(GroupName)/group_members?sort=recent_sign_in

## star について
- 誰が付けたかは見えない
- 自分が付けた star の一覧も見えない

## 横断検索について
Group=Any、Project=Any で横断検索できそうだが **リポジトリ名や Issue 名しかヒットせず** ファイル内までは検索されない。

ファイル内も検索したいなら Project=XXXXX と何か一つ選択する。つまり **本文を含めた検索はリポジトリ単位でしか行えない**。

## repo の公開範囲
- Public: URL知ってたら誰でも見れます
- Internal: ログインしてる人なら誰でも見れます
- Private: あなたしか見れません

## Wiki で同フォルダ内の Markdown ファイルにリンクを張りたい
- :o: `[AWS CloudFormation とは](what_is_cloudformation)`
- :x: `[AWS CloudFormation とは](what_is_cloudformation.md)`
- :x: `[AWS CloudFormation とは](what_is_cloudformation.html)`
