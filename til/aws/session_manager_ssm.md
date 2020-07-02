# AWS Session Manager bastion 踏み台レス
- SSM を使うと踏み台レスでインスタンス（Private subnet 下のものも）にアクセスできる
- 踏み台(EIP)要らない

## やること
- 各自の PC に aws ssm コマンドインストール
    - python, pip, awscli 必要
- 接続先インスタンスのすべてに「AmazonSSMManagedInstanceCore ポリシーをアタッチしたロール」を付与
    - **起動しているインスタンスに付与した場合、いったん再起動しないと反映されない**

## 接続方法
tp linux 

```
$ aws ssm start-session --target (インスタンスID)
```

to windows

```
$ aws ssm start-session --target (インスタンスID) --document-name AWS-StartPortForwardingSession --parameters "portNumber=3389,localPortNumber=12345"

$ (mstsc で localhost:12345 に繋ぐ)
```
