# Python Pillow

## 指定画像ファイルのりサイズ

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
