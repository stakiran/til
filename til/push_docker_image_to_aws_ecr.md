# ECR に docker イメージを push する
assume-role で行う例

## IAM まわり

### assume-role で手に入れるロール R
- これでも「pushするのに必要な最小限」だったりする……
    - なんか read 系も色々必要みたい
    - see: https://docs.aws.amazon.com/ja_jp/AmazonECR/latest/userguide/security_iam_id-based-policy-examples.html
    - 実際、これ全部指定しないと push が通らなかったりした（ケースがあったりした）
    - これ、実質[AmazonEC2ContainerRegistryPowerUser](https://docs.aws.amazon.com/ja_jp/AmazonECR/latest/userguide/ecr_managed_policies.html#AmazonEC2ContainerRegistryPowerUser)と同レベルだよなー……
- 信頼されたエンティティで、後述のユーザー U を入れるのも忘れないように


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetRepositoryPolicy",
                "ecr:DescribeRepositories",
                "ecr:ListImages",
                "ecr:DescribeImages",
                "ecr:BatchGetImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:PutImage",
                "ecr:GetLifecyclePolicy",
                "ecr:GetLifecyclePolicyPreview",
                "ecr:ListTagsForResource",
                "ecr:DescribeImageScanFindings"
            ],
            "Resource": "*"
        }
    ]
}
```

### assume-role するユーザー U

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::(AccountID):role/(ロールRの名前)"
        }
    ]
}
```

## コマンドライン
前提:

- `~/.aws.credentials` には、ユーザー U のアクセス/シークレットキーを設定している
- assume-role で手に入れたキーは AWS_XXXXX 環境変数にセットして使う
    - 環境変数の方が優先順位が高いので、セットした分が使われる
    - 使わなくなったら環境変数消せばいい(unset)ので、つけ外しが楽
- jq コマンド使ってる

指定するもの:

- role_arn には、ロール R を指定する
- role_session_name は、ただのセッション名なので被らなければ何でもいいと思う

```
echo assume-roleします
echo ----

temp_credentials=assume-role-credentials.sensitive
aws sts assume-role --role-arn $role_arn --role-session-name $role_session_name > $temp_credentials

echo 環境変数にセットするのだるいので, ファイルに吐き出したものをjqで取り出して挿入までします
echo ----

export AWS_ACCESS_KEY_ID=`cat $temp_credentials | jq ".Credentials.AccessKeyId" -r`
export AWS_SECRET_ACCESS_KEY=`cat $temp_credentials | jq ".Credentials.SecretAccessKey" -r`
export AWS_SESSION_TOKEN=`cat $temp_credentials | jq ".Credentials.SessionToken" -r`

echo ECRにログインします
echo ----

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin $ecr_repos_url

echo push
echo ----

docker push $your_image_tagname $ecr_repos_url/$ecr_repos_name:$your_image_tagname_for_ecr
```
