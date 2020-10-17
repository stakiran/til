# Powershell

## プロパティ名の全取得と値の全取得
Azure AD から取得する文脈だが、

- 1: `Get-Member` でプロパティ名をゲット
- 2: foreach で obj1.xxxx の xxxx 部分を、1 で回す

```powershell
import-module AzureAD

connect-AzureAD
$user = Get-AzureADUser -SearchString "my_email_address@example.com"
$methods = $user | Get-Member -MemberType Properties 
$methods | foreach { write-host $_.Name = $user.($_.Name) }
disconnect-AzureAD
```

## Azure AD からのデータ読み出し
- ただし connect 時に毎回ログイン画面が出る

```
$ install-module AzureAD -Scope CurrentUser
```

スクリは一つ上を見て

## UTF-8 でリダイレクト出力する

```powershell
$pre = Get-MpPreference
$pre.ExclusionExtension | Out-File -Encoding UTF8 after_exclusion_extension.txt
```

こっちだと utf-16 になる

```powershell
$pre.ExclusionExtension > after_exclusion_extension.txt
```

## $profile の場所は変更できない？ → できない
デフォは `%userprofile%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1` だが変えたい。

:x: global 入れたけどだめ（env global という意味ではないか……

```powershell
Set-Variable -Name profile -Value "D:\data\dotfiles\profile.ps1" -Scope Global
```

:x: [about_Profiles - PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-6) でも変更方法書いてない

## powershell のプロンプトの変える
[PowerShellのprofile.ps1自分用設定 - Qiita](https://qiita.com/tomoko523/items/87ccaec05a433b02f67e)

```
$ powershell -Command "Test-Path $profile"
False
★ない

$ powershell -Command "New-Item -path $profile -type file -force"
★つくられる
  →%userprofile%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

$ youreditor %userprofile%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

以下を入れる。

```powershell
function prompt() {
  "(PS)$ "
}
```

## ワンライナー
powershell -Command "コマンドライン"

## コメント

```powershell
# 一行
```

```powershell
<#
 複数行
#>
```

## コマンドレットを調べる
Get-Command *EventLog*

## powershell > command > イベントログ eventlog
Get-EventLog -List

Get-EventLog application

Get-EventLog system

Get-EventLog application -Newest 3

## powershell.exe
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

## 実行権限
get

```
$ powershell -Command "Get-ExecutionPolicy -List"

        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       Undefined
```

set

```
$ powershell -Command "Set-ExecutionPolicy RemoteSigned"
```

## powershell バージョン確認
[2018年11月現在の最新バージョンはWindows 10用の5.1です](https://www.pc-koubou.jp/magazine/12142)

```
$ powershell -Command "Get-Host"

Name             : ConsoleHost
Version          : 5.1.17763.771
InstanceId       : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
UI               : System.Management.Automation.Internal.Host.InternalHostUserInt
                   erface
CurrentCulture   : ja-JP
CurrentUICulture : ja-JP
PrivateData      : Microsoft.PowerShell.ConsoleHost+ConsoleColorProxy
DebuggerEnabled  : True
IsRunspacePushed : False
Runspace         : System.Management.Automation.Runspaces.LocalRunspace
```

```
$ powershell -Command "$PSVersionTable"

Name                           Value
----                           -----
PSVersion                      5.1.17763.771
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.17763.771
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```
