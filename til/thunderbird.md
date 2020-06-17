# Thunderbird

## テキスト形式で編集する
アカウント設定 > 編集とアドレス入力 > HTML 形式 のチェックを外す

## ヘッダ
Ctrl + U

表示 > メッセージのソース

## google mail で SMTP が送れない
https://support.google.com/mail/troubleshooter/1668960?hl=ja&rd=1#ts=1665018%2C1665141%2C2769074

- smtp.googlemail.com → smtp.gmail.com に変える
- SMTPの設定は、設定画面の一番下の項目から一括設定する
- アカウントAだったら、アカウントAのメアドが対応したSMTP設定を選ぶこと

この辺を気をつけたらいけた。

## 編集画面での折り返しを無効にする
- プレーンテキスト編集用には mailnews.wraplength を変更
- HTML編集用には editor.htmlWrapColumn を変更

双方ともデフォルト値は 72 

## 折り返しを無効にする方法
-  [オプション] - [詳細] - [一般] - [設定エディタ] から設定エディタを起動
-  mailnews.wraplength の値を 0 に設定
-  editor.htmlWrapColumn を 0 に設定

## フォルダの整理

```
・自由に並び替えたいなら Manualy sort folders アドオンを使う。
  ただしCRUDしたフォルダの順番は崩れてしまうので、
  その度に並び替えしなおさないといけない。

・フォルダ名にPrefixを付けて整列するのが楽

・メッセージフィルタの移動先フォルダは, フォルダ場所を変えても変わらない.
```

## 添付ファイルをプレビューしない
表示 > 添付をインラインで表示 off
