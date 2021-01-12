# Terraform

## lifecycle is 何？
- [Terraformでテンプレートのアップデート時に特定のリソースの変更を適用しない方法 | Developers.IO](https://dev.classmethod.jp/articles/terraform_ignore_changes/)
- [The lifecycle Meta-Argument - Configuration Language - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/meta-arguments/lifecycle.html)

ソース変更時のリソース変更挙動を指定できる

- 毎回消す
- 削除を防ぐ
- 無視する
    - >実際のリソースとTerraform管理下のリソースの差分があった際、指定したリソースの変更が無視される様になります。
    - list of string

### ignore_changes の例

```tf
resource "aws_instance" "inst1" {
  ……
  security_groups = ["aws_security_group.sg1.id", "aws_security_group.sg2.id"]
  ……

  lifecycle {
    ignore_changes = ["security_groups"]
  }
}
```

## tf plan -var-file は複数並べられる

## リソース一覧が見たい、など tf に定義されたのを列挙したい場合
- 以下コマンドなどで
    - state list
    - state show
    - output
- ただし state ファイルから読み込むので、事前に state をつくっておく(planする)必要がある
    - ★backend 使ってるときの state の挙動がわからねぇ……
        - 1: tf plan したら remote state がもう書き換わっちゃう？
        - 2: remote は書き換わらずに、ローカルでつくられる？ and （適用するなら）それを push する必要あり？
        - 3: 1と2が両方起きる？
            - つまり backend 使う場合は local tfstate を gitignore するなどの対応が実質推奨
        - :rabbit: たぶん 3

graph コマンドだけは例外で、ローカル完結できる。

## s3 でバックエンド
```tf
terraform {
  backend "s3" {
    bucket = "mybucket"
    key    = "path/to/my/key"
    region = "us-east-1"
  }
}
```

- backend "s3" の場合、三行だけでいける
    - バケット名、保存先、リージョン
    - 保存先は .tfstate ファイルにする
- required
    - aws provider
    - いくつかの IAM
- recommended
    - s3 側でバージョン管理有効にする

参考:

- [Terraformのbackend機能を利用してstateファイルを共有する](https://blog.mosuke.tech/entry/2018/06/17/terraform-backend/)
- [Backend Type: s3 - Terraform by HashiCorp](https://www.terraform.io/docs/backends/types/s3.html)

## terraform init でプロキシ通らん

```
set HTTP_PROXY=http://IP:PORT
set HTTPS_PROXY=http://IP:PORT
```

- HTTPS_PROXY の方が使われる
- http のケースと同じ url を使う

[Use a proxy with Terraform - Server Fault](https://serverfault.com/questions/931493/use-a-proxy-with-terraform)
