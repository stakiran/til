# Packer

## 基礎
AWS の場合

- hashicorp製品
- AMI をつくる
- json 書いてビルドする感じ
- 何が新しい?
    - AMIは手作業でつくってた
    - IaCじゃない
    - IaCにできる
- 内部では AWS CLI 使ってます
- インスタンスログイン後の処理は provisioner で可能
    - shell とか ansible とか使える
    - `[{command block}, {command block} ...` ← このイメージ
- 主にゴールデンイメージ用？
    - 構築済イメージつくっといて、ここからインスタンスを立ち上げる
    - インスタンスに都度設定適用していくのではなくて

Q: ベースとなるamiってこまめに変わるイメージだけど、ハードコードだと辛くない？

- たとえば source_ami_filter を使う
    - `source_ami: ami-xxxxxxxxx` ここに動的に値を入れる
    - ワイルドカードで指定する感じ
    - most recent なやつが選ばれる
    - 該当数は常に 1 件のみにする（2件以上ヒットすると failed 扱いになる）

see:

- [10分で理解するPacker - Qiita](https://qiita.com/Chanmoro/items/38e9d5441141f340e805)
- [PackerでAMIをぱかっと作ってみた | Developers.IO](https://dev.classmethod.jp/articles/packer-101-oku/)
- https://www.packer.io/docs/builders/amazon/ebs#source_ami_filter

