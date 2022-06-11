# AWS CLI aws configure と環境変数

## プロファイルの切り替えは AWS_PROFILE 環境変数
あるいは aws コマンドで都度 `--profile xxx` 指定するか

## aws configure に profile をつくる
セクションの書き方が違う

- config では `[profile MYPROF]` のように書く
- credentials では `[MYPROF]` のように書く(`profile `が要らない)

まあ `aws configure --profile MYPROF` などでつくるのが確実か

## aws configure と environment variable 環境変数の違い
[Environment Variables To Configure the AWS CLI - AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

- 環境変数 AWS_CA_BUNDLE に設定して、その場で有効な設定をつかう
- aws configure `ca_bundle` をセットして、恒久的に設定する

```
set AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxxxxxx
set AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
set AWS_DEFAULT_REGION=ap-northeast-1
set AWS_DEFAULT_OUTPUT=json
set AWS_CA_BUNDLE=....
```

## For Linux
- ~/.aws
- /root/.aws

デフォユーザーと root ユーザーとで混在しやすい(root ではつくってるがデフォでは作ってないのでデフォからは設定がないように見えるとか)ので注意。

## For windows
%userprofile%\.aws\config

```ini
[default]
region = ap-northeast-1
output = json
ca_bundle = D:/data/crt/xxxx.pem
```

%userprofile%\.aws\credentials

```
[default]
aws_access_key_id = ...
aws_secret_access_key = ...
```
