# glob

## subdirectory サブフォルダ含めてファイル一覧

```
import glob
import os

def get_filename(path):
    return os.path.basename(path)

def get_basename(path):
    return os.path.splitext(get_filename(path))[0]

favorites_dir = os.path.join(
    os.environ['USERPROFILE'],
    'favorites'
)
query = '{}/**/*.url'.format(favorites_dir)
favorites_files = glob.glob(query, recursive=True)

for urlfile in favorites_files:
    title = get_basename(urlfile).lower()
    ...
```
