# Terraform AWS provider

## ●AWSノウハウ
一部一般ノウハウもあるがいったんここに

### リソース固有
- lifecycle で ignore_changes するケースとか
- ...

### 共通や初期
- gitignore
    - giho で
- backend s3
    - ビルド時に動的に terraform.tf につくるようにする
    - key に account, region, env などを含めておくと一意のパスになる
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
- 特定の環境に注入する場合、main.tf にて data で注入先情報をゲットする
- AWS リソースにはできるだけタグをつけておく
    - 特に Name タグ
    - なんだかんだマネコンから探して確認する機会は多い
    - 直感的にフィルターできる名前体系を考えておく
    - `tags = {...}` をコピペではなく共通的につくるにはどうしたらいいんだろう
        - custom function はないし
        - [terraform.md](terraform.md) 見て
- 説明コメントは書かない
    - 英語文章に全部日本語訳を書く、みたいなことはしない
    - 同様に tf コードにもいちいち説明コメントは書かない
    - tf コードをスラスラ読めるようになれ
    - (?) 設定根拠どう書けばいいんだろ

## aws_alb と aws_lb の違いは？
- aws_alb は aws_lb のエイリアス

```go
			// Adding the Aliases for the ALB -> LB Rename
			"aws_lb":               dataSourceAwsLb(),
			"aws_alb":              dataSourceAwsLb(),
			"aws_lb_listener":      dataSourceAwsLbListener(),
			"aws_alb_listener":     dataSourceAwsLbListener(),
			"aws_lb_target_group":  dataSourceAwsLbTargetGroup(),
			"aws_alb_target_group": dataSourceAwsLbTargetGroup(),
```

from: https://github.com/hashicorp/terraform-provider-aws/blob/8800edbdf92e756e2cc18f66b87b18cf4db1499e/aws/provider.go#L396
