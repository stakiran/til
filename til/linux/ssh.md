# ssh

## ●ssh-keygen
passphrase 無し、確認も略してつくる。

ssh-keygen -t rsa -f ./keypair-user1 -q -N ""

## ssh キーペア 鍵 ログイン
ssh user1@192.168.1.1 -i ../keypair-user1

## ssh 基本的なコマンドライン
ssh -p 22 -l ec2-user -i ~/.ssh/id_rsa 192.168.1.1
## ssh 指定ユーザーでの公開鍵ログインをするまで
ログインに対応したいサーバーにログインして

ユーザーつくる。ここでは user1

```
sudo useradd user1
sudo passwd user1
(パスワードは評価環境なら user1 などテキトーで良い)
```

つくった user1 で su して、.ssh 配下に公開鍵を登録する。

パーミッション含めて厳密な指定が必要。700 は「所有者のみフルコン」、600は「所有者のみ読み書き可」。

```
su user1
mkdir .ssh
chmod 700 .ssh
touch .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
vi .ssh/authorized_keys
(.pub の内容を貼り付ける)
```

