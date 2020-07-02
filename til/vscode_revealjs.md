# VSCode Reveal.js

## export to pdf
結論:

- **現時点では「ブラウザでプレビュー後に印刷ダイアログ出す」まで(PDFファイルはつくらない)**
- export/ フォルダにごりごり生成されるので gitignore する

## 1 open in presentation in browser は ok

```json
    "revealjs.browserPath": "C:/Program Files/Mozilla Firefox/firefox.exe",
```

これで export in html が可能になる

- 実行したら `export` フォルダがつくられる
- http://localhost:63240/#/ ← こんな URL でサーバー立つ

## 2 export in pdf は？
挙動としては **ブラウザでプレビューさせた後に印刷ダイアログ呼び出す** 感じ。pdf ファイルをつくるわけじゃない。

- http://localhost:63240/?print-pdf-now#/

印刷してみたが、**設定変えられない上に 1-slide 1-page で普通に見切れる** のでダメ。

## css style customize

### Front matter

```yaml
---
customTheme : "ここにCSSファイル名(.css要らず)"
---
```

### CSS

```css
/* .reveal クラスをつける感じ、あとは HTML そのもの */
.reveal strong {
    color: red;
}
```

## config
- https://github.com/evilz/vscode-reveal

> You can customize many setting on for your reveal.js presentation.

front matter に普通に指定していけばいい

## 投影する
- markdown ファイルとしてガシガシ
- pallet > revealjs: show presentation by side
- 書いてるペインを閉じる
- pallet > presentation mode

## 投影を終える
- もう一度 presentation mode

## インストール
- vscode-reveal
- Presentation Mode
