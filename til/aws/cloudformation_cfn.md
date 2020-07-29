# CloudFormation

## マネジメントコンソールを見れる IAM ユーザーをつくるには？（ポリシーは？）
`resouce=*` の Describe なポリシーをつくればよい。

逆を言えば特定インスタンスのみ Describe する、なんてことはできない（DesribeInstances、つまり全部リストアップしか action が用意されてない）。

## 指定インスタンスと SecurityGroup のみ触れる IAM ユーザー with パスワードログイン
- 指定インスタンスの start/stop と、指定 SG の ingress の edit のみサポート
- IAM ユーザーはパスワード持っててすぐにでもログイン可能
    - パスワードは Cfn つくるときに指定
    - つくった後、stack output から丸見え（noechoしてない）

```yaml
Parameters:
  WhitelistEditorUserPassword:
    Description: Password of an IAM user to edit whitelist.
    MinLength: 16
    Type: String
    Default: !PleaseUseThePasswordGenerator!

Resources:
  IAMUserForWhitelistEditor:
    Type: AWS::IAM::User
    Properties:
      LoginProfile:
       Password: !Ref WhitelistEditorUserPassword
       PasswordResetRequired: false
      Policies:
        - PolicyName: "whitelist-editor-instance"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
            - Effect: "Allow"
              Resource:
                -  !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:instance/$(Instance}"
              Action:
                - "ec2:DescribeInstanceStatus"
                - "ec2:DescribeInstanceAttribute"
                - "ec2:StartInstances"
                - "ec2:StopInstances"
        - PolicyName: "whitelist-editor-sg"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
            - Effect: "Allow"
              Resource:
                -  !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:security-group/${SG}"
              Action:
                - "ec2:RevokeSecurityGroupIngress"
                - "ec2:AuthorizeSecurityGroupIngress"
        - PolicyName: "whitelist-editor-describes"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
            - Effect: "Allow"
              Resource:
                - "*"
              Action:
                - "ec2:DescribeInstances"
                - "ec2:DescribeSecurityGroups"
      UserName: "whitelist-editor-for-xxx-env"
```


## metadata パラメーター並び順変更 version バージョン番号入れる

```
Metadata:
  Version:
    Description: "vA.B.C"
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label: 
          default: "Group xxx"
        Parameters:
          - Param1
          - Param3
          - Param4
      - Label: 
          default: "Group xyz"
        Parameters:
          - Param2
          - Param5
```

## IAMUser と AccessKey
指定インスタンスのみの start instance を許したい場合

```
Outputs:
  User1AccessKey:
    Value: !Ref AccsessKeyUser1
  User1SecretKey:
    Value: !GetAtt AccsessKeyUser1.SecretAccessKey

Resouces:
  IAMUserUser1:
    Type: AWS::IAM::User
    Properties: 
      Policies: 
        - PolicyName: !Join [ "-", ["Ref":"XXXX", "user1"]
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
            - Effect: "Allow"
              Resource:
                -  !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:instance/${Instance1"
                -  !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:instance/${Instance2}"
              Action:
              - "ec2:StartInstances"

  AccsessKeyUser1:
    Type: AWS::IAM::AccessKey
    Properties: 
      UserName: !Join [ "-", ["user1", "starter" ] ]
```

## SecurityGroup 設定戦略
- 何もつけなければ all deny
- SecurityGroup は「何らかの allow を追加する」ことにほかならない

よって **許可したいものだけ SecurityGroup でつけていく** 感じ。

## SecurityGroup で「指定した IP アドレスから導通」
下記サブネットの件と同じだが、cidr しか指定できないので /32 を補う必要がある。

```yaml
  SecurityGroupFromCiServer:
    Type: AWS::EC2::SecurityGroup
    Properties:
      ...
      SecurityGroupIngress:
        - IpProtocol: "-1"
          CidrIp: !Join [ "", ["Ref":"Server1PrivateIp", "/32"] ]
```

## SecurityGroup で「指定したサブネットから導通」
- サブネットの CIDR を指定する
- ただし以下注意点
    - サブネットの GetAtt では ipv6 の cidr しか取れない
    - しかしサブネット次第では **ipv6 が設定されてない** ことがある
    - 鉄板は「サブネット作成時に指定した cidr 文字列」をなんとかして指定すること

下記例では、サブネット作成時に使った cidr 文字列を、パラメータから渡してもらう形にしている。

```
Parameters:
  vpc:
    Type: AWS::EC2::VPC::Id
  CidrIpv4Subnet1:
    Type: String

Resouces:
  SecurityGroupFromSubnet1:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: SecurityGroup about FROM subnet-1.
      VpcId: !Ref vpc
      SecurityGroupIngress:
        - IpProtocol: "-1"
          CidrIp: !Ref CidrIpv4Subnet1
```

## SecurityGroup で「指定した SG がついたインスタンスのみ導通」
- 導通させたいインスタンスにつけるラベルは SecurityGroupWithinInstancesLabel
  - 実装は空
- 加えて、ラベルのついたもののみ通す SG として SecurityGroupWithinInstances をつくる

```yaml
  SecurityGroupWithinInstances:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: SecurityGroup about allow all within instances.
      VpcId: !Ref VpcId
      SecurityGroupEgress:
        - IpProtocol: "-1"
          DestinationSecurityGroupId: !Ref SecurityGroupWithinInstancesLabel
      SecurityGroupIngress:
        - IpProtocol: "-1"
          SourceSecurityGroupId: !Ref SecurityGroupWithinInstancesLabel
  SecurityGroupWithinInstancesLabel:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Label. SecurityGroup about allow all within this userstack instances. 
      VpcId: !Ref VpcId
```

- 最後に、インスタンスには上記二つをつける

```
  Instance1:
    Type: AWS::EC2::Instance
    Properties:
      ...
      SecurityGroupIds:
        - !Ref SecurityGroupWithinInstances
        - !Ref SecurityGroupWithinInstancesLabel
```

## EIP

```
  eipForInstance1:
    Type: AWS::EC2::EIP
    Properties: 
      Domain: vpc
      Tags:
        - Key: Name
          Value: !Sub ${Var1}-eip-instance1

  eipAssociationForInstance1:
    Type: AWS::EC2::EIPAssociation
    Properties: 
      AllocationId: !GetAtt eipForInstance1.AllocationId
      InstanceId: !Ref Instance1
```

インスタンス（Instance1）側の NetworkInterfaces は無しで良い。

- 同じテンプレートファイル内で VPC もつくっている場合は、DependsOn で「VPC が先に作成される」ようにすること ← 未確認だがドキュメントにそう書いてある
  - 既存の VPC に eip やインスタンスを作る場合なら不要

## パイプラインの実行（ステージ移行）をさせない
結論

- DisableInboundStageTransitions で先頭ステージ名を指定すれば良い
- ただしこのようなパイプライン上ではステージ実行がされなくなる（ので、したければ定義を削除して再アップロードするしかない）

===

課題:

- マネコン上で「進行中」のままになる
- 手動で「変更をリリース」ボタンを押しても実行されない

つまり **Disable した部分（ここでは全ステージ）を手動で実行させる方法がない**

```
  pipeline1:
    Type: AWS::CodePipeline::Pipeline
    Properties:
      ……
      DisableInboundStageTransitions:
        - Reason: ★理由書く
          StageName: Stage1 ★先頭のステージ名
      Stages:
        - Name: Stage1
          Actions:
            - Name: ……
        - ……
```

## DELETE FAILED になったスタックをキレイに消す
- 1 削除しようとすると「削除に失敗したリソースをスキップするか」的なのが出るので、これらを確認して手動で消す（既に消えていることもある）
- 2 この要領で、手作業で全部消す
- 3 終わったら、スタック削除で all skip にして実行 ← これでスタック自体が delete complete になって消える

## 説明欄の日本語入力は時期尚早
バリデーションでエラーが出なくても、日本語が表示されない(`???`で文字化けする)ことがある模様。

まだ英語のみで書いた方が賢そう at 2019/12/10
