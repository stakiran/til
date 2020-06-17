# yum

## アンインストール
yum remove unzip

## インストール済みパッケージの検索
`yum list installed | grep unzip`

## yum プロキシ

```
$ cat /etc/yum.conf
proxy=http://(myproxy):(port)
```
