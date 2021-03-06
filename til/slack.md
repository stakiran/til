# Slack
- [検索クエリ](https://slack.com/intl/ja-jp/help/articles/202528808-Slack-%E5%86%85%E3%82%92%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B)
- [スラッシュコマンドリファレンス](https://slack.com/intl/ja-jp/help/articles/201259356-%E3%83%93%E3%83%AB%E3%83%88%E3%82%A4%E3%83%B3%E3%81%AE%E3%82%B9%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B)

## デスクトップアプリ x64 in win10 
2020/03/03 17:11:33 中止。**通知ポップアップを無効にする手段がないから**

2020/03/03 15:35:24

- メモリ: 300MB
- プロセス: 5個くらい
- `%localappdata%\slack`
    - 起動時、作業ディレクトリは `app-xxxx` まで掘られてるので注意

設定

- ダウンロードのロケーション: 変える
- ログイン時にアプリを起動する: off
- ウィンドウが閉じてる間も……起動中にしておく: off
- 通知系全体的に

## 今日の日付に飛ぶ
適当な内容でつぶやく。

分報以外ではきついかも。

## 分報
`z-times-YOURNAME` で。

表示上で最後になるよう z つけるのが望ましい。

## Q: プライベートチャンネルの最後の一人が退出したらどうなる？
Ans: **退出されずに** アーカイブされる

つまり自分一人だけが見えるアーカイブ( :question: 未確認 どうだろ)、という状態。

ちなみに **退出は不可能**

## アカウント設定 メアドなど
/account/settings にアクセスするか、

- 左上 > プロフィール＆アカウント > 「…」の縦アイコン > アカウント設定

## english emoji 英語名の絵文字を知る
日本語だと絵文字名わからずに GitLab など他への応用ができないので調べる。

F12 ツールで見れた。

## ミュートしてるチャンネルの通知を無効にする
情報アイコン(!) クリック > 通知設定 > 環境設定を編集する

`@channel と @here を無効に……` 的なやつをオンにする

## WYSIWYG がうざいです
~~コピペ後、ctrl + shift + f で plain text 展開可。~~ 環境設定 > 詳細設定 > 入力オプション > マークアップでメッセージを書式設定する onにする

## 指定の日付に移動する、が動作しない
以下の場合はジャンプできない。

- その日に投稿がない場合
- その日の投稿が「～～さんが参加しました」などシステムメッセージのみの場合

ジャンプ出来ない場合は何も怒らない＆カレンダー上もジャンプ可否がわからないので **ジャンプできる日にあたるまで一日ずつ試すしかない** というちょっと不親切な仕様。

フィードバック投げたら「今はできない」「参考にします」とのこと

> たしかに不便かと思いますので、今回いただいた内容を社内へフィードバックさせていただきます。
> 
> 貴重な提案をありがとうございました！他にも気になったことがありましたら、こちらに連絡していただければと思います。

## 投票する
- `:1:` とか `:2:` とかの絵文字使って選択肢示す

```
(聞きたいこと)

:1: 
:2: 
:3: 
:4: 
```

## 絵文字を追加する
- 左上 > Slack をカスタマイズ 
- カスタム絵文字を追加するボタン
    - 文字絵文字は [絵文字ジェネレーター](https://emoji-gen.ninja/) 使うと楽

似た単語でも引っ掛けたい場合はエイリアスも登録しておく。

### あると便利な絵文字
- 既読
- 完了・済
- 了解
- 承知
- ありがとうございます
- 同意系
    - それな
    - わかりみが深い
- ……

## 検索 > 指定絵文字のついたメッセージ
`has::memo:`

`has:` の後に `:emoji:` をつける。 `::` が続いて違和感あるがそんなもん。

## REST API
要点:

- 1: トークンを発行する
    - **ワークスペース管理者の許可(Approval)が必要**
- 2: HTTP REQUEST のヘッダに 1 のトークンひっつけてリクエスト

リンク:

- [API Methods](https://api.slack.com/methods)
- [Rate Limits](https://api.slack.com/docs/rate-limits)
- [Paginating through collections](https://api.slack.com/docs/pagination)

### 例: 指定チャンネルの全メッセージを取るには？
こんな流れ:

- 1: [conversations.list](https://api.slack.com/methods/conversations.list) でチャンネル一覧をゲットしチャンネル ID を得る
- 2: [channels.history](https://api.slack.com/methods/channels.history) で指定 ID のチャンネルからメッセージを取る（Paginative)
    - メッセージ総数を事前に知りたいなら [search.messages](https://api.slack.com/methods/search.messages) で responce["messages"]["total"] とか見る

## チャンネルを削除する(アーカイブ)
削除という概念は無いので **アーカイブ** にする。

- ギアアイコン > その他のオプション > このチャンネルをアーカイブする

アーカイブ後の復元も可能。

## :memo: 初学者向けに教えること
まずは [Slack ヘルプセンター](https://slack.com/intl/ja-jp/help) を熟読する

- チャットコミュニケーションには実地的だが「一つの体系的手法」であるため **ちゃんと勉強する** 必要がある（テキトーに使っても恩恵は受けられない）
- 数時間くらいかけて熟読してもバチは当たらない

### 脱初心者向けクイズ
この辺に答えられるようになったら脱初心者。

- DM とプライベートチャンネルとパブリックチャンネルの違いは？
- Mention は何のためにあるか
- Reply(スレッド) は何のためにあるか
- Mute は何のためにあるか
- #general で雑談してはいけない理由は？
- 無闇に DM やプライベートチャンネルで済ませるのではなく、なるべくパブリックチャンネルを使うべきなのはなぜか
- なぜメールよりも Slack を使うべきか
- なぜ他のチャットサービスよりも Slack を使うべきか
