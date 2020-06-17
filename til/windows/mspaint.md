# mspaint.exe paint ペイント

## ペイントでモザイクを入れる
- 範囲選択して Ctrl + W
- 25% で確定
- もう一度開いて 400% で元に戻す

上限が 400% なので（できるだけ粗くしたいなら）25% を使うしかない。

## mspaint.exe のレジストリ設定
- キーは HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Paint
- 終了時の設定が保存される
- ここいじった後に mspaint.exe 開けば、いじった設定が使われる

設定値:

- キャンバスサイズ
    - HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Paint\View
    - BMPHeight
    - BMPWidth
- フォントサイズとフォント名
    - HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Paint\Text
    - PointSize
    - TypeFaceName

無いもの:

- デフォの保存先ディレクトリ
- デフォの保存拡張子
- テキストの透明/不透明指定
