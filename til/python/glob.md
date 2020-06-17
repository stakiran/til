# glob

## subdirectory サブフォルダ含めてファイル一覧

```
import glob
import os

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
