# Azure DevOps

## SSHベース
- 1: 手元で鍵つくる
- 2: プロジェクト画面側で public key を登録

必要なら ssh config も

例: `C:\Program Files\Git\etc\ssh\ssh_config`

```
Host ssh.dev.azure.com
 User git
 Port 443
 IdentityFile D:\data\sensitive\211201_azure_projectABC
 IdentitiesOnly yes
 ProxyCommand connect.exe -H (HOST):(PORT) %h %p
```

## Httpsベース
project（リポジトリ）ごとにpasswordを発行できる。

### OSに保存させるgitconfig
Windowsの場合は資格情報が使われる。linuxは知らない。

```
[credential "https://(YOUR-ORGANIZATION)@dev.azure.com/"]
	helper = store
	UseHttpPath = true
```

### git config 初期 for VM, CloudShell
必須のやつ

```
$ git config --global user.name ★
$ git config --global user.email ★
```

認証情報は、global と system の両方にあるので、両方上書きしないとデフォのやつが出てくる（windowsだと認証画面出してくるアレ）。linux はどうなってるか知らん。

```
$ git config --global credential.helper ★
$ git config --system credential.helper ★
```
