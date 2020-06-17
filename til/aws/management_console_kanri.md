# 管理コンソール マネジメントコンソール
雑多置き場になっている感ある。

## AMI マイ ami メモ
- 自分のアカウントのみで使える ami をつくれる
- インスタンスつくりたいときはインスタンス作成 > ami id で検索して **マイ AMI** にヒットするものを

## eth1 セカンダリipアドレスが見えない
参考: [Amazon EC2(Linux)のネットワーク設定でハマったときに見るメモ ｜ DevelopersIO](https://dev.classmethod.jp/cloud/ec2-linux-network-conf-tips/)

## 秘密鍵 fingerprint

```
$ openssl pkcs8 -in xxxxx.pem -nocrypt -topk8 -outform DER | openssl sha1 -c
```

## EC2インスタンスやEBSスナップショットを別アカウントに移管する
移管元で、

- ec2 > アクション > イメージ > イメージ作成
- AMI > イメージパーミッションの変更 にて Private + 移管先のアカウント番号指定で ok

移管先で、

- AMI > 自己所有をプライベートに変更する

これで見えるはず
