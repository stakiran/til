# AWSアカウントIDを取得するコマンド
- バッチなので一行に加工できないけど……
- 現在のプロファイルが見に行ってる AWS アカウントを取ってくる

```
@echo off
setlocal

echo https://
aws sts get-caller-identity | jq ".Account" | tr -d "\""
echo .signin.aws.amazon.com/console
```
