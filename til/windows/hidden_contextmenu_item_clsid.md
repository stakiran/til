# 右クリックメニューの項目非表示化
以下からそれっぽいものの CLSID を無効にする

```
HKEY_CLASSES_ROOT\*\shellex\ContextMenuHandlers
HKEY_CLASSES_ROOT\Directory\shellex\ContextMenuHandlers
HKEY_CLASSES_ROOT\Folder\shellex\ContextMenuHandlers
HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers
HKEY_CLASSES_ROOT\AllFilesystemObjects\shellex\ContextMenuHandlers
```

無効化方法

- `{474C98EE-CF3D-41f5-80E3-4AAB0AB04301}` → `zzz{474C98EE-CF3D-41f5-80E3-4AAB0AB04301}`

## CLSID

| CLSID | Name |
| ----- | ---- |
| `{A470F8CF-A1E8-4f65-8335-227475AA5C46}` | EncryptionMenu 共有とセキュリティ |
| `{CB3D0F55-BC2C-4C1A-85ED-23ED75B5106B}` | FileSyncEx OneDriveの内部名 |
| `{596AB062-B4D2-4215-9F74-E9109B0A8153}` | 以前のバージョンの復元 |
| `{474C98EE-CF3D-41f5-80E3-4AAB0AB04301}` | Offline files 常にオフラインで使用する |
| `{f81e9010-6ea4-11ce-a7ff-00aa003ca9f6}` | Sharing 共有 |
| `{a2a9545d-a0c2-42b4-9708-a0b2badd77c8}` | StartMenuPin |
| `{90AA3A4E-1CBA-4233-B8BB-535773D48449}` | TaskBandPin |
| `{09A47860-11B0-4DA5-AFA5-26D86198A780}` | EPP WindowsDefenderでスキャン |
| `{3dad6c5d-2167-4cae-9914-f99e41c12cfa}` | ライブラリに追加 |
| `` |  |
| `` |  |
