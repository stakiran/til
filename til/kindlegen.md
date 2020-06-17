# kindlegen

## 2020/03/07 10:53:09
[kindlegen](https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765211)

- pandoc などで html をつくる
- kindlegen book.html で mobi をつくる

mobi を開いてみる

- kindle でも文字化け、縦書きならず
- kindle previewer3 でも文字化け、縦書きならず

いけた！ pandoc 側で html4 だわ

```
pandoc -f markdown+emoji -t html4 --standalone -c ./stylesheet.css book.md title.txt -o book.html --toc --toc-depth=2
```

参考: [S1500M: Markdown 記法から縦書き mobi (kindle direct publishing で出版可能な) ファイルを作成する](https://s1500m.blogspot.com/2017/06/markdown-mobi-kindle-direct-publishing.html)
