# AWS Secret Manager
- 秘密情報を一箇所に集める
- 機密情報使うアプリは、毎回コイツから取得する(not ハードコード)
- > コード内のハードコードされた認証情報 (パスワードを含む) を Secrets Manager への API コールで置き換えて、プログラムでシークレットを取得することができます。

ローテーションとは:

- Secret Manager 側が持ってる認証情報を切り替えること
- RDS など主要サービスは自動で切り替わる
    - たぶん RDS 側でパスワード変えただけで自動で追従してくれる
- 自動が対応してないサービスも、lambda 関数つくればいけるらしい

使うときのイメージ

```
aws secretsmanager get-secret-value --region ${REGION} --secret-id ${SECRETS_ID} 
```

実際はロールの管理や付与も必要なんだろうが。

see:

- [機密情報を一元管理できる「AWS Secrets Manager」とは？概要と主要機能、動作原理、各種リソースまとめ | Developers.IO](https://dev.classmethod.jp/articles/about-secrets-manager/)
- [AWS Secrets Manager とは - AWS Secrets Manager](https://docs.aws.amazon.com/ja_jp/secretsmanager/latest/userguide/intro.html)
- [AWS Secrets Managerを使おう！ - Qiita](https://qiita.com/mm-Genqiita/items/f93285a6058c64b39f23)
