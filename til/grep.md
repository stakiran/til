# grep

## ●基本パターン
from [grepでこういう時はどうする? - Qiita https://qiita.com/hirohiro77/items/771ffb64dddceabf69a3]

```
grep 検索したい文字列 検索したいテキストファイル

コマンド | grep 検索したい文字列

grep -e 検索したい文字列1 -e 検索したい文字列2 検索したいテキストファイル

grep -i 検索したい文字列 検索したいテキストファイル

grep -v 除外したい文字列
```

## grep で指定配下に NG キーワードを含むファイルがないか調べる例
仮に以下を NG にした場合

- `hoge\`
- `jp.`
- `abc`
- `DeF`

```
grep -inrE "(hoge)\\\\|(jp)\.|abc|def" *
```

解説

- i で大文字小文字無視
- n で結果に行番号表示
- r で再起検索
- E で正規表現使用

## grep: Trailing backslash がでて \\ で検索できない
`\\\\` と四つで。

```
$ grep -rE "(windows)\\\\" *
```

## 指定ディレクトリ以下の検索

```
grep -r 検索文字列 検索対象パス

grep -r 検索文字列 *
  → カレントディレクトリ以下すべてを対象にする
```


## 指定ディレクトリを除外する

```
$ grep -rn "todo" ./ --exclude-dir={.git,node_modules}
```

## カレントディレクトリ配下のgrep

```
$ grep -n -r --include="*.cpp" --include="*.h" "hoge" ./
./hogemod/hogemodMain.cpp:23:#include "hogelib.h"
./hogemod/hogemodMain.cpp:24:#include "hogelib2.h"
…
```

ポイント

- 「--include」オプションで複数区切れる
- -n でライン数表示
- -r で再帰検索

## 固定文字列で検索
`grep -F "[caption=]"`

## 複数キーワードの検索
`find . -name "*.cpp" -o -name "*.[ch]" | xargs grep -f [検索文字列ファイル]`

## grep: input file 'X' is also the output. が出る
grep でファイルにリダイレクトすると、そのファイル自体も grep 検索対象になり「grepのinputかつoutput」という状態になる。grep の仕様上、それは問題があるみたい。

`--exclude` で、リダイレクト先ファイル名を除外してやるとよい。

```
$ grep -n -r --exclude=".grep" --exclude-dir=".git" "@todo" ./ > .grep
```
