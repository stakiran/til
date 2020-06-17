# gitignore

## 空ディレクトリを保持したい、でも中身は管理したくない
中身を管理したいなら .gitkeep。

```
*
!.gitignore

# 必要なら解説もつけておくとよい
!README.md
```

## ホワイトリスト形式で指定ディレクトリ配下を管理対象に含めたい

(root)\.gitignore として

```
# いったん全部除外
*
# ディレクトリも全部除外
*/
# !XXXX で例外を書いていく
!.gitignore
!*.py
!*.md
# ★data フォルダ配下も例外に追加したいんだけど、どうしたらいいい？
?????

```

答え

- 1. `(root)\.gitignore` に `!data/` を追加
- 2. `(root)\data\.gitignore` に `!*` を追加

data フォルダの中にも gitignore が必要なのね。。。

## ローカルに無視設定を追加したい(リポジトリ設定として入れたくない)場合
https://help.github.com/articles/ignoring-files/

> Use your favorite text editor to open the file called .git/info/exclude within the root of your Git repository. Any rule you add here will not be checked in, and will only ignore files for your local repository.
> 
> 1.In Terminal, navigate to the location of your Git repository.
> 
> 2.Using your favorite text editor, open the file .git/info/exclude.

## gitignoreに書いてるのに無視されない場合
とりあえず既にバージョン管理下に置かれてないか否かを調べる。

置かれている場合、index から remove してやる。

## ■ホワイトリスト
.gitignore, text2pcap.bat, pyスクリプト(ただしold配下を除く)
のみを選定したい場合。

```
*
!.gitignore
!text2pcap.bat
!*.py
old
```

全部弾いた後に ! で例外を指定してくイメージ
