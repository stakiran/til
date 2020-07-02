# peco

## 復数選択
ctrl + space

出力順は常に表示順固定。

## フィルタリングしたファイル名を指定プログラムで開く

```
$ ls | peco | xargs start "" "%hidemaru%"
```

## フィルタリングしたファイル名をコピー

```
$ ls | peco | clip

$ ls | peco | clip | cut -d$'\n' -f1
```

cmd だと下は使えない。cmd が改行文字という概念を表現できない。
