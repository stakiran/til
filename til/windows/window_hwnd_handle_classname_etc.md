# ウィンドウハンドルとかウィンドウクラス名とかそのへん

# ファイルを開くダイアログはどうやって特定する？
- 結論
    - ダイアログは `#32770`、タイトルは `ファイルを開く` で特定する
    - ウィンドウタイトル名も（言語問わないなら）固定なので、絞って使える

```
ff
  ファイルを開く
  #32770
vscode
  Open File
  #32770
hide
  ファイルを開く
  #32770
```

情報源:

- [About Window Classes - Win32 apps - Microsoft Docs](https://docs.microsoft.com/en-us/windows/win32/winmsg/about-window-classes)
    - > #32770 	The class for a dialog box.
- [GetOpenFileNameA function (commdlg.h) - Win32 apps - Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/win32/api/commdlg/nf-commdlg-getopenfilenamea?redirectedfrom=MSDN)
    - open, saveAs は win32api なので共通してるはず
