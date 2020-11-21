# Google Chrome

## テキストエンコーディング変更
- デフォではない
- https://chrome.google.com/webstore/detail/charset/oenllhgkiiljibhfagbfogdbchhdchml/

## テキストボックスへの日本語入力が超遅い

### 対処1: Chrome を再起動する

### 対処2: Google日本語入力時だが、IME と衝突しているのでオフにする
- 設定 > 言語 > 日本語を選んでオプション
- Microsoft IME を選んでオプション
    - 学習をオフに
    - 詳細設定を開いて、他の学習や予測系も全部オフに
- Chrome を再起動する

## 一部ウェブサイトで認証が通らなくなった
概要

- Chrome の SameSite Cookie 仕様変更によるものと考えられる
- この変更によりセキュリティが向上し、SameSite に？対応していないウェブサイトは Chrome で動作しなくなった
- 動作させたいなら、disable にする

手順

- `chrome://flags/`
- SameSite で検索
- Cookies without SameSIte must be secure を Disable  に変更して relaunch

運用アイデア

- ~~サードパーティの Cookie をブロックする~~ 少なくともTeamsが動作しないので没

参考:

- [【一問一答】 Chrome の SameSite Cookie の変更とは？ ： Cookie への新たなアプローチ | DIGIDAY［日本版］](https://digiday.jp/platforms/what-is-chrome-samesite/)

## Tampermonkey
あります

- https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo/related?hl=ja

以下設定はしておく

- ダッシュボード > 設定タブ
    - 匿名の統計 off

## 下のダウンロードバーが表示されたままでうっとうしい
[Always Clear Downloads 2 - Chrome ウェブストア](https://chrome.google.com/webstore/detail/always-clear-downloads-2/jcajchndfkmnaefkhoaoiagemplbfffn)

## マウスジェスチャー
- 老舗無料ツールは既にお亡くなりになられている
- back/forward 使えればいいので小さいのにした
    - [miniGestures - Chrome ウェブストア](https://chrome.google.com/webstore/detail/minigestures/apnjnepphihnjahpbfjiebcnpgmjnhfp?hl=ja)
    - 設定画面から L と R を割り当てる

## chrome データバックアップ
- そもそも Google アカウント使ってクラウドに保存せい、が基本スタンス
    - [How to Backup Google Chrome: A Guide for 2020](https://www.cloudwards.net/backup-google-chrome/)
- ローカルでやるなら以下をまるごと
    - `%localappdata%\Google\Chrome\User Data`
    - もうちょっと踏み込んで、たぶん以下でいけるはず
        - `User Data\Default` フォルダだけで良い
        - Default のうち、Service Worker と Cache はキャッシュなので最悪なしでもok
        - Extensions もファイル数でかい（jsフルセットの過去バージョン全部保持で 19000 ファイルとか）ことがあるのでなしでok
    - 試したばかりの現時点で 500MB、うち上記二つで 350 MB くらいしめてる

## メモリ使用量
- 前提
    - 8GB win10
    - Firefox からブクマと履歴を移した
    - 下記の初期設定は一通りした
- 起動しただけ
    - 300MB
- Slackにログイン
    - +100MB
- Teamsにログイン
    - +210MB

### Firefoxとの比較
- Firefox だと 900 MB は超える
- Firefox はメモリが滞留したまま増えていく
- Chrome だと動的に GC してくれている印象がある

だが環境次第なところありそう: [firefox メモリ - Twitter検索 / Twitter](https://twitter.com/search?q=firefox%20%E3%83%A1%E3%83%A2%E3%83%AA&src=typed_query)

## Software reporter を無効にする
`%localappdata%\google\Chrome\User Data\SwReporter`

無効化できん……

- 設定から切っても復活するらしいので強引に対処する必要がある
- 1 とりあえず `exezzz` みたいにファイル名無効にした
    - ダメ。フォルダごと複製されてしまう
- 2 notepad.exe を software_reporter_tool.exe にリネームして上書きしてみた
    - 内部的に単に software_reporter_tool.exe 叩くだけなら、メモ帳立ち上がって終わりになる（実質無効化できる）はずだが
    - 2020/08/26 18:20:33 ダメだった。復活しやがる
- 消し方わからないので **起動時にプロセスチェックして出現してたら殺す** ことにした

[Google Chrome の Software Reporter Toolを無効化！ - Qiita](https://qiita.com/YuheiTani/items/162ce1d559d2618f31b4)

## ブックマークエクスポート
ブクママネージャ > 右上アイコンから可能

html

```html
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3 ADD_DATE="1592030598" LAST_MODIFIED="1592031076" PERSONAL_TOOLBAR_FOLDER="true">ブックマーク バー</H3>
    <DL><p>
        <DT><H3 ADD_DATE="1592030817" LAST_MODIFIED="0">hogehoge</H3>
        <DL><p>
        ……
```

## 初期設定
前提:

- Firefox メインで、サブとして Chrome 使いたい
    - Firefox は知的生産やプログラミング用で遊び要素入れたくない
    - Chrome 側で遊び要素やる（ネットサーフィン etc
- Chrome はログインしない閲覧専用用途

設定すること

- ブックマークと設定のインポート
    - プロファイル正しいの選ぶ
    - **すべてのFirefoxウィンドウ閉じてください** 出る
    - 閲覧履歴部分が特に時間かかる、CPUフルパワー
        - software_reporter_tool.exe 動いてて気持ち悪い
    - 終わらないのでchrome閉じた
- 同期とgoogleサービスは全部オフ
- プライバシーとセキュリティ
    - スペルチェックoff
    - cookieは終了時に削除
    - マイクなどは全部許可しないで
- 自動入力は全部オフ
- 閲覧データの削除
    - 詳細設定で

## 拡張
- ublock origin
- empty new page
    - https://chrome.google.com/webstore/detail/empty-new-tab-page/dpjamkmjmigaoobjbekmfgabipmfilij?hl=ja
    - デフォで about:blank できないので

## バイナリ
`C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`

