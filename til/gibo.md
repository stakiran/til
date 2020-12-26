# gibo

## Q: 内部の仕組みどうなってんの？
- 初回は git clone で .gitignore 集を DL してくる
    - windows だと %appdata%\.gitignore-boilerplates
- あとは dumop (Name) で与えられた Name に対応するファイルを stdout する

なのでバッチファイルみたいなシェルのスクリプトレベルで実現できてる。

## .gitignore を吐き出す
terraform で試す例

- dump (name)
- 拡張子ではなく名前
    - dump tf は unknown だった
- stdout なのでファイル化したければリダイレクト

```
$ gibo dump terraform
### terraform

# Local .terraform directories
**/.terraform/*

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log

# Exclude all .tfvars files, which are likely to contain sentitive data, such as
# password, private keys, and other secrets. These should not be part of version
# control as they are data points which are potentially sensitive and subject
# to change depending on the environment.
#
*.tfvars

# Ignore override files as they are usually used to override resources locally and so
# are not checked in
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Include override files you do wish to add to version control using negated pattern
#
# !example_override.tf

# Include tfplan files to ignore the plan output of command: terraform plan -out=tfplan
# example: *tfplan*

# Ignore CLI configuration files
.terraformrc
terraform.rc



$ gibo dump tf
Unknown argument: tf
```

## install on windows

```
$ cd
d:\bin

$ git clone https://github.com/simonwhitaker/gibo
```

ala

```
[gibo]
rawbin=%bin%\gibo\gibo.bat %*
```
