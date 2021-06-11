# BitLocker

## BitLocker を設定したことにする
ここ？

- HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\FVE

見つからん

- [オペレーティング システム ドライブの暗号化設定 https://admx.help/?Category=MDOP&Policy=Microsoft.Policies.BitLockerManagement::BMSOSDEncryptionPolicy&Language=ja-jp]
    - HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\FVE\MDOPBitLockerManagement
    - ShouldEncryptOSDrive
    - 1 にしたら bitlocker 設定したとみなせる？
    - システム設定からは無効のままが見えてる
    - 試す at 2021/06/08
