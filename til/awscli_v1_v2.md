# AWSCLI v1 v2

## aws==0.2.5 を消す
久々に AWS 使って、boto3 botocore awscli あたり upgrade したら、awsコマンドが使えなくなった。

古い aws コマンドを消して解決。

```
$ where aws
D:\bin1\python374\Scripts\aws.cmd
D:\bin1\python374\Scripts\aws.exe ★こっちが aws==0.2.5 の古いやつだったみたい

pip uninstall aws
```
