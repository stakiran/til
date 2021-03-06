# Git

## ●merge マージ
マージされる側に checkout する。つまり merge とは merge from の意

```
git checkout master
git merge branch1
```

別の覚え方として、**今チェックアウトしているブランチが操作される** でもいい。マージする場合、操作されるのはマージされる側だから、merge は merge from なのだと自明になる。

### master の最新内容を開発ブランチ bra1 にマージしたい

```
git co master
git pull origin master
git co bra1
git merge origin master
```

master を更新して、bra1 に移って master をマージするだけだが、origin が必要（なんで？）。

### PR 時に出てる Conflict の解消
GitHub で案内出てるからそれに従えばよいが

step1 として、master 側の更新を取り込んでから conflict を解消する。

```
git fetch origin
git checkout -b bra1 origin/bra1
git merge master
```

終わったら、step2 として master 側にマージする。

```
git checkout master
git merge --no-ff bra1
git push origin master
```

- `--no-ff`？
    - fast-forward マージさせないオプション
    - merge to master 時は、極力これでマージするのが推奨されている
    - fast-forward だと（マージ用のコミットをつくらないので）更新追いかけづらい
        - merge 元である bra1 側と比較して見比べるとか調べるとかしづらい
    - see: [gitのmerge --no-ff のススメ - Qiita](https://qiita.com/nog/items/c79469afbf3e632f10a1)

## ==

## git status で日本語ファイル名が文字化けする

```
[core]
	quotepath = false
```

## ブランチつくって push するまで
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

## git log で日本語が文字化けする
less の文字コードみたい

```
$ set LESSCHARSET=utf-8
```

## git rebase ミスったのでやめたい
git rebase --abort

直近1回分の rebase をキャンセルできる。

## コミットログをキレイにする git rebase -i
- git rebase -i
- わからない場合は適当に新規に repo つくって、そこで試してみる
- コミットの歴史を書き換えるので、他人も使ってる remote branch には push しない
- Q: 実際運用するときはどんな感じになる？
    - local branch でガシガシコミットする
    - (このとき push はしない)
    - 落ち着いたら、git rebase -i でコミットを整理
    - 整理できたら、push する
    - :rabbit: **ガシガシも全部 remote に置いて見せたい！的な発想は捨てましょう**
- Q: でもそのコードに至った過程とか残したいじゃない？
    - そこはチーム次第
        - 「fix typo みたいなくだらないものは消して」かもしれないし
        - 「いや過程とかいいから数コミットくらいでまとめてくれ」かもしれないし
- Q: -i (commitID) の commitID が指すコミットは破壊される？
    - Ans: されない
    - fとrをする限りはされない（ほかは知らない）
    - rebase -i の実行前後で log を確認して、commitID が変わってないことを見てみればいい

```
$ git log --oneline
コミットを確認する
```

```
$ git rebase -i (CommitID)
latestから指定コミットまでの範囲について、
コミットをいじるモードに入る
```

いじるモードのファイル

- oneline 形式で、**古いコミットから** ずらりと並ぶ
- 書き方は普通にコメントで書いてあるのでそえｒを

隣接する2つのコミットをまとめたい場合

- fixupを使う
    - 自分を、一つ上のコミットにまとめる
    - コミットメッセージは、一つ上の方をそのまま使う
- before
    - pick xxxxxxx commit1
    - fixup yyyyyyy commit2
    - pick zzzzzzz commit3
- after
    - pick xxxxxxx commit1 ★ここにcommit2の変更も入っている
    - pick zzzzzzz commit3

隣接するnつのコミットをまとめたい場合(fixupはfでもいける)

- before
    - pick xxxxxxx commit1
    - f yyyyyyy commit2
    - f zzzzzzz commit3
- after
    - pick xxxxxxx commit1 ★ここにcommit2とcommit3の変更も入っている

see:

- [あのコミットをなかった事に。git rebase -i の使い方 - karakaram-blog](https://www.karakaram.com/git-rebase-i-usage/)

## gitconfig の layer
- 1 system
    - `(Gitインストール先)\etc\.gitconfig`
- 2 global
    - `%userprofile%\.gitconfig`
- 3 local

global に書いたのに反映されない場合、system 側を見る。

## 改行コードの違いだけで差分になって git status 出ているけど、どうすればいい？
- そのままコミットすればいい
- git が差分吸収してくれる
    - 新規コミットにせずに対処してくれる

## コミットログの username や email を書き換える
まとめ:

- local repo または一人用 repo ならお好きにどうぞ
- 複数人 repo の場合はやめた方がいい
    - commit filter で該当箇所だけ書き換えても、全部のコミットの情報書き換えちゃうので
    - つまり push -f が事実上必須

なんか `rebase -i` とか使えば個別に直せるらしいが、まだ試してない。

コード:

- Windows の場合、xxx.sh に書いてから `sh ./xxx.sh` などを実行する
    - 要 Git For windows
    - `C:\Program Files\Git\usr\bin\sh.exe` が使われてる

```sh
git filter-branch --commit-filter '
        if [ "$GIT_AUTHOR_EMAIL" = "schacon@localhost" ];
        then
                GIT_AUTHOR_NAME="Scott Chacon";
                GIT_AUTHOR_EMAIL="schacon@example.com";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' HEAD
```

> コミットにはその親の SHA-1 値が含まれるので、このコマンドは (マッチするメールアドレスが存在するものだけではなく) すべてのコミットを書き換えます。

see: [Git - 歴史の書き換え](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%81%95%E3%81%BE%E3%81%96%E3%81%BE%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB-%E6%AD%B4%E5%8F%B2%E3%81%AE%E6%9B%B8%E3%81%8D%E6%8F%9B%E3%81%88)

## リモートにあるブランチをローカルでマージしたい

```
$ git fetch origin (branchname)
```

これでローカルに取り込まれるので、あとは origin 指定で merge する。

```
git merge origin/(branchname)
```

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

## delete ローカルブランチとリモートブランチの削除
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
