# Python ctypes win32api

## SetCursorPos, GetCursorPos

```
import ctypes

def get_cursor_pos():
    point = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    ret = (point.x, point.y)
    return ret

def set_cursor_pos(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
```

## GetForegroundWindow, GetWindowRect

```
import ctypes
from ctypes.wintypes import RECT

def get_foreground_window():
    return ctypes.windll.user32.GetForegroundWindow()

def get_window_rect(hwnd):
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.pointer(rect))
    ret = {
        'x1'  : rect.left,
        'y1'  : rect.top,
        'x2'  : rect.right,
        'y2'  : rect.bottom
    }
    return ret
```
