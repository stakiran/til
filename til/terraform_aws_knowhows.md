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

## ●CI/CD は「git clone するだけで動作する」ようにする
- たとえば Jenkins も jenkinsfile で pipeline 流せるようになっている
    - ジョブとしてはソース取ってくる設定+αで良い

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
- key に account, region, env などを含めておくと一意のパスになる

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
