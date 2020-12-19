# GitHub

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

## Q: https://github.com/settings/keys の Last used が last week で正しくなさそうだが？
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
