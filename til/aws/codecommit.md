# AWS CodeCommit

## codecommit 403 対策 cmdkey 削除
以下 kill_cmdkey.bat をつくって、タスクスケジューラから 15 分単位実行で登録。

```
@echo off
setlocal
set cmdbody=cmdkey /delete:LegacyGeneric:target=git:https://(YourDevAccount-AccessKey)@git-codecommit.ap-northeast-1.amazonaws.com/v1/repos

%cmdbody%/selflearn-infra
%cmdbody%/selflearn-userstack
%cmdbody%/selflearn-startup

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

