# CSS

# 直下、配下、隣接

```
a > b    aの直下のb
a b      aの配下のb(直下より下も辿る)
a + b    aに隣接したb
a ~ b    aの後ろにあるb
```

from http://weboook.blog22.fc2.com/blog-entry-268.html

# OR と AND
例
.class1
.class2

AND
  .class1.class2

OR
  .class1, .class2

# table のセンタリング
```html
<table class="center">
```

```css
.center {
  margin-left: auto;
  margin-right: auto;
}
```

[How To Center a Table](https://www.w3schools.com/howto/howto_css_table_center.asp)

# n番目
:nth-child(n)

[何番目系の便利なCSSまとめ - Qiita https://qiita.com/ituki_b/items/62a752389385de7ba4a2]

# リンク文字列の色を変える
a:xxxx でいくつかバリエーションある

```
/* For the link string in H1.
   The default link color is not too readable.
   So, comply the color of this theme, cayman, white. */
h1 > a:active, h1 > a:visited, h1 > a:link {
  color: #ffffff;
}
```

# 画像のセンタリング

```
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
```

# 見出しに連番を付ける
- 各 h タグに対して、counter-reset、counter、counter-increment で連番制御
- 表示テキストは ::before に対して content を使い、counter で数字参照
- body でのトップレベルカウンターリセットも忘れずに

以下は MDwiki カスタマイズ時の例

```css
/* for section numbering */

body {
  counter-reset: level1;
}

/* MDwiki では大見出しは表示されないので省略
#md-content h1 {
  counter-reset: level2;
}
*/

#md-content h2 {
  counter-reset: level2;
}

#md-content h3 {
  counter-reset: level3;
}

#md-content h4 {
  counter-reset: level4;
}

#md-content h2::before {
  counter-increment: level1;
  content: counter(level1) ". ";
}

#md-content h3::before {
  counter-increment: level2;
  content: counter(level1) "-" counter(level2) ". ";
}

#md-content h4::before {
  counter-increment: level3;
  content: counter(level1) "-" counter(level2) "-" counter(level3) ". ";
}
```
