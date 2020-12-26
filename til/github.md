# GitHub

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
