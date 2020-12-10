# Box Notes

## 壊れた Box Notes ファイルを復旧する
バージョン管理から古いバージョンに戻す。

たとえば https://www.box.com/notes/XXXXXXXXXXXX が壊れた場合、

- https://www.box.com/file/XXXXXXXXXXXX?sb=/activity/versions/ を開く
    - notes じゃなくて file に
    - 末尾に ?sb=/activity/versions/
- バージョン管理画面が出るので、古いバージョンを復元してみる

## デフォの Box Note 保存先を変える
デフォでは「私のBox Notes」配下になるが変更可。

- ブラウザ版にログイン
- 左下ギアアイコン > デフォルトの保存場所を変更

## Box Notes の内容をインデントつきでテキストにコピペする
- winword に貼り付ける
- winword からエディタに貼り付ける
- 先頭の文字は以下のようになっているので、適宜置換する
    - レベル1: `•	`
    - レベル2: `o	`
    - レベル3: `	`
    - ちなみにレベル4以降は無い（box notes側でレベル4以降があってもレベル3に集約される）

```
•	
  o	
    	
```

## ●ショートカットキー
- ctrl + / で一覧出せることだけ覚えておけばいい
- ctrl + > による文字サイズ変更は、文字選択しないとダメです
- ctrl + alt + 8/9 の箇条書き/打ち消し線、これだけで基本的には ok

## アプリ
- Download Box Notes for Mac or Windows - Box Notes
    - https://www.box.com/ja-jp/resources/downloads/notes

`"%localappdata%\boxnotes\Box Notes.exe"`
