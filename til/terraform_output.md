# Terraform output

## 反映
- 一度 apply して state に反映させる必要がある
- その後、`terraform output` で取れる

```
$ terraform output
main_vpc_id = "vpc-XXXXXXXXXXXXXXXXX"
main_vpc_tags = tomap({
  "Name" = "xyzenv-main-vpc"
})
```

## 書き方

```
output "main_vpc_id" {
  description = "ID of the main VPC"
  value       = aws_vpc.main.id
}
```

## 参照可能な属性の探し方
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc#attributes-reference
- attributes reference を見る
    - vpc の場合、id とか arn とか tags_all とかがある
