# Python Pillow
- save はフォーマット未指定ならファイル名拡張子から判断
- 対応フォーマットは `python -m PIL` で見れる

## クリップボードのイメージを保存

```python
# encoding: utf-8

import datetime
import os
import sys

from PIL import ImageGrab, Image

def today_datetimestr():
    todaydt = datetime.datetime.today()
    dtstr = todaydt.strftime('%Y%m%d_%H%M%S')
    return dtstr

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)

clipboard = ImageGrab.grabclipboard()
is_not_image = not isinstance(clipboard, Image.Image)
if is_not_image:
    print('Not image.')
    sys.exit(1)

outname = '{}.png'.format(today_datetimestr())
outfull = os.path.join(MYDIR, outname)
clipboard.save(outfull)
print('Image {} saved.'.format(outname))
```

## 指定画像ファイルのリサイズ

```python
from PIL import Image
from PIL import ImageFile

# 画像ファイル名から画像ハンドル？をゲットして、
img = Image.open(infilepath, 'r')

# リサイズ後のサイズを指定してリサイズ実行
w, h = 640, 480
newsize = (w, h)
resized_img = img.resize(new_size)

# リサイズした画像ハンドル？を保存する。
resized_img.save(outfilepath, 'JPEG',
    quality=100,
    optimize=True,
    progressive=True
)
```

以下はリサイズ比ベース

```
img = Image.open(infilepath, 'r')

# これで元画像のサイズをゲット
w, h = img.size

# あとはよしなに
```

## 画面キャプチャ on Windows

```python
from PIL import ImageGrab

def capture_fullscreen():
    return ImageGrab.grab()

def capture_rect(x1, y1, x2, y2):
    return ImageGrab.grab(bbox=(x1, y1, x2, y2))

def save_to_png(grab_obj, filename):
    grab_obj.save('{}.png'.format(filename))

def save_to_jpeg(grab_obj, filename):
    grab_obj.save(
        '{}.jpeg'.format(filename),
        quality=100,
        optimize=True,
        progressive=True
    )
```
