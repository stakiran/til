# Teraterm

## Q: ポートフォーワード越しの SSH 接続が通じない
- (フォーワード通じてアクセス新たな Teraterm 窓では)プロキシ設定外しましょう
    - 設定変えただけでは反映されないことがあるので **teraterm を立ち上げ直してやる** のが確実

## delete キーを有効にする
keyboard.cnf を以下のように（デフォでは insert の 338 に insert 以外が当たっている、などあべこべになっていることがある）。

```
;Insert key
Insert=338
;Home key
Find=327
;PageUp key
Prev=329
;Delete key
Remove=339
;End key
Select=335
;PageDown key
Next=337
```

加えて、設定 > keyboard を開いて、del キーのチェックを外す。

## Teraterm で接続設定を保存する
- 一通り設定する
- 設定 > 設定の保存
- どっかに ini を保存する

## Teraterm で接続設定を読み込む
**起動しただけでは読み込まれないのでまずは ini を読み込む**

- 設定 > 設定の読み込み
- 読み込みたい ini ファイルを指定

## ポートフォーワード SSH 転送設定 概要
- 設定 > SSH 転送

例: Sv1 に自席から `127.0.0.1:11111` でつなぎたい場合

```
myPC ---- Humidai ----- Sv1
        aa.aa.aa.aa   ss.ss.ss.ss
```

- 1: 踏み台アクセス **後に** 転送されるルートをつくる
  - ローカルのポート: `localhost`
  - リモート側ホスト: `ss.ss.ss.ss`
  - ポート: `11111`
- 2: 踏み台にアクセスするルートをつくる
  - 普通に秘密鍵、プロキシ、接続先 IP やポートなどを設定

上記全部できたら ini に保存しておくと良い。
