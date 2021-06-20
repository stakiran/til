# BitLocker

## 1 レジストリ初動
ここ？

- HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\FVE

見つからん

- [オペレーティング システム ドライブの暗号化設定 https://admx.help/?Category=MDOP&Policy=Microsoft.Policies.BitLockerManagement::BMSOSDEncryptionPolicy&Language=ja-jp]
    - HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\FVE\MDOPBitLockerManagement
    - ShouldEncryptOSDrive
    - 1 にしたら bitlocker 設定したとみなせる？
    - システム設定からは無効のままが見えてる
    - 試す at 2021/06/08
    - 効果なし at 2021/06/16

ドライブのプロパティとして見えているから、ドライブ単位の設定なのかもしれない

## 2 manage-bde を wrap する
仮に manage-bde status の結果をパースしているのだとしたら。

```
$ manage-bde -status c:
……
    変換状態:               暗号化は完全に解除されています
    暗号化された割合:       0.0%
    暗号化の方法:           なし
    保護状態:               保護はオフです
    ロック状態:             ロック解除
……
```

```
$ where manage-bde
C:\Windows\System32\manage-bde.exe
C:\Windows\System32\manage-bde.wsf
```

Wrapper batch を PATH に通してみる

- `d:\path\wrapper` つくる
- システム環境変数側の PATH の、systemroot より上に追加

manage-bde.bat をつくって置く

```bat
@echo off
……
echo.
……
echo     BitLocker のバージョン: なし
echo     変換状態:               暗号化は完全に解除されています
……
```

文言を変えるために、暗号化後の問題を探す

- [1](https://echoecho.hatenablog.com/entry/2019/04/03/%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%A7%E3%81%AEBitLocker%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%BF%E3%82%B9%E7%A2%BA%E8%AA%8D)
    - インデントがわからん
- [2](https://so-zou.jp/software/tool/security/bitlocker/)
    - 各設定値が詳しい

いや、インデントは要らないか。文言変えた。これで様子見 at 2021/06/16
