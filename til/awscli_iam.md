# AWSCLI aws iam

## IAM ユーザー作成
バッチファイルラッパーだけど

- パスワードポリシー通らないとエラーが出る
- 既存だったら already exists が出るだけ

```bat
@echo off
setlocal

set username=★User1
set password=★プログラムでつくる
set cmdline=call aws iam

%cmdline% create-user --user-name %username%
%cmdline% create-login-profile --user-name %username% --password %password% --password-reset-required
%cmdline% attach-user-policy --user-name %username% --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
%cmdline% attach-user-policy --user-name %username% --policy-arn arn:aws:iam::aws:policy/IAMUserChangePassword
```

作成したらログインURL、ユーザー名、パスワードを当人に教える

ログイン URLは以下でつくる

- 1: アカウントIDをget
    - `aws sts get-caller-identity | jq ".Account" | tr -d "\""`
- 2: `https://ここに入れる.signin.aws.amazon.com/console`

## IAM ユーザー削除
- 先に
    - ポリシー全部消す必要がある
    - login profile も消す必要がある

```
@echo off
setlocal
set cmdline1=call aws iam detach-user-policy --user-name
set deletee_policy1=--policy-arn arn:aws:iam::aws:policy/IAMUserChangePassword
set deletee_policy2=--policy-arn arn:aws:iam::aws:policy/★その他存在してるのは全部指定
set cmdline2=call aws iam delete-login-profile --user-name
set cmdline3=call aws iam delete-user --user-name

set username=★User1
%cmdline1% %username% %deletee_policy1%
%cmdline1% %username% %deletee_policy2%
%cmdline2% %username%
%cmdline3% %username%
```
