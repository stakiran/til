# Shell Script and Bash

## shell script で template を実現する

```sh
cat << EOS >> ファイル名
ここにファイル内容
ここにファイル内容
EOS

cat << EOS >> ファイル名
ここにファイル内容
こんな風に分割して書くこともできる
EOS

cat << EOS >> ファイル名
${shellscriptvar}
\${othersystemvar} shell script var として認識させたくない場合はエスケープする
EOS
```

## bash: Bad Substitution？
色々あるけど、

- 変数が見つからない
    - テンプレートとして使ってる場合に、sh じゃない変数は `${xxx}` じゃなくて `\${xxx}` にする必要あり
    - `${xxx}` だと sh として解釈してしまう
