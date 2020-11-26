# prettier

## 手元で使いたい場合

```
$ npm install -g prettier

$ prettier hoge.js

$ prettier hoge.js --write
```

## ESLint との違い
[Prettier 入門 ～ESLintとの違いを理解して併用する～ - Qiita](https://qiita.com/soarflat/items/06377f3b96964964a65d#%E4%BD%95%E6%95%85-prettier-%E3%82%92%E5%88%A9%E7%94%A8eslint-%E3%81%A8%E4%BD%B5%E7%94%A8%E3%81%99%E3%82%8B%E3%81%AE%E3%81%8B)

- prettier の方が整形の品質が高い
- eslint は構文チェックもできる（というかメイン）が、prettier は整形しかできない
    - ので eslint でチェックして、整形は prettier と分担する、などがベター
