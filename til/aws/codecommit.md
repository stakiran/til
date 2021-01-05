# AWS CodeCommit

## 複数の AWS アカウントの CodeCommit を使い分けて clone する
AWS アカウント1, 2 があるとする

1: ~/.aws/config やら credentials やら

- 1 と 2 の ca_bandle, access key, secret key などを定義する
- default と profile2 とか
- あるいは profile1 と profile2 とか

2: gitconfig の共通設定(以下は東京リージョン)

```
[credential "https://git-codecommit.ap-northeast-1.amazonaws.com/"]
	helper = !aws codecommit credential-helper $@
	UseHttpPath = true
```

問題は **この helper 指定時にもプロファイル指定が必要なこと。どうやって切り替えるか**。

3: たとえば alauncher でエイリアスつくる。

```ini
[codecommit_PROF1]
rawbin=git config --global credential.https://git-codecommit.ap-northeast-1.amazonaws.com/.helper "!aws --profile PROF1 codecommit credential-helper $@"

[codecommit_]
rawbin=git config --global credential.https://git-codecommit.ap-northeast-1.amazonaws.com/.helper "!aws codecommit credential-helper $@"
```

すると `codecommit_PROF1` コマンドを実行して、PROF1 側の helper が使える。

参考: [Using Git with AWS CodeCommit Across Multiple AWS Accounts | AWS DevOps Blog](https://aws.amazon.com/jp/blogs/devops/using-git-with-aws-codecommit-across-multiple-aws-accounts/)

- local の gitconfig で使い分ける案（だがこれだと最初の clone ができぬ）

## codecommit からの clone が repository not found でしくじる
どれか

- 期限切れの認証キャッシュ残ってる
- credential helper が正しくない(AWS configure のプロファイル指定が違うとか)
- そもそも権限ない

`set GIT_CURL_VERBOSE=1` でログ出すとわかる。

## codecommit 403 対策 cmdkey 削除
以下 kill_cmdkey.bat をつくって、タスクスケジューラから 15 分単位実行で登録。

```
@echo off
setlocal
set cmdbody=cmdkey /delete:LegacyGeneric:target=git:https://(YourDevAccount-AccessKey)@git-codecommit.ap-northeast-1.amazonaws.com/v1/repos

%cmdbody%/repo1
%cmdbody%/repo2

exit /b
```

## codecommit clone/pull 時に 403 が出る
- たぶん資格情報の期限切れ
- 保存されてる資格情報をいったんクリアする

Windows で wincred を使っている場合

```
$ cmdkey /list | grep -i aws
これで保存されてる資格情報を見る
たぶんこんな感じ

    ターゲット: LegacyGeneric:target=git:https://...@git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/(repo1)
    ターゲット: LegacyGeneric:target=git:https://...@git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/(repo2)
    ターゲット: LegacyGeneric:target=git:https://...@git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/(repo3)
    ...

$ cmdkey /delete:LegacyGeneric:target=git:https://(YourUserAccessKey)@git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/(RepoName)
これで消す
```

参考情報

- [AWS CodeCommitで急に403が返ってくるようになった時の対処方法 - Qiita](https://qiita.com/szk3/items/f346d5c1804653d8b35a)
    - まさにこれ
    - デフォの https の mac の credential だと keychain の有効期限が 15 分、これがすぐ切れてる
    - ~~windows の場合は？~~ 上述

