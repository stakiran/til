# SELinux

## getenforce

```
現状態を出力
Enforcing   SELinux機能は有効でアクセス制御も有効。
permissive  SElinuxはwarningを出すが、アクセス制限は行われません
disabled    SElinux機能・アクセス制御ともに無効
```

## setenforce
SELinuxの状態を一時的に変更する

```
setenforce 0   #SELinuxを一時的に無効化(permissiveになる)
setenforce 1   #SELinuxを復活
```

## SELinuxを完全に無効化する
- vi /etc/sysconfig/selinux
- `SELINUX=enforcing` to `SELINUX=disabled`
- 再起動
