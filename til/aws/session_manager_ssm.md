# AWS Session Manager bastion 踏み台レス
- SSM を使うと踏み台レスでインスタンス（Private subnet 下のものも）にアクセスできる
- 踏み台(EIP)要らない

## やること
- 各自の PC に aws ssm コマンドインストール
    - python, pip, awscli 必要
- 接続先インスタンス
    - 1 すべてに「AmazonSSMManagedInstanceCore ポリシーをアタッチしたロール」を付与
        - :o: 成功1: Amazon Linux 2 + AdministratorsAccess
        - :o: 成功2: Ubuntu Server 18.04 + AmazonSSMManagedInstanceCore + AmazonEC2RoleforSSM
        - AmazonSSMManagedInstanceCore だけでいけるかはまだ試してない
    - 2 **起動しているインスタンスに付与した場合、いったん再起動しないと反映されない**
    - 3 インスタンスが private subnet な場合は、NAT などでインターネットに出れるようにしておく
    - マネコンの接続ボタンからエラーが出なかったら OK

ハマる:

- インスタンスに SSM Agent のインストールが必要
    - Amazon Linux と一部 Ubuntu の AMI にはデフォでインストール済
    - 参考: [Linux の EC2 インスタンスで SSM エージェント をインストールして設定する - AWS Systems Manager](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/sysman-install-ssm-agent.html)
    - 参考: [プライベートサブネットに配置したEC2にAWS Systems Manager Session Managerを使ってアクセスする | Developers.IO](https://dev.classmethod.jp/articles/ssm-session-manager-private/)
        - UserData 使ってインストールするやり方（試してない）

## 接続方法
tp linux 

```
$ aws ssm start-session --target (インスタンスID)
```

to windows

```
$ aws ssm start-session --target (インスタンスID) --document-name AWS-StartPortForwardingSession --parameters "portNumber=3389,localPortNumber=12345"

$ (mstsc で localhost:12345 に繋ぐ)
```

## Q&A

### Q: CloudFormation では？

```yaml
  IAMRoleForSessionManagerLogin:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
        - Effect: "Allow"
          Principal:
            Service:
            - "ec2.amazonaws.com"
          Action:
          - "sts:AssumeRole"
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
        - "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM"
```

### Q: Could not connect to the endpoint URL: "https://ssm.ap-northeast-1.amazonaws.com/"
たぶんエンドポイントまで届いてない。プロキシ設定してないとか。
