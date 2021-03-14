# Terraform AWS provider

## RDS cluster instance の updated in-replace 変更を即時反映するには？
- `apply_immediately = "true"` が必要
    - これがないと「次のメンテナンスウィンドウに更新するよ」になる（即時じゃない）
- また DB インスタンスは起動しっぱなしにしておく
    - 停止していると逆に 400 エラーで失敗する

## apply 先のリージョンはどこで指定する？
Ans: provider

> region - (Optional) This is the AWS region. It must be provided, but it can also be sourced from the AWS_DEFAULT_REGION environment variables, or via a shared credentials file if profile is specified.

指定必須とある

- Q: え？us-east-1にログインした状態でも、別リージョンにリソースつくれるってこと？
    - Ans: yes
    - というか「どのリージョンにログインしているか」は関係ないです
    - たとえばローカルで terraform 叩くこともあるでしょ
    - 当たり前
    - ~~よくわからん悩み方してるな~~

see: [Docs overview | hashicorp/aws | Terraform Registry](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

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
