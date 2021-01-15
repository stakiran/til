# Terraform AWS provider

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
