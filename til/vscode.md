# Visual Studio Code(VSCode)

## ● MacOS ショートカット

```
command + k, command + u          コメントアウト解除
command + k, command + c          コメントアウト
command + option + left/right     prev/next tab 分割をまたぐ
command + option + up/down        前後にマルチカーソルつくる
command + shift + v               markdown preview
shift + option + up/down          clone line to up or down
fn + up/down                      pageup, pagedown
option + z                        toggle wordwrap
command + k, command + left       focus to 隣のペイン
command + cursor                  move cursor to 上下左右端
command + shift + k               delete line
command + K, command + S          keyboard settings
command + P                       file search
```

## ● Windows ショートカット

```
ctrl + shift + >                  パンくずリストを開く
ctrl + shift + \                  対応する括弧に移動
```

あとは keyboard settings で調べればいいか。

## 開いているファイルのパス表示バー（パンくずリスト）を消す
- 設定を開く（ctrl + ,）
- breadcrumbs で探して、disable にする

## whitespace タブ スペースの可視化
- 拡張機能 whitespace+
- インストール後、コマンドパレットから whitespace+ toggle
- config いじれば、ファイル開いたときに自動で有効とかもできる

tab, 全角, 半角を色別に表示してくれるので見やすい

## マルチカーソル 選択範囲にマッチする部分を一つずつ選択していく
Ctrl + D

## マルチカーソル cursor クリックで増やす
Alt + クリック

## shift-jis を読み込むには？
ステータスバーの utf-8 部分クリック > reopen > shift-jis を選ぶ

## ctrl+k ctrl+u でインラインコメント除去
選択した後で押すと一気にできる。楽。

## ctrl+k ctrl+c でインラインコメント追加
選択した後で押すと一気にできる。楽。

## ctrl+k ctrl+s ← こういうのってどうやって押すの？ chords
- chords と呼ばれるやつ
- vscode の場合は、
    - ctrl+k を押す → ctrl+s を押す
    - 実は ctrl+k を押す → (ctrlを押したまま)sを押す、でもいける

たとえば toggle fold は ctrl+k ctrl+l だが、これは ctrl+k → (ctrl押したまま)l → (ctrl押したまま)k → (ctrl押したまま)l → …… と、押したまま k l k l ……と押すだけで toggle できる。

## キーボードショートカットを調べる
ctrl+k ctrl+s

インクリメンタルサーチで絞り込む

例: 動かす系の操作を調べたい場合 → `move` で検索してみるとか

## シンボル移動
ctrl + shift + o

## インデント上げる、下げる
ctrl + ]

ctrl + [

## Warning: "--debug-brk" is not available in Node.js v10.16.0; use "--inspect-brk" instead. ← これなに？
launch.json に書いてる protocol が古い。legacy から inspector にする。

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "name": "mocha test.js",
            "request": "launch",
            "program": "${workspaceRoot}/test.js",
            "stopOnEntry": false,
            "runtimeExecutable": "${env:APPDATA}/npm/mocha.cmd",
            "runtimeArgs": [],
            "args": [],
            "cwd": "${workspaceRoot}",
            "console":"integratedTerminal",
            "protocol": "inspector" ★ここ
        },
```

元々古い node.js(v5以下とか)用に protocol=legacy モードが用意されてた＆私もこれ使っていたが、今は node v10 であり legacy 使えないので、本来の inspector を指定せよって話。

## 常に新しいタブで開かれるようにする
- ファイル > 基本設定 > 設定
- 「enable preview」で検索する

"workbench.editor.enablePreview": false

↑ これっぽい設定があるはずなのでオフに

参考: https://stackoverflow.com/questions/38713405/open-files-always-in-a-new-tab

## メニューバーとタイトルバーが一緒になっているのを別々に分ける
v1.30.1 の話。

- ファイル > 基本設定 > 設定
- 「title bar」で検索する
- Title Bar Style を native にする
- VSCode を再起動したら反映される

## VSCode で、古い node でデバッグ実行する
デバッグ実行すると `...%appdata%/npm/mocha.cmd --inspect-brk=24783 test.js` のようなコマンドラインが実行されるが、node v6 以前など古い node では inspect オプションに対応してないため実行できない。

これを回避するためには、以下のように launch.json に `"protocol": "legacy"` を追加してやる。

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "name": "mocha test.js",
            "request": "launch",
            "program": "${workspaceRoot}/test.js",
            "stopOnEntry": false,
            "runtimeExecutable": "${env:APPDATA}/npm/mocha.cmd",
            "runtimeArgs": [],
            "args": [],
            "cwd": "${workspaceRoot}",
            "console":"integratedTerminal",
            "protocol": "legacy"
        }
    ]
}
```

## ctrl + tab で次のタブ
ファイル > 基本設定 > キーボードショートカット

keybindings.json に以下を書く。

```json
{
    "key": "ctrl+tab",
    "command": "workbench.action.nextEditor"
},
{
    "key": "ctrl+shift+tab",
    "command": "workbench.action.previousEditor"
}
```

参考: https://stackoverflow.com/questions/38957302/is-there-a-quick-change-tabs-function-in-visual-studio-code
