# Windows Defender ATP
- [Microsoft Defender Advanced Threat Protection - Configuration Manager - Microsoft Docs](https://docs.microsoft.com/ja-jp/configmgr/protect/deploy-use/windows-defender-advanced-threat-protection)
- [Microsoft Defender Advanced Threat Protection - Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/security/threat-protection/microsoft-defender-atp/microsoft-defender-advanced-threat-protection)

## 所感
- 動作
    - **プロセスの実行を監視している**
    - スキャンほど重くはない
    - cpu で言えば 0.5% ～ 7% くらい
- 動作よくわかってないので勉強せねば
- 設定画面もよくわかってない

## ポータル
https://securitycenter.windows.com/

## サービス
Windows Defender Advanced Threat Protection Service

```
$ sc qc sense
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: sense
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 2   AUTO_START  (DELAYED)
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe"
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Windows Defender Advanced Threat Protection Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem
```

## コマンドライン
C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe
