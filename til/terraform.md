# Terraform

## lookup?
https://www.terraform.io/docs/configuration/functions/lookup.html

> lookup(map, key, default)

> For historical reasons, the default parameter is actually optional. However, omitting default is deprecated since v0.7 because that would then be equivalent to the native index syntax, map[key].

v0.7+ では省略禁止なので、実コードでは必ず default も都度指定してる感じになる。

## ユーザー定義関数 custom function
- サポートしてない
- 別の手段で頑張る
- src
    - [Functions - Configuration Language - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/functions.html)
        - > The Terraform language does not support user-defined functions, and so only the functions built in to the language are available for use
    - [Add the ability to create custom interpolate functions via a plugin. · Issue #15603 · hashicorp/terraform](https://github.com/hashicorp/terraform/issues/15603)
        - サポートする気はないです
        - 利用者が意識せねばならない互換性が増えちゃうから……
        - やりたければ custom data source か external data source で頑張って

[Terraform で（無理やり！）独自の関数を定義する - Qiita](https://qiita.com/tmshn/items/64789684a6057131b8b6)

- 1: たとえば .py ファイルつくって、data "external" から ` program = ["python", "func.py"]` みたいに
- 2: module で実現する
    - resource をつくらない module
- どっちも強引だが、そうしないとダメかー……

## tfstate をバージョン管理するのはアリ？
Ans. 基本的にはなし

- 以前は小規模ならアリだった
- が、tfstate には機密情報が入ることがある
- 今は local or remote の二択が主流
- が、一人利用ならバージョン管理するのも良いだろう
    - 一人で使ってる private repo とか

see: [devops — .tfstateファイルをGitにコミットする必要がありますか？](https://www.it-swarm-ja.tech/ja/devops/tfstate%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92git%E3%81%AB%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88%E3%81%99%E3%82%8B%E5%BF%85%E8%A6%81%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%81%8B%EF%BC%9F/827326767/)

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
