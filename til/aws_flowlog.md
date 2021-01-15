# AWS Flow Log
- VPC 内でパケットキャプチャっぽいことする
- VPC, Subnet, ENI に設置する
    - [aws_flow_log | Resources | hashicorp/aws | Terraform Registry](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/flow_log)
- 保存先は S3 か cloudWatch log

see:

- [VPC フローログ - Amazon Virtual Private Cloud](https://docs.aws.amazon.com/ja_jp/vpc/latest/userguide/flow-logs.html)
