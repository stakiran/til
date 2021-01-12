# AWS Instance profile

## instance profile とは？
- ec2 インスタンスに IAM ロールを付与する機能
- aws の api(aws cliなど)を叩くために必要
- これがない場合、credentials を使う必要があってだるい

どうつくる?

- instance profile つくる
    - 割り当てる role を指定する
- instance に、instance profile を割り当てる

[Terraformを使ってEC2インスタンスにIAMロールを当ててみる - tjinjin's blog](https://cross-black777.hatenablog.com/entry/2015/12/04/233206)
