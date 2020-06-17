# jq

# ["hoge"] ← これから hoge を取り出す

```
jq -r .[0]

$ aws ec2 describe-instances --filters "Name=vpc-id,Values=vpc-XXXXXXXXXXXXXXXXX" "Name=private-ip-address,Values=10.0.0.1" --query "Reservations[].Instances[].NetworkInterfaces[].NetworkInterfaceId"
[
    "eni-YYYYYYYYYYYYYYYYY"
]

$ …… | jq .[0]
"eni-YYYYYYYYYYYYYYYYY"

$ …… | jq -r .[0]
eni-YYYYYYYYYYYYYYYYY
```

# お試し
普通に python やら js やらで書くのと同じように書けばok。

→ **ピリオド始め + pythonでjs書くのと同じ要領(ただしピリオドで繋ぐ)**

エスケープとかでくるしそうならリファレンス見て。-r だかなんだが回避策は普通にあるみたい。

```
$ watch.bat
{
    "StackEvents": [
        {
            "StackId": "arn:aws:cloudformation:...",
            ……,
            "ResourceStatus": "CREATE_IN_PROGRESS",
            ……
        }
    ],
    "NextToken": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

$ watch.bat | jq ".StackEvents[0].ResourceStatus"
"CREATE_COMPLETE"
```
# 入手

## windows
公式サイトから jq.exe バイナリを。

PATH 通った場所に置く。

## centos

```
yum install epel-release
yum install jq
```

## rhel

```
sudo su
yes | yum install wget
wget -O jq https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
chmod 775 ./jq
cp jq /usr/bin
```

