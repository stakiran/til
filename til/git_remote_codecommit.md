# git remote codecommit
- [git-remote-codecommit を使用して AWS CodeCommit への HTTPS 接続をセットアップする手順 - AWS CodeCommit https://docs.aws.amazon.com/ja_jp/codecommit/latest/userguide/setting-up-git-remote-codecommit.html]
- [amazon s3 - how to check awscli and compatible botocore package is installed - Stack Overflow https://stackoverflow.com/questions/51911075/how-to-check-awscli-and-compatible-botocore-package-is-installed]
- [python - ImportError: cannot import name 'docevents' from 'botocore.docs.bcdoc' in AWS CodeBuild - Stack Overflow https://stackoverflow.com/questions/64596394/importerror-cannot-import-name-docevents-from-botocore-docs-bcdoc-in-aws-co]

## use
プロファイルに基づく codecommit を見に行くので、先にプロファイルを切り替えておく

```
$ set AWS_PROFILE=profile1

$ git clone codecommit://repo1
```

## install
boto系の再インストールから必要だった

```
pip uninstall botocore
pip uninstall boto3
pip install botocore
pip install boto3

pip install --upgrade awscli

pip install git-remote-codecommit
```
