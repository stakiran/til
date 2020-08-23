# :x: マウスカーソルの移動範囲を制限する with ClipCursor()

## 背景
- 左にノート、右にモニタの2画面
- 右がメインモニタで、左がサブ
    - つまりサブ側には x<0 でアクセス
- 普段はメインだけ使ってる
    - **このとき迂闊にサブ側に入るのがうっとうしい**

## ref
- [ClipCursor API 関数解説](https://www.tokovalue.jp/function/ClipCursor.htm)
- [ClipCursor function (winuser.h) - Win32 apps | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/win32/api/winuser/nf-winuser-clipcursor)
- [win32api__ClipCursor_meth.html](http://timgolden.me.uk/pywin32-docs/win32api__ClipCursor_meth.html)
- [how to 'undo' ClipCursor(rect)](https://forums.codeguru.com/showthread.php?298732-how-to-undo-ClipCursor%28rect%29)
    - > ClipCusor( NULL ) worked.

## src

```python
# -*- coding: utf-8 -*-

import os
from time import sleep

import win32api
import win32con

dispx = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
dispy = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

sx = 0
sy = 0
gx = dispx
gy = dispy
rect = (sx, sy, gx, gy)

print('Restricted mouse cursor between ({},{}) and ({},{})'.format(sx, sy, gx, gy))
win32api.ClipCursor(rect)
while True:
    sleep(5.0)
win32api.ClipCursor()
```

## 効果
ありませんでした。

どころかサブ側ではマウスカーソルがデフォにリセットされた？（普段は実用カーソルにしている）

## なんで？
- たぶんアクティブウィンドウ単位でしか作用しないから
    - MS Docs にはその旨記述されてないけど……

[.net - Trapping mouse on one monitor - Stack Overflow](https://stackoverflow.com/questions/18186946/trapping-mouse-on-one-monitor)

- アクティブウィンドウ変えたら切れてしまう
- カウンターとしてマウスをフックして無理やり制限してしまう案が出てる
