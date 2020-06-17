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
