# Boost Note

## Q: 指定 repo を読み込ませることはできる？
できないです（下記のように json 専用フォーマットで保存されるので）

## storage の中身
- boostnote.json
- (storageのパス)/attachments/添付ファイル類？
- (storageのパス)/notes/XXXXXXXXX.json

XXXXXXXXX.json

```json
{"_id":"note:XXXXXXXXX","title":"title1","content":"- aaa\n- aaa","tags":[],"folderPathname":"/","data":{},"createdAt":"GMTっぽいんだけど","updatedAt":"GMTっぽいんだけど","trashed":false,"_rev":"XXXXXXXXX"}
```

## bin

```
"%localappdata%\Programs\boostnote.next\Boost Note.exe"
```

