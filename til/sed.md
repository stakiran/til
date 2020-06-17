# sed

## SELinux disabled サンプル

```
$ sed -e 's/SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux
これで /etc/sysconfig/selinux をいじった結果を stdout

$ sed -i -e 's/SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config
`-i` で直接編集できる。
```
