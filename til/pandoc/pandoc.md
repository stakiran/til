# Pandoc

## Install 2.10 to win10 
- https://pandoc.org/installing.html
- Haskell なくてもいけるようになってる、37MB

## バイナリ
`%localappdata%\Pandoc\pandoc.exe`

## 任意変数を使うには template しかなさそう
pandoc -D epub3 で epub3 のテンプレート内容を見る。body 部分に本文流し込まれるので、そこ以外をいじればいけるって感じ？

これベースにして custom_template ファイルつくって、--template=custom_template するらしい？

[Pandoc - Pandoc User’s Guide](https://pandoc.org/MANUAL.html#option--template)

[Pandocのテンプレート機能でYAMLから本の奥付を自動生成する - Qiita](https://qiita.com/sky_y/items/47da01623f50380c2023)

## 縦書き

[文章は時空を超えて: 『縦書き』と『横書き』は印象がちがう——それぞれに合った書き方を](https://bunshohajikuwo.blogspot.com/2018/01/blog-post_21.html)

> 「文章は、縦書きよりも横書きのほうが読みやすい」という人の割合が多くなっていると言われています。

横書きだと空白入れないと読みづらくなる。

[縦書きの本よりも横書きの本を推したい｜ToLi｜note](https://note.com/toli_torey/n/n7057d7c3a7bb)

横書きメインなのに縦書き向けに直すのだるいよな

> 本を読み慣れている人にとっては、縦書きのほうが読みやすいようだ。「ネットの小説も縦書きで読みたい」という声も聞く。慣れってやつは強い。

> 私は本をガバガバ読む人間だが、縦書きのほうが読みやすいとは思わない。スマホで電子書籍を読んでいると、どっちも変わらないのだ。だって同じ画面でネットの横書きの文章も読むからね。

なれなのかなー

### 2020/03/07 html to mobi with kindlegen
読めたが、微妙。

- 行間がカスい
- padding 働いてない
- フォントも小さい？
- めくり方向が横書き
- 行頭がなぜか二文字分空いてる
- 目次機能は働かない

```
@echo off
setlocal

python renban.py -i draft.md -o book.md
rem html4 must?
pandoc -f markdown+emoji -t html4 --standalone -c ./stylesheet.css book.md title.txt -o book.html --toc --toc-depth=2

kindlegen book.html

pause
```

### 2020/03/07 小説で試した
- epub はダメ
- html
  - border-left は行頭ではなく「画面で見た左側」に付く感じ
  - 「a\nb」は別行にならない ← 当たり前だが。こういうのは全部直す必要あり

### how to
css

```
body {
  -epub-writing-mode: vertical-rl;
  writing-mode: tb-rl;
  direction: ltr;
}
```

ちょっと試してみた感想:

- 半角は縦にならない
- ボーダーがあると違和感満載
- table は右から左になる（除外できないのか？
- html で見てみると、firefox では？縦スクロールでスクロールできん

## 画像でキャプションを表示しない

```
![control_how_to_access.jpg](img/control_how_to_access.jpg) \
                                                            ^
                                                            これをつける
```

## 画像の中央寄せとキャプション

```
figure {
  text-align: center;
}

figcaption:before {
  content: "図.";
}
```

## 注釈

```
本文に [^1] をつけて……

[^1]: ここで解説
```

- html と epub では「末尾に注釈が一覧で表示される」「各注釈には "元の位置に戻るリンク" がある」という仕上がり。
- `[^word]` もいけるらしいが試してない
  - 関連では 1, 2 だから数字で良いかと思う
- 注釈の採番単位は以下のとおり
  - html → ページで一つ？（一番最後にまとめて 1,2,3...）
  - epub3 → 大見出し単位で採番される

## --list-extensions この pandoc のデフォの拡張機能オンオフ状況

```
-spaced_reference_links
+startnum
+strikeout
+subscript
+superscript
-styles
+task_lists
+table_captions
+tex_math_dollars
-tex_math_double_backslash
-tex_math_single_backslash
+yaml_metadata_block
```

`+` はじまりは有効のもの。`-` はじまりは無効のもの。

## --list-input-formats この pandoc がサポートする形式

## 番号つきリストは無効にできない？
a) はじまりとか防ぎたいが、できないっぽい。

startnum はいけそうだったが、

```
a. xxxxxxx
b. xxxxxxx

これが

a. xxxxxxx
a. xxxxxxx ★採番が続かない
```

これだけだった。

## 拡張機能の有効・無効
pandoc -f markdown+emoji-startnum

emojiは有効、startnumは無効。

## epub で使える絵文字
- :warning:
- :point_up:
- :coffee:

## 改ページ
<div style="page-break-before:always"></div>

## html
pandoc -f markdown+emoji -t html --standalone -c ./stylesheet.css why_your_windows_pc_heavy.md title.txt -o book.html --toc --toc-depth=2

## epub
pandoc -f markdown+emoji -t epub3 why_your_windows_pc_heavy.md title.txt -o book.epub --css stylesheet.css --toc --toc-depth=2 --epub-cover-image=cover.jpg
