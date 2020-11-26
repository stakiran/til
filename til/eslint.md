# ESLint

## import hoge from `@/xxxx.js` で hoge を使わない場合にエラー無視したい

```
// eslint-disable-next-line no-unused-vars
import hoge from '@/xxxx.js';
```

[ESLintのコメントでのルール制御 - Qiita](https://qiita.com/nju33/items/2d0cfea4fffbfdbff87a)

## 初期設定
eslint --init でウィザード

## フォーマッタを使う
eslint --fix hoge.js

これで eslint ルールに従って hoge.js を直す。

# Rules

## 複数行コメントの書き方
https://eslint.org/docs/rules/multiline-comment-style

stared block, bare, separate line の三種類がある

```
    "rules": {
        "multiline-comment-style": ["error", "starred-block"]
    }
```

## タブ幅のみ適用する書き方
.eslintrc.json

```json
{
    "rules": {
        "indent": [
            "error",
            4
        ]
    }
}
```

# 推奨設定を使うサンプル
from [ESLintでJavaScriptの構文チェックを始める ｜ Tips Note by TAM](https://www.tam-tam.co.jp/tipsnote/javascript/post9944.html)

```json
{
  "extends": "eslint:recommended",
  "rules": {
    "curly": "error",
    "no-undef": "error"
  },
  "env": {
      "browser": true,
      "jquery": true
  },
  "globals": {
    "exports": true,
    "require": true,
    "MODULE1": true,
    "MODULE2": true,
    "DATACLASS1": true
  }
}
```
