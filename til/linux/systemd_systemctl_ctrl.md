# systemctl
status, start, stop と is-enabled, enable, disable。後者は起動時の自動起動。

## 起動中のサービス一覧
systemctl list-units --type=service

## 確認

```
systemctl status yum-cron
systemctl is-enabled yum-cron
```

## 操作

```
systemctl start yum-cron
systemctl stop yum-cron

systemctl enable yum-cron
systemctl disable yum-cron

```
