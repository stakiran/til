# Windows Defender AV

## ExclusionProcess と ExclusionPath の違い
- Process は「指定プロセス **が開くファイル** を除外する」
    - >This cmdlet excludes any files opened by the processes that you specify from scheduled and real-time scanning.
- Path は指定パスが表すファイルやフォルダ(内の全ファイル)を除外する
- **プロセス自体を除外したければ Path を使う**
    - > Specifying this parameter excludes files opened by executable programs only. The cmdlet does not exclude the processes themselves. To exclude a process, specify it by using the ExclusionPath parameter.

## 自分好みの設定にする

```
$ cd (yourWorkFolder)

$ powershell -Command "Get-MpPreference > before.txt"

$ (yourEditor) defender_config.ps1
Set-MpPreference -ScanScheduleDay 7
...
(好みの設定を書く)
...
Get-MpPreference > after.txt

$ powershell ./defender_config.ps1
```

あとは defender_config.ps1 をいじる＆実行するを繰り返しながら、WinMerge で before/after をチェック。

## get-mppreference で値を省略させずに見る

```
(PS)$ $pre = get-mppreference
(PS)$ $pre.ExclusionExtension
db
js
lib
log
md
py
txt
yml
```

## 必要な情報一式
- official
    - [Set-MpPreference - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=win10-ps)
    - [Windows Defender AV で定期的なクイック スキャンとフル スキャンをスケジュールする - Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus)
- github 実例
    - [Search · Set-MpPreference](https://github.com/search?l=PowerShell&q=Set-MpPreference&type=Code)

設定例:

```
$ powershell
(powershell) Get-MpPreference | clip
＜エディタにコピペして見る＞
```

```
$ powershell
(powershell) Set-MpPreference -ScanScheduleDay 7
(powershell) Set-MpPreference -DisableArchiveScanning $True
```
