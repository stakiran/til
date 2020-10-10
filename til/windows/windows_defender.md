# Windows Defender AV / リアルタイム保護

## 弾いてるはずなのに MsMpEng.exe が CPU 回してくる件
事象:

- D:\bin を弾いてるのに、D:\bin\fenrir\fenrir.exe を AHK からホットキーで起動するたびに MsMpEng.exe が動いている

設定:

- `Set-MpPreference -ExclusionPath` で D:\bin を指定してる
- `ExclusionProcess` は指定してない

考えられること:

- 本件では「AHKから fenrir を起動している」
- ExclusionProcess で AHK を除外するべきではないか？

## リアルタイム保護自動オンをしているスケジュールを消す

```
schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Update" /f
schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan" /f
schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance" /f
schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cleanup" /f
schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Verification" /f
exit /b
```

すぐ実行できるようにしておくと便利。それさえ手間ならタスクスケジューラから定期的に呼び出せるようにしておく。

## リアルタイム保護を一時的に無効にする
設定から。

このウィンドウは常に開いておき、たまにチェックすると良い（面倒だが）

## Set-MpPreference でワイルドカードを使うとどうなる？
[Configure and validate exclusions based on extension, name, or location - Windows security | Microsoft Docs](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-extension-file-exclusions-microsoft-defender-antivirus#use-wildcards-in-the-file-name-and-folder-path-or-extension-exclusion-lists)

- 任意のフォルダを表現できる
- `c:\hoge\*\*fuga` みたいな多層も可能

## Set-MpPreference のフォルダ除外はサブフォルダの有効？
yes

[拡張子、名前、場所に基づく除外の構成と検証 - Windows security | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/security/threat-protection/microsoft-defender-antivirus/configure-extension-file-exclusions-microsoft-defender-antivirus#use-wildcards-in-the-file-name-and-folder-path-or-extension-exclusion-lists)

> フォルダーの除外は、そのフォルダーの下にあるすべてのファイルとフォルダーに適用されます (サブフォルダーが再解析ポイントの場合を除く)。 再解析ポイントのサブフォルダーは個別に除外する必要があります。

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
