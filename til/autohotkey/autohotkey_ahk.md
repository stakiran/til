# AutoHotkey

# ●template

```
SetWorkingDir %A_ScriptDir%
CoordMode Menu, Screen
CoordMode Mouse, Screen
CoordMode Caret, Screen
FileEncoding, CP65001

; config
#Include %A_ScriptDir%\config.ahk
```

# ●class クラス

```
class Counter {
  __New(){
    this._v := 0
  }

  plus(){
    curv := this._v
    newv := curv + 1
    this._v := newv
  }

  get(){
    Return this._v
  }
}

counter := new Counter()
counter.plus()
```

# gui add 内部でホットキー

```
keyExit := "Esc"
Hotkey, %KeyExit%, press_esc
Gui, Add, Hotkey, vDummy, %KeyExit%

return

press_esc:
close:
ExitApp
```

# gui add text で折り返し(wrap)
150pixelの場合

```
+Wrap w150
```

see [Where do I put "Wrap" to wrap text in a GUI Text - Ask for Help - AutoHotkey Community https://www.autohotkey.com/board/topic/31966-where-do-i-put-wrap-to-wrap-text-in-a-gui-text/]

# 改行は `n
`\n` ではない

# 式に出現する % は %% 囲みと同じ意味
[When single percent % signs are used in the script? - Ask for Help - AutoHotkey Community https://www.autohotkey.com/board/topic/149907-when-single-percent-signs-are-used-in-the-script/]

以下は全部同じ

```
MouseMove, % adjx, % outy
MouseMove, %adjx%, %outy%
MouseMove, adjx, outy
```

ただし一番下は MouseMove が expression を許してるから使える

# UTF8 CP65001 は ahk ファイルに BOM がないと文字化けする
gui text で文字化けした

```
FileEncoding, CP65001

Gui, Add, Text,, おはよう！
Gui, Show
```

# and or not
and とかも使える

```
#If !WinActive("ahk_exe Code.exe") and !WinActive("ahk_exe ONENOTE.EXE")
^k::Send {F7}
#If
```

```
&&
||
!
```

# backtick バッククォートを扱う
デフォでは ` がエスケープ文字なので、別のに切り替える。

```
#EscapeChar \
::@@@::
  SendInput ```
return
#EscapeChar `
```

# クリップボードにコピー
`:=` だと上手く動いてくれないことがある？

```
copy_method(s){
  clipboard = %s%
}
```

# 日付時刻 datetime

```
FormatTime, d_yyyymmdd,, yyyy/MM/dd
FormatTime, d_hhmmss,, HH:mm:ss
d_dow := get_dowstr()
d_yyyymmdd_hhmmss := d_yyyymmdd " " d_hhmmss
d_yyyymmdd_dow_hhmmss := d_yyyymmdd " (" d_dow ") " d_hhmmss

FormatTime, d_yymmdd_short,, yyMMdd
FormatTime, d_hhmmss_short,, HHmmss
FormatTime, d_hhmm_short,, HHmm
d_yymmdd_hhmmss_short := d_yymmdd_short "_" d_hhmmss_short

get_dowstr(){
  FormatTime, downum,, WDay
  dowtable := "SunMonTueWedThuFriSat"
  startpos := ((downum-1)*3)+1
  dowstr := ""
  StringMid, dowstr, dowtable, %startpos%, 3
  return dowstr
}
```

# キャレット位置の取得

```
CoordMode Caret, Screen
pos := {}
pos.x := A_CaretX
pos.y := A_CaretY
```

# 自身のディレクトリやフルパス 

```
BASEDIR = %A_ScriptDir%
FULLPATH_SCRIPT = %A_ScriptFullPath%
```

# 修飾キー押しっぱを検出する

```
open_method(fullpath){
  s := GetKeyState("Shift")
  a := GetKeyState("Alt")
  c := GetKeyState("Control")
  w := GetKeyState("LWin")

  ; shift 押下
  if(s && !a && !c && !w){
    MsgBox % "Edit open"
    Return
  }

  ; ctrl 押下
  if(!s && !a && c && !w){
    MsgBox % "Directory open"
    Return
  }
  ; open normally.
  Run, %fullpath%
}
```

# undefined

```
is_nothing(obj){
  Return obj==""
}
```

# 改行とかタブ文字とか whitespace tab

```
`n
`t
```

# 指定ウィンドウのみ 指定ウィンドウ以外 window active
引数は ahk_class ahk_exe などが使える。

```
#If WinActive("ahk_class #32770")
ScrollLock::run, D:\bin\dialis\dialis.exe
#If

#If !WinActive("ahk_class Hidemaru32Class")
!d::run, D:\work\github\stakiran\temp\191217_ahk_datetime_menu\menu_datetime.ahk
#If
```

# split 配列変数定義 アクセス
".git;box" など

```
config_exclude_foldername := CONFIG.EXCLUDE_FOLDERNAME
StringSplit, exclude_folders, config_exclude_foldername, ";"

exclude_folderlist := Object()

Loop, %exclude_folders0%
{
  excluder_name = exclude_folders%A_Index%
  exclude_folderlist.Insert(%excluder_name%)
}

For index,element in exclude_folderlist
{
  MsgBox % "Element number " . index . " is " . element
}
```


# 現在日付時刻
組み込み変数が便利

```
t := A_Hour*100 + A_Min
if(1600<=t){
  MsgBox "16:00 過ぎたぜ"
}
```

# スリープ

```
; 1秒
Sleep 1000
```
