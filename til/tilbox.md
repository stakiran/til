# tilbox

## macos で GUI アプリをターミナルから開く
- `open -a` でアプリ名を指定
- アプリ名はアプリケーションフォルダ内のファイル名（とか Alfred から見えるやつ）

```
alias drawio="open -a 'draw.io.app'"
```

## linux using port 調べる
一覧

```
$ lsof -i -P
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3 1807 ssm-user    3u  IPv4  24381      0t0  TCP *:8080 (LISTEN)
```

絞る

```
$ lsof -i:80
$ lsof -i:8080
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3 1807 ssm-user    3u  IPv4  24381      0t0  TCP *:http-alt (LISTEN)
```

## cmd コマンドプロンプトで改行文字を扱う
[コマンドプロンプトやバッチファイルで、環境変数に改行文字(LF)を入れて使う。: Windows Script Programming](http://scripting.cocolog-nifty.com/blog/2008/11/lf-7446.html)

環境変数に定義 + 遅延展開という荒業ならいけるらしい。

## コマンド出力の行末空行 newline をカットする

```
| cut -d$'\n' -f1
```

cmd では `\n` が改行文字にならないので不可能。

## mac で gif 撮影
[.mov を gif に変換【Mac】 - Qiita https://qiita.com/ntkgcj/items/6ac08a007f24a2de0b36]

- 動画キャプチャなどでmovを撮影
- `ffmpeg -i 画面収録_299U-08-09_1.93.N.mov -r 24 gamen_test1.gif`
    - brew install ffmpeg でインストールする

## mac 選択範囲を動画キャプチャ
shift + command + 5

## mac スクリーンショット command + shift + 3/4
3 は画面全体
4 は範囲選択

ctrl も加えたらクリップボードコピーになる。

## clipmenu
clipmenu.app はダウンロードフォルダにあった。 2020/04/07 12:38:17

## vscode で右クリックメニューできない
かざぐるマウスで chromium 系のチェックを外す。

## vscode で ctrl k ctrl s の chords 効かないときは ahk を疑え

```
^k::Send {F7}
```

↓

```
#IfWinNotActive ahk_exe Code.exe
^k::Send {F7}
#If
```

## ファイル内タグ 検索 vscode
option + u に以下コマンドを btt で登録

    echo tag_`uuidgen | cut -c 25-` | tr -d "\n" | pbcopy

vscode でタグ入れる

    option + u
    command + v

タグで検索する

    command + F

## uuid
uuidgen

$ uuidgen | cut -c 25- | tr -d "\n" | pbcopy
最後の12桁だけとる

$ echo tag_`uuidgen | cut -c 25-` | tr -d "\n" | pbcopy
先頭に tag_ 文字をつける

## twitter list url
https://twitter.com/stakiran2/lists/taskmanagement

https://twitter.com/(account-name))/lists/(list-name)

大文字小文字問わない
ログインしなくても読める

余談だが following/followers/likes はログインしないと見れない。

## windows 永続 ping
`-t` オプション

## alfred ファイルがみつからない場合はスペースを
スペースを先頭に入れると `,` が出て、アプリではなくファイル検索になる。

gistfile1.md とか表示されるようになった at 2020/01/20(Mon) 16:41:42

## よく使う記号
★
≒
※

## 商標、登録商標、™️、®️
商標は単に目印。誰でも使ってれば発生するが権利はない。™️ トレードマークで明示できる。

登録商標は特許庁で承認済。®️で示す。

## ●sublime recent shortcuts
option + left drag     矩形選択

## git 一つ前のコミットに戻す
git revert (コミットしたばかりのリビジョンのコミットID)

例:
git revert 81a80c31800c393f0a8cf4abb6fd69526d0ea599

## github clone with ssh
git clone git@github.com:stakiran/text.git

## mac 検索 前後ろ
command (+ shift) + G

## mac firefox 更新
command + shift + r

## vscode markdown アウトライン outline
- breadcrams パンくずリストが良さげ
  - mac: command + :
  - win: ctrl + shift + :

以下は微妙

- command + shift + o でシンボルジャンプ
  - 表示は常に一番上から
  - markdown の場合、見出しがシンボルになってるのでアウトラインできる
- focus outline view
  - とりあえず control + o に充てた
  - outline view 上で移動できる、フォーカスも自然
  - エディタ領域でのカーソル位置を view が追従しないのが微妙
- いずれにせよ検索で絞り込めるのは強い

## macos btt 日付時刻文字列挿入
できた

bettertouchtool > settings > global の keyboard
action は utility > paste custom text で、datetime のフォーマットを。

```
(BTT)@dateformat:yyyy/MM/dd hh:mm:ss(BTT)
(BTT)@dateformat:yyMMdd(BTT)
(BTT)@dateformat:hh:mm:ss(BTT)
```

## terminal control + u で入力クリア

## macos dateコマンドとか

```
$ cat yyyyfull.command 
#!/bin/sh
#cd `dirname $0`
#date +"%Y/%m/%d(%a) %H:%M:%S" | tr -d "\n" | pbcopy
date +"%Y/%m/%d %H:%M:%S" | tr -d "\n" | pbcopy
#osascript -e 'tell application "Terminal" to quit' &
exit
```

```
$ osascript -e 'tell application "Terminal" to do script "echo `date +\"%y\"`; exit"'
```

## mac defaults 設定をコマンドラインで

```
# Disable warning when quitting
defaults write com.googlecode.iterm2 PromptOnQuit -bool false

# Show Status bar in Finder （ステータスバーを表示）
defaults write com.apple.finder ShowStatusBar -bool true

# Show Path bar in Finder （パスバーを表示）
defaults write com.apple.finder ShowPathbar -bool true

# Show Tab bar in Finder （タブバーを表示）
defaults write com.apple.finder ShowTabView -bool true

# 全ての拡張子のファイルを表示
defaults write NSGlobalDomain AppleShowAllExtensions -bool true

# 拡張子変更時の警告を無効化
defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false

# Set `${HOME}` as the default location for new Finder windows
# 新しいウィンドウでデフォルトでホームフォルダを開く
defaults write com.apple.finder NewWindowTarget -string "PfDe"
defaults write com.apple.finder NewWindowTargetPath -string "file://${HOME}/"
```
