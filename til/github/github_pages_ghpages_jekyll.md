# GitHub Pages

## 自動リンク
[Syntax | kramdown](https://kramdown.gettalong.org/syntax.html#automatic-links)

[Autolink in kramdown? · Issue #459 · barryclark/jekyll-now](https://github.com/barryclark/jekyll-now/issues/459)

`<>` で囲めばいいらしい……

## タイトルのパイプ区切りをなくしたい

```
    <title>{{ page.title }} - {{ site.title }} </title>
```

テンプレに title タグ直打ちしちゃう。

## Jekyll Kramdown デフォ設定
[Default Configuration | Jekyll • Simple, blog-aware, static sites](https://jekyllrb.com/docs/configuration/default/)

## Jekyll
[GitHub PagesとJekyllについて - GitHub ヘルプ](https://help.github.com/ja/github/working-with-github-pages/about-github-pages-and-jekyll)

以下のファイル・フォルダはダメ

- /node_modulesまたは/vendorと名付けられたフォルダ内にあるもの
- 次のいずれかの文字で始まるもの: _、.、 #
- 次の文字で終わるもの: ~

デフォで搭載されたプラグインがいｋぅつかある

- [GitHub - benbalter/jekyll-titles-from-headings](https://github.com/benbalter/jekyll-titles-from-headings)

## Jekyll variables
[Variables | Jekyll • Simple, blog-aware, static sites](https://jekyllrb.com/docs/variables/)

site.xxx とか page.xxx とか
