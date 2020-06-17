# コマンド、shell:xxxx、環境変数 etc

## shell:XXXX をコマンドラインで開く

```
explorer shell:recyclebinfolder
```

run からだとそのまま開けるが、それ以外では開けないので explorer から渡すようにする。

## ms-settings のリスト
[Windows 設定アプリの起動 - UWP apps - Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/uwp/launch-resume/launch-settings-app)

- `ms-settings:network-proxy`
- `ms-settings:windowsdefender`

## 設定をコマンドラインで開く
start ms-settings:system

run dialog から直打ちするなら `ms-settings:system` で良い。

## %appdata% と %localappdata%
[Windowsのディレクトリ構成ガイドライン - torutkのブログ](https://torutk.hatenablog.jp/entry/20110604/p1)

- %appdata% はコンピュータに依存しないもの（コピペして別環境でも使える）
- %localappdata% はこのコンピュータに依存するもの

……みたいだけどぶっちゃけよくわからん。

サマリー:

- %appdata% で見つからなかったら %localappdata% 見てみる
- %localappdata%\Microsoft\Outlook
