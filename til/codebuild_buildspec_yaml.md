# AWS CodeBuild とか buildspec.yaml とか
- 詳しいし例もある
    - [CodeBuild のビルド仕様に関するリファレンス - AWS CodeBuild](https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-example)

## ビルドログは logs を指定しないと見れない
- cloudwatch logs の設定が必要
    - マネコンで loggroup name と stream name 入れれば自動でつくってくれる
- これつくらないとビルドログ自体が見れない

## 環境変数は project, spec どっちもいけるが、project が優先される
- buildproject 側で設定できる
- buildspec 側でも設定できる

```yaml
# buildspec 側で設定する例（カスタム環境変数）
env:
  variables:
    VAR1: value1
    VAR2: value2
```

両方設定した場合、buildproject 側が優先される。

## 環境を見たいとき
- 調べるコマンド打って、ビルド開始してから見てみる
- Amazon Linux なので EC2 やコンテナ立てて調べてもいいが、CodeBuild 独自の設定もあると思うので、まあ実際に見てみるのが確実

```
phases:
  install:
    commands:
      - echo ==== OS version
      - cat /etc/os-release
      - uname -a
      - echo ==== Directory
      - pwd
      - ls -l
      - echo ==== Envvars
      - export
      - echo ==== Tools
      - aws --version
      - python --version
```

## terraform apply する例
- codepipeline から使う前提（ソースがcodepipeline）
- terraform のインストール方法は色々ある
    - 公式では https://www.terraform.io/downloads yum を使っている
        - 動かんけど（yum repo側が死んでる？）
    - ここでは zip を展開して bin/ にコピるという荒業でカバー
        - OS にあったバイナリが必要（amazon linux2 の場合は ARM64）
    - あとは事前に terraform 入りの docker image つくって ECR に push しといて、build project 側でそのイメージを使うようにする案もある
- terraform に必要な IAM 権限
    - ここでは administratorsaccess レベルの access/secret を secrets manager シークレットに保存し、それを取得している
    - 他にも IAM ロール付与で済む方法があるらしい？

```
version: 0.2

env:
  secrets-manager:
    # secret name    : /CodeBuild/manage/terraform/awscredentials
    # secret key name: AWS_ACCESS_KEY_ID
    # varname        : AWS_ACCESS_KEY_ID
    # 
    # (varname) : (secretname):(secretkeyname)
    # buildpec 内からは varname でアクセスする。
    # 別の言い方をすると、varname という名前の環境変数が設定される。
    # なので、AWS_XXXX 系の環境変数を設定したければ、この varname の時点でやる。
    #
    AWS_ACCESS_KEY_ID: /CodeBuild/manage/terraform/awscredentials:AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY: /CodeBuild/manage/terraform/awscredentials:AWS_SECRET_ACCESS_KEY
  variables:
    VAR1: value1
    VAR2: value2

phases:
  install:
    commands:
      - yum -y install wget unzip
      - wget https://releases.hashicorp.com/terraform/1.2.4/terraform_1.2.4_linux_arm64.zip
      - unzip ./terraform_1.2.4_linux_arm64.zip -d /usr/local/bin/
      - terraform --version
  pre_build:
    commands:
      - cd work/terraform/tutorial1
      - terraform init
  build:
    commands:
      - terraform apply -auto-approve
  post_build:
    commands:
      - terraform output
```
