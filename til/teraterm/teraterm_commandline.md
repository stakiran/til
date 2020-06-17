# Teraterm コマンドライン
- General: https://ttssh2.osdn.jp/manual/4/ja/commandline/teraterm.html
- SSH: https://ttssh2.osdn.jp/manual/4/ja/commandline/ttssh.html
- Proxy: https://ttssh2.osdn.jp/manual/4/ja/commandline/ttproxy.html
- Macro: https://ttssh2.osdn.jp/manual/4/ja/macro/

## ひととおり試した
以下を想定

- 社内など HTTP プロキシが通っている
- AWS
    - まずは Bastion(踏み台) でポートフォーワードした後、プライベートサブネット内の Main Server(作業サーバー)に繋ぐというシナリオ

### 1 config

```
@echo off

rem [teraterm program]
set TERATERM_FULLPATH=D:\bin\teraterm\ttermpro.exe

rem [Proxies]
set PROXY_SERVER=myproxyserver.com
set PROXY_PORT=80
set PROXY_ADDRESS=%PROXY_SERVER%:%PROXY_PORT%

rem [Auth]
set USERNAME=ec2-user
set PRIVATEKEY_PEMFILE_FULLPATH=D:\data\crt\aws_xxxxx_dev.pem

rem [IP and Ports]
set IP_BASTION=xx.xx.xx.xx
set IP_MAINSERVER=xx.xx.xx.xx
set PORT_BASTION=22
set PORT_MAINSERVER=22

rem [Forwaring]
set YOUR_LOCALPORT_FOR_MAINSERVER=11111
set BASTION_FORWARD1_MAINSERVER=%YOUR_LOCALPORT_FOR_MAINSERVER%:%IP_MAINSERVER%:%PORT_MAINSERVER%set BASTION_FORWARDS=%BASTION_FORWARD1_MAINSERVER%
```

### 2 プロキシとポートフォーワード
- 紛らわしいが ssh 関連設定は /ssh、プロキシ関連設定は -proxy で指定する

```
@echo off

call %~dp00_configure.bat

set commandline="%TERATERM_FULLPATH%" %IP_BASTION%:%PORT_BASTION% /ssh /auth=publickey /keyfile="%PRIVATEKEY_PEMFILE_FULLPATH%" /user=%USERNAME% /ssh-L%BASTION_FORWARDS% -proxy=http://%PROXY_ADDRESS%

echo [Commandline]
echo %commandline%
start "" %commandline%
```

### 3 ポートフォーワードを使ってログイン
- :warning: プロキシは外す必要がある(ことが多い)

```
@echo off

call %~dp00_configure.bat

set commandline="%TERATERM_FULLPATH%" localhost:%YOUR_LOCALPORT_FOR_MAINSERVER% /ssh /auth=publickey /keyfile="%PRIVATEKEY_PEMFILE_FULLPATH%" /user=%USERNAME%

echo [Commandline]
echo %commandline%
start "" %commandline%
```
