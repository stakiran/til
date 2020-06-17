# ESLint

# フォーマッタを使う
eslint --fix hoge.js

これで eslint ルールに従って hoge.js を直す。

# タブ幅のみ適用する書き方
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
