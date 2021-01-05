# GitHub

## 新しいアカウントつくって SSH 認証する on Windows
`C:\Program Files\Git\etc\ssh\ssh_config` に設定を書く

- ポートは 22 SSH が使えるならそれを
- ダメなら 443 HTTPS で
- 所属組織次第

```
Host github.com
 User git
 Hostname ssh.github.com
 Port 443
 IdentityFile (秘密鍵ファイルのWindowsフルパス)
 ProxyCommand connect.exe -H (PROXYのIP):(同左PORT) %h %p
```

たしかめる

```
$ where ssh
C:\Windows\System32\OpenSSH\ssh.exe
C:\Program Files\Git\usr\bin\ssh.exe ★git時はこっちが使われるので注意

$ "C:\Program Files\Git\usr\bin\ssh.exe" -T git@github.com
……
hi (あなたの名前)! You've successfully authenticated, ...
```

GitHub で確認

```
$ git clone git@github.com:(あなたのGitHubユーザー名)/(リポジトリ名).git

$ git config --local user.email "(ID)+(USERNAME)@users.noreply.github.com" & git config --local user.name "(あなたの表示名)"
★事前に https://github.com/settings/emails から private e-mail をコピーする

$ (pushまで成功したらok)
```

## wincred on Windows で HTTPS 認証を再登録する
探して消す。

```
$ cmdkey /list
……
    ターゲット: LegacyGeneric:target=git:https://github.com
    種類: 汎用
    ユーザー: stakiran
    ローカル コンピューターの常設
……

$ cmdkey /delete:git:https://github.com
```

消えたので、もう一度登録する。

```
$ (push とかすると)
Username for 'https://github.com': stakiran
Password for 'https://stakiran@github.com': (パスワードまたは Personal Access Token を入れる)

$ cmdkey /list
……
    ターゲット: LegacyGeneric:target=git:https://stakiran@github.com
    種類: 汎用
    ユーザー: stakiran
    ローカル コンピューターの常設
……
```

## Personal Token で clone できるようにするまで
- 1: トークンつくる
    - https://github.com/settings/tokens
    - repo 配下だけ全部チェックオン
- 2: clone する
    - ちょっと紛らわしいが、github.com の後は普通のパス

```
git clone https://MYUSERNAME:TOKEN@github.com/USERNAME/REPONAME
```

:warning: .git/clone にトークンがベタ書きされるので注意

## Q: https://github.com/settings/keys や https://github.com/settings/tokens で Last used の日時が正しくなさそうだが？
Ans: 正しいです

数秒前に使ったばかりでも Last used within the last week と出る。

## SSH で clone できるようにするまで
1: 秘密鍵と公開鍵つくる

```
$ cd ~/.ssh

$ ssh-keygen -t rsa
(プロンプトに従って鍵のファイル名を適当に設定)

```

2: 公開鍵(.pub)をコピーして、GitHub に登録

- https://github.com/settings/keys
- New SSH key より
- どの PC から使うものか、ちゃんとタイトルはつけた方がいい

3: どの URL に対してどの鍵を使うか、という ssh の設定を書く

~/.ssh/config

```
Host github.com
 User git
 port 22
 Hostname github.com
 IdentityFile ~/.ssh/(使う秘密鍵のファイル名)
 TCPKeepAlive yes
 IdentitiesOnly yes
```
