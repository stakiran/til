# AWSCLIでリージョンごとに取りたい場合
環境変数で一時的に変えてから aws コマンドを実行する。

```
set AWS_DEFAULT_REGION=ap-northeast-1
aws resource command option...

set AWS_DEFAULT_REGION=ap-southeast-1
aws resource command option...
```
