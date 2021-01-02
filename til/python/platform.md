# Python platform

## macos 判定

```py
def is_mac():
    import platform
    p = platform.platform()
    if len(p)>=6 and p[:6]=='Darwin':
        return True
    return False
```

使うときはこんな感じ

```py
# ...
# is_mac() の定義は先にしておく必要がある
# ...

if is_mac():
    import libclipboard_mac as libclipboard
else:
    import libclipboard
```
