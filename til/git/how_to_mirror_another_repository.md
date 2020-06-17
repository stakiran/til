# Git リポジトリを別のリモートリポジトリに同期（ミラーリングする）

## new
- 1: 同期先で create new repo
- 2: ローカルで

```
$ git clone --mirror (SOURCE REPO URL)
$ (cdする)
$ git push --mirror (1のcloneURL)
```

## update

```
$ git remote add (適当に名前つける) (1のcloneURL)
$ git fetch --all
$ git push (適当につけた名前) --mirror
```
