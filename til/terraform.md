# Terraform

## data リソース参照時は data. をつけろ（でないと  Reference to undeclared resource）

## taint
- 汚染フラグ
- これをつけたリソースは、内部的に再作成される
    - plan 時に is tainted, so must be replaced と表示される
    - apply 時は再作成が走る

## local で plan したい場合のノウハウ
- 1: 既に使われているビルドファイル等から、tf plan のコマンドラインを入手
- 2: かんたんなコマンドで実行できるラッパーをつくる
    - windows なら .bat つくって、path 通ってる場所に置くとか
- 3: tf plan > stdout.stdout のように、ファイルに出す
- 4: この stdout ファイルを VSCode で開く

VSCode を使うメリット

- 自動リロードされる
- タブの一つとして扱えるので扱いやすい
- [ANSI Colors - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=iliazeus.vscode-ansi) を使えば、ANSI の色付けもできる

## tfplan と tfstate
tfplan

- バイナリファイル
    - なので人間には読めない
- terraform apply 時に食わせることで、（そのtfplanに書かれた内容に従った）applyができる
    - なので plan で tfplan 吐いて、吐いたそれをそのまま apply で食わせるのが一般的

tfstate

- stateファイル
- apply後に作成される
- 作成先 ★ここちょっと自信ない……
    - カレントディレクトリ
    - if backend 指定時 then そっちにもつくる

## for_each で each.value is object with 1 attribute "xxx" が出る
for_each が指している変数側で、漏れなく value を定義する。

例: attr2 を新たに追加したい場合

```
locals {
  map1 {
    "element1" = {
      "attr1" = "value1"
      "attr2" = 2 // ★呼び出し元でこれ使ってるコードを書いた場合
    }
    "element2" = {
      "attr1" = "value11"
      // ★ここ含め他のすべての要素にも attr2 を定義しなきゃいけない
      //   してないと上記エラーが出る(xxxしか見つからないがな、と)
    }
    "element3" = {
      "attr1" = "value1111"
    }
  }
```

## for_each
- これは variable の default argument 使って直接値を定義してる例
- each.key または each.value["VALUEKEYNAME"] で参照

```tf
variable map1 {
  default = {
    key1 = {
      valuekey1 = "value1"
      valuekey2 = "value2"
    }
  }
}

resource xxx yyy{
  for_each = var.map1

  argument1 = each.value["valuekey1"]
}
```

リソース名はどうなるか

- resourcetype.resourcename["key1"]

## 0.14 fmt で "${xxx}" to xxx がされるケースとされないケース
されないケースの例:

- ブロックの中
    - 例: aws provider の data template_file の argument `vars = {...}` など
- xxx に変数参照と普通の文字列が混在しているとき
    - 例: `"${var.prefix}-hogehoge-${var-suffix}"`

## 0.11 to 0.12
基本は以下

- 0.11 で tf 0.12checklist
- remove .terraform/ dir
- 0.12 で tf init
- tf 0.12upgrade
    - ここで fmt みたいにコード修正が走る

その他のテクニック

- data.template_file 部分で差分が出る
    - templatefiles() 関数を使う
- splat について
    - `aws_subnet.xxxx.*.id` こういうやつ
    - これ単体で list になるので、`[]` で囲む必要はない
    - 複数の splat を並べる場合、flatten() が必要
        - `flatten([splat1, splat2, ....])`

## terraform init で 403 forbidden
- .terraform フォルダをいったん削除してからリトライするとたぶん ok
- plugins/ が（途中で失敗する、手作業でバイナリ置いたなど）中途半端な状態だと、init がうまく動作してくれない

## provider のバージョン周り
- ドキュメンテーション
    - https://registry.terraform.io/providers/hashicorp/aws/2.55.0
    - コンボボックスからバージョン選べるようになってる
- バイナリ
    - https://releases.hashicorp.com/terraform-provider-aws/2.55.0/

## version の ~> 2.68.0 is 何
ok

- 2.68.0
- 2.68.1
- ...

NG

- 2.69.x

肝

- rightmost の部分のみ `>=` になる
- `>` ではない

余談

- Hashicorpは、古いバージョンは x.y.0 のみ置く
    - ある -> https://releases.hashicorp.com/terraform-provider-aws/2.55.0/
    - ない -> https://releases.hashicorp.com/terraform-provider-aws/2.55.1/
- これは `~> 2.55.0` でも init でインストールできる
- このことから、`>=` だと言える
- そもそも一般論から考えて「以上」の方が使いやすい

## terraform graph
```
$ terraform graph | dot -Tsvg > graph.svg
```

- Graphviz の dot.exe の PATH 通しておく必要あり

## terraform import is 何
- `terraform import (path_to_resource) (path_to_realworld_resource)`
- 既存リソースを、path to resource で指定した名前で、tfstate に追加する
- tfstate に書くだけで、tfファイルは更新されない（ので手動で記述する必要がある）
    - plan を繰り返して「うん、差分なくなったね」までたどり着くゲー

わからん:

- realworldの方の文法
    - terraform path だったり、AWS 側の resource id だったり、IAMリソース系は arn だったり、route53では zoneid だったりするんだけど

## Missing resource instance key エラー
何を言っている？

- argument に指定している data.xxxx が count で定義されている
- このままだと、xxxx 側の count の値によって xxxx があったりなかったりする
- argument 側が一意に定まらない
- 定まるようにしなさい

どうすれば

- エラーメッセージに書いてあるけど、`data.xxxx[count.index]` みたいにする
- つまり xxxx 側の count の値を反映した形の参照をうまく指定してやる

## 条件に応じてリソースを作成する・しない ifdef みたいなやつ
- count meta-argument を使う
    - count=0 のときはリソースが作成されない
- 条件分岐は三項演算子で書ける

```tf
resource "type" "name" {
    count = var.region == "ap-northeast-1" ? 1 : 0
    ...
}
```

locals を使えばもうちょっとリーダブルにできる

```
locals {
  use_only_in_tokyo = var.region == "ap-northeast-1" ? 1 : 0
}

resource "type" "name" {
    count = local.use_only_in_tokyo
    ...
}
```

## local と input variable の違い
Ans: 上書きできるかどうか

- input は -var-file など他手段で上書きできる
    - 未指定時に tf plan/apply すると enter a value が出るとか
- local はできない

使い分けは？

- > 意図しない値の設定を防ぐためにもtfファイル上で変数を扱う際はまずLocal Valuesを利用し、外部から値の入力が必要な場合のみvariableを利用するのがオススメ
- [【モダンTerraform】VariableとLocal Valuesの使い分けについて - febc技術メモ](https://febc-yamamoto.hatenablog.jp/entry/2018/01/30/185416)

勘違いしたところ

- local というと「ファイル中でしか有効にならない」「main.tf に local variable 定義したら、他のファイルからは locals.xxx で見れない？」というイメージ
- 違います
- あえていうなら **外部から上書きできない input variable** みたいなもん

## -target オプション
```
$ tf plan -var-file=path/to/xxxx.tfbvars -target=resoucetype.resourcename
```

- 指定したリソースに対して plan を実施できる
- 指定したリソースから参照されているリソースがあれば、その定義も走査される
- `-target` は複数指定も可能

使いどころ

- plan 全体だと error warning が多いが、target なら絞って確認しやすい
- 常用はしないこと
    - 小さな構成に分割して、各々で tf plan できるようにするべき

## 0.12 にしてから warning 多すぎるのだがなんとかならないか？
- (n warnings) ← これの短縮表示しかありません
- ただし 0.14 だと fmt である程度自動修正できます

====

- tf plan の option としては見当たらない。
- [Any way to disable new deprecation warnings? - Terraform - HashiCorp Discuss](https://discuss.hashicorp.com/t/any-way-to-disable-new-deprecation-warnings/3999)
    - 「ver 0.12 になってから warning 増えすぎて鬱陶しいんだが」的なこと言うてる
- [Consolidate repetitive warning messages by apparentlymart · Pull Request #23425 · hashicorp/terraform](https://github.com/hashicorp/terraform/pull/23425)
    - 「暫定処置として、たとえば 200 個のメッセージが出たら 1 個出す + 198warnings、みたいな表示で対応します」と言ってる
    - merge されてる
    - v 0.12.29 では既にある
- [Flag or env var for quieting syntax deprecation warnings · Issue #23406 · hashicorp/terraform](https://github.com/hashicorp/terraform/issues/23406)
    - ちょっと楽できる個人ツール（terraform公式ではない）つくった
        - https://github.com/apparentlymart/terraform-clean-syntax
        - `"${aaa}"` を `aaa` にする ← こういう修正を自動でやってくれる
        - でも 0.14 で terraform fmt に組み込まれた

### tf14 fmt で ok
軽く確認した限り、以下を是正してくれる。

- 0.11 時代の古い表記
    - `${aaa}` → `aaa`
- そもそも行儀悪い書き方
    - `type = map` → `type = map(any)`

### X terraform-clean-syntax 使ってみる
$ go get github.com/apparentlymart/terraform-clean-syntax

cannot find package がでて、もう古い感じ。

素直に 0.14 の fmt 使うしかなさそう。0.14 fmt で warning 消した後、0.12 を使うみたいな。

alauncher

```ini
[terraform]
rawbin=%bin1%\terraform\0.12.29\terraform.exe %*
alias=tf
prm=%*

[terraform_v11]
rawbin=%bin1%\terraform\0.11.14\terraform.exe %*
prm=%*
alias=tf11

[terraform_v12]
rawbin=%bin1%\terraform\0.12.29\terraform.exe %*
prm=%*
alias=tf12

[terraform_v14]
rawbin=%bin1%\terraform\0.14.5\terraform.exe %*
prm=%*
alias=tf14
```

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
- ただし state ファイルから読み込むので、事前に state をつくっておく(applyする)必要がある

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
