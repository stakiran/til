# Python パス操作

## パスの一部を取り出す

```
def get_filename(path):
    return os.path.basename(path)

def get_basename(path):
    return os.path.splitext(get_filename(path))[0]
```
