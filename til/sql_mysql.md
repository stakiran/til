# SQL MySQL

## デフォルトのパスワード
root/なし

変更するには

```
SET PASSWORD FOR root@localhost=PASSWORD('password');
```

## ログイン
mysql -u ユーザ名 -pパスワード データベース

```
-h ホスト
--port ポート番号
```

## my.cnfについて
優先順序

- 1 ~/.my.cnf
- 2 /etc/my.cnf
- 3 /etc/mysql/my.cnf

from http://sawara.me/mysql/2073/

見当たらない場合は自分で作る from http://d.hatena.ne.jp/tyamaguc07/20110406/p1

## データベース

```
show databases;
use データベース名
drop database データベース名;
```

## 文字コード関連
データベース単位

```
mysql> alter database wikidb character set utf8;
Query OK, 1 row affected (0.00 sec)

mysql> show create database wikidb;
+----------+-----------------------------------------------------------------+
| Database | Create Database                                                 |
+----------+-----------------------------------------------------------------+
| wikidb   | CREATE DATABASE `wikidb` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+----------+-----------------------------------------------------------------+
1 row in set (0.00 sec)
```

デフォルト設定

```
mysql> show variables like 'character_set%'
    -> ;
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | latin1                     |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
```

変更するには

```
$ sudo cp /usr/share/mysql/my-default.cnf /etc/my.conf
$ sudo vim /etc/my.conf
[mysqld]
character-set-server=utf8

[client]
default-character-set=utf8
$ sudo systemctl restart mysqld.service
```

## テーブル

```
show tables;
show columns from テーブル名
```

## ユーザ・パスワード
ユーザ一覧確認

```
rootでログインして
select Host, User, Password from mysql.user;
```

## ユーザ削除

```
delete from mysql.user where user="*削除するユーザ名";
```

## パスワード変更

```
set password for username=password('パスワード');
```

ただしrootの場合はホスト名も要る。

```
set password for root@localhost=password('パスワード');
```

## 権限確認

```
show grants for ユーザ名
※ユーザ名の書式は 'username'@'hostname'
  →例: 'root'@'localhost'
```

基本書式

```
GRANT 権限 ON レベル TO 割当先ユーザ;
```

レベル

```
グローバルレベル:
	GRANT 権限 ON *.* TO user;
データベースレベル:
	GRANT 権限 ON db_name.* TO user;
テーブルレベル:
	GRANT 権限 ON db_name.table_name TO user;
カラムレベル:
	GRANT 権限 (カラム1, カラム2, ...) ON db_name.table_name TO user;
```

- http://sasuke.main.jp/useri.html
- http://www.dbonline.jp/mysql/user/index6.html
