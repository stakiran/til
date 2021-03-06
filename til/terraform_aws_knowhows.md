# Terraform AWS Knowhows ノウハウ
いったん AWS 無関係のノウハウ全般もぶっこんでおく（●つける）

## ●
- 名前の DRY はマジで重要
    - 一箇所
- 少しでもリーダブルにする
    - count の部分で三項演算子使いがちだが、ぱっとみてわからない
    - variable でクッション置いてもいいし、locals でラップした xxxx.tf をつくってもバチ当たらない
- モジュール……
- plan test とか
- autoscaling で新旧コンテナ入れ替えるやつとか
- depends_on はどういうケースに書くべきか
- main.tf にいろんな記述を混在させない
    - variable, data, locals etc
    - それぞれ別ファイルにした方が再利用性や自動化（自動生成）や diff がしやすくなる

## ●リソースタイプ単位のメモ
ecs

- cluster
    - 普通に `aws_ecs_cluster` でつくる
- instance
    - たとえば `aws_launch_configuration` で定義
        - userdata で /etc/ecs/ecs.config に設定を書く
        - 最低限 ECS_CLUSTER にクラスター名を
    - この起動設定を使って `aws_autoscaling_group` をつくる
- service
    - `aws_ecs_service`
    - cluster argument で、このサービスを動かす cluster を指定
    - task_definition argument で、このサービスの定義を書いた task definition を指定
- task definition
    - 1 jsonでタスク定義を書いておく(渡してもらいたい部分は `${varXXX}`)
    - 2 data `template_file` で、1 からテンプレートをつくる
    - 3 `aws_ecs_task_definition` で、 2 をレンダリングする
        - container_definitions argument に data.template_file.XXXXX.rendered を指定

## ディレクトリ構造

### 1
- AWS
    - ECS による micro service
    - フロントには ALB を置いてロードバランス
- module ではなく generator を使用
- README などドキュメントはなし

```
*.tf
  (構築コード)

backend.sh 

build/
  (CI/CD用コード)

config/
  staging/
    *.tfvars
  production/
    *.tfvars

scripts/
  (resource generator……類似リソースをテンプレから一気につくる)
  (commandline generator……マシン上で実行するスクリをつくる)
  (その他開発時に役立つスクリプト群)

templates/
  *.json
  (ecs task)
  (s3 policy)
  (user data)
```

- tf
    - リソース単位で集めていいものは resourcetype.tf みたいな感じに
    - 意味的にまとめたいものはよく練った上で xxx 単位に

```
xxx_alb
xxx_ecs
cloudwatch
DB
s3
task_xxx
iam
sg
vpc
……
```


- その他の .tf
    - main.tf に書くこともできるが、ファイルに分けた方がわかりやすい
    - この場合、main.tf は provider 情報などバージョン情報だけになる

```
main.tf
variables.tf
locals.tf
data.tf
```

## CI/CD 
- 「git clone するだけで動作する」ようにする
    - たとえば Jenkins も jenkinsfile で pipeline 流せるようになっている
        - ジョブとしてはソース取ってくる設定+使うjenkinsfile設定+αで良い
- 承認フェーズ設けたいなら、plan後に input prompt を出して止める
    - jenkins だと `input message` とか
    - [Pipeline: Input Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-input-step/)

## module か generator か
module

- o 実装がキレイになる
- o 使い方を利用者に強制させることができる
- x **パスが変わったら state も変わってしまう**
- x 環境A,B,Cのうち、Cだけ～～を～～にしたい！みたいな微差に弱い
    - そして何らかの事情でそういう「例外」は割と起こる

generator

- o 微差に対処しやすい
- x **generatorを介さずに手で修正するマン** の出現
- x 「最初に雛形つくるのが楽だけ」に終始してしまいがち
- x 自前の実装が必要
    - たとえば shell script で `cat << EOS >> filename.tf` でつくるとか
- x 工夫して実装しないと generator template がハイライトされない
    - たとえば EOS 内部の tf は(.sh モードで開かれてるだろうから)ハイライトされない
  
## gitignore
- giho で

## backend s3
- ビルド時に動的に terraform.tf につくるようにする
- key に account, env などを含めることで一意のパスにする
- :rabbit:
    - なんでこうすると嬉しいのか、まだピンと来てない

イメージ:

```
terraform {
  backend "s3" {
    bucket = "..."
    key    = "status/terraform/${ACCOUNT}/${ENV}.tfstate"
    region = "..."
  }
}
```

## tf ファイルのつくりかた
- 1ファイルに集約した方が良いもの
    - 各種インスタンスやタスクを載せるために必要な土台部分とか
        - vpc, subnets, route, eip, sg
    - 順序関係なく独立して定義しておける、他のリソースから参照されるリソースとか
        - s3 bucket
        - secret系
        - cloudwatch
- テンプレート化しておくもの
    - task definition
    - iam policy
    - userdata script

## data による注入
- 特定の環境に注入する場合、data で注入先情報をゲットする

## Tag、特に Name
- リソースにはできるだけタグをつけておく
    - 特に Name タグ
    - なんだかんだマネコンから探して確認する機会は多い
    - 直感的にフィルターできる名前体系を考えておく
    - `tags = {...}` をコピペではなく共通的につくるにはどうしたらいいんだろう
        - custom function はないし
        - [terraform.md](terraform.md) 見て
