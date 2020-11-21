# Git

## ●ブランチつくって push するまで
branch でローカルにつくる

checkout で切り替える

git push origin xxxxx で指定ブランチに push。

```
$ git branch -a
* master
  remotes/origin/master

$ git branch develop_xxx

$ git checkout develop_xxx
Switched to branch 'develop_xxx'

$ git branch -a
* develop_xxx
  master
  remotes/origin/master

$ git push origin develop_xxx
Total 0 (delta 0), reused 0 (delta 0)
To https://...
 * [new branch]      develop_xxx -> develop_xxx
```

## ●merge マージ
マージされる側に checkout する。つまり merge とは merge from の意

```
git checkout master
git merge branch1
```

別の覚え方として、**今チェックアウトしているブランチが操作される** でもいい。マージする場合、操作されるのはマージされる側だから、merge は merge from なのだと自明になる。

## bra1 の更新を bra2 に取り込む

```
git checkout bra1
git pull
git checkout bra2
git merge bra1
```

いったん最新にした後、merge して取り込む。

## コミットメッセージ直前の修正

```
git commit --amend -m "修正後メッセージ"
```

## ローカルブランチとリモートブランチの削除
両方消したい場合には以下のようにする

- 1 ローカルから消す
    - `git branch --delete bra1`
- 2 リモート側も消す
    - `git push origin :bra1`
        - `(local):(remote)` のうち、ローカル側を空にしている
        - 空の内容でリモート側を更新しろ = リモート側を消せ

Q: ブラウザ画面でリモート側消した後、`git remote update` でローカル側に反映するには？

- Ans. 下記参照。

### git branch -a で、消したはずのリモートブランチが表示されたままになる
- サービス側の機能で消した、他人が消した等で起こる
- 以下で念の為 dry run した後、問題なければ実行

```
git remote prune origin --dry-run
```

参考: [消したはずのリモートブランチがローカルで表示されるので削除する - Qiita](https://qiita.com/nantekkotai/items/0ca7c9e850eff65aaf66)

## origin など remote のエイリアスを設定する

```
git remote add URL

gir remote set-url URL
```

editしたい場合はset-urlじゃないとダメ。

閲覧は git remote -v

## 少し前のコミット内容を、今のコミットの一つ上に積み上げたい（語彙力

### やりたいこと
こんなコミットログがあるとする。

```
bbbbbb commitmsg-5  <=== HEAD
aaaaaa commitmsg-4
zzzzzz commitmsg-3
yyyyyy commitmsg-2
xxxxxx commitmsg-1
```

xxxxxx の内容を積み上げたい。以下のようにしたい。

```
cccccc commitmsg-6  <=== HEAD
bbbbbb commitmsg-5
aaaaaa commitmsg-4
zzzzzz commitmsg-3
yyyyyy commitmsg-2
xxxxxx commitmsg-1
```

このとき、xxxxxx と cccccc の内容は同一である（それぞれ export して winmerge しても一致する）。

↑ これを実現するには？

### 方法
Tortoise Git と WinMerge を使う。

- 1: xxxxxx のコミットを export
- 2: 1 は zip なので適当な場所で展開
- 3: WinMerge を使って以下を比較
    - local repo
    - 2 で展開したフォルダ
- 4: 3 の結果を参考に、local repo の内容を、2 で展開したフォルダの内容に手作業で上書き
    - WinMerge で差分がなくなったら ok
- 5: コミットする

## git alias の登録

```
git config --global alias.s "status"
git config --global alias.ss "status --short"
git config --global alias.pom "push origin master"
git config --global alias.ls "log --pretty=oneline --abbrev-commit" 
```

## git credential.helper=cache とは
https の場合、user/pass で認証したあと、メモリ上に一定時間保持する。

## 特定サイトのみで ssl CA Info を使う

```
[http "https://XXXX.co.jp"]
	sslCAInfo=C://data1//crt//cer_for_xxxx.cer
```

## 過去コミットの author と commiter 全部変える
https://qiita.com/sea_mountain/items/d70216a5bc16a88ed932

```
$ git filter-branch -f --env-filter "GIT_AUTHOR_NAME='sea_mountain'; GIT_AUTHOR_EMAIL='valid_email@example.com'; GIT_COMMITTER_NAME='sea_mountain'; GIT_COMMITTER_EMAIL='valid_email@example.com';" HEAD 
```

## git config 削除
git config --global --unset http.sslVerify

--unset は key の前に書くこと。後に書くと value としてセットされてしまう。

## gitプロトコルで clone するときの url
git@github.com:stakiran/repo13.git

## 特定のコミットに戻る
git checkout (コミットID)

## ローカルの変更を打ち消す
git checkout FILENAME

以下で全部消す

git checkout .
