# linked account を Cfn で自動構築する
無理そうだが、ほぼ自動は可能。

- アカウント CRUD 部分は boto3 などで
- アカウントに対するリソース作成は CFn で
- Cfn Stackset を使えば「リージョンとアカウントの組」をリストにして、そいつらに同じスタックを流せる

## AWSCLI や boto3 ならある
[Create AWS Accounts with CloudFormation - The IT Hollow](https://theithollow.com/2018/09/10/create-aws-accounts-with-cloudformation/)

- lambda で `client.create_account` とか使ってる

[Automate account creation, and resource provisioning using AWS Service Catalog, AWS Organizations, and AWS Lambda - AWS Management & Governance Blog](https://aws.amazon.com/jp/blogs/mt/automate-account-creation-and-resource-provisioning-using-aws-service-catalog-aws-organizations-and-aws-lambda/)

- これも結局 lambda
- https://github.com/aws-samples/account-factory/blob/master/AccountCreationLambda.zip

結論: アカウント作成のレイヤーは awscli や boto3 など sdk 使わないとダメですー

## Cfn もアカウント作成のレベルではリソースがない

## stackset
[CloudFormation スタックセットを利用した 複数のAWSアカウントやリージョンを横断したリソース展開 - Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/)

- スタックセット
- 「リージョンとアカウントの組」をリストで持ち、各々に対してスタック流せる

[【AWS】複数のAWSアカウントを管理するためにStackSetを活用する #1/2【Multi Accounts】 - Qiita](https://qiita.com/tmiki/items/6a72b9ce67ed0a85e243)

- 日本語で詳しい
- 各アカウントに対してスタック流せるのはわかった
