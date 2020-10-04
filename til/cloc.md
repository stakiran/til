# cloc

```
$ cloc ./ --by-file --report-file=%outfile%
```

- ./ でカレントディレクトリ配下
- --by-file でファイルごとに
- 出力はリダイレクトよりもオプション使った方が安定する?

## 指定ディレクトリを弾く

```
--exclude-dir=node_modules,html
```

## 指定ファイルを弾く

```
--not-match-f="(data\.js)"
```

正規表現の not match f(file) で。`--exclude-list-file` は上手いこと動いてくれない on windows 10。

## .vue ファイルをカウントしてくれません
- 1 clocを最新バージョンにあげる
    - https://github.com/AlDanial/cloc/releases
- 2 cloc github からリクエストする
