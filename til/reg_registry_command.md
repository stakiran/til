# reg command reg query etc

## query

```
$ reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU
    DetectionFrequency    REG_DWORD    0x10
    ……

$ reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "DetectionFrequency"

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU
    DetectionFrequency    REG_DWORD    0x10

$ reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "DetectionFrequencyzzz"


エラー: 指定されたレジストリ キーまたは値が見つかりませんでした

$ reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AUzzz" /v "DetectionFrequency"
エラー: 指定されたレジストリ キーまたは値が見つかりませんでした
```

## add

```
$ reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "DetectionFrequencyNEWVALUE" /t "REG_DWORD" /d "0x10"
この操作を正しく終了しました。

  →未存は即新規

$ reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\ZZZ\ZZZ" /v "DetectionFrequencyNEWVALUE" /t "REG_DWORD" /d "0x10"
この操作を正しく終了しました。

  →未存キーも即新規。ネストでも問題なく新規できる。

$ reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "DetectionFrequency" /t "REG_DWORD" /d "0x10" /f
値 DetectionFrequency は存在します。上書きしますか? (Yes/No) y
この操作を正しく終了しました。

  →既存だと確認

$ reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "DetectionFrequency" /t "REG_DWORD" /d "0x10" /f
この操作を正しく終了しました。

  → /f で確認ナシにできる。
```
