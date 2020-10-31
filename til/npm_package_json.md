# npm

## cloc を npm run count として組み込みたい場合は？
- npm install cloc で package.json に追記
    - 余談: dependencies に入るので、devDependencies 側に移した方が良い

scripts 配下に以下を

```
  "scripts": {
    "serve": "vue-cli-service serve",
    ...
    "count": "cloc ./ ……"
  },
```

:memo: scripts 配下では ./node_modules/.bin が最優先パスになる

## package.json コメントアウトは？
- ダミーオブジェクトで囲む
- npm では `//` がコメントアウト用に reserved されてる


```
"// " : {
  ……
}
```

[How do I add comments to package.json for npm install? - Stack Overflow](https://stackoverflow.com/questions/14221579/how-do-i-add-comments-to-package-json-for-npm-install)

## npm install --save-dev って何？
[npm installの–saveと–save-devの違いと-g – the2g](https://the2g.com/2280)

> npm install -g

グローバル

> npm install とか npm install --save とか

ローカル、かつdependenciesに追記。開発プリの実行（動作）に必要な場合。

> npm install --save-dev

ローカル、かつdevDependenciesに追記。テストツールや Linter など開発ツールの実行に必要な場合。

以下 vue cli の例

- dependencies
    - vue
    - vue-router
    - vuex
    - axios
- devDependencies
    - eslint
    - @vue-cli-service
    - vue-template-compiler

## npm install が dyld: Library not loaded: /usr/local/opt/icu4c/lib/libicui18n.64.dylib エラーで動かん
brew update node

で直る。brew経由でnodeいじったのがあかんらしい。

see [npmのエラー解決「dyld: Library not loaded: /usr/local/opt/icu4c/lib/libicui18n.60.dylib」 - Qiita https://qiita.com/SuguruOoki/items/3f4fb307861fcedda7a5]

## package-lock.json is 何？
- npm v5+ くらいから npm install 時に自動生成されるブツ
- パッケージ依存関係を厳密に管理したファイル
    - バージョン管理してあげると優しい
- 頻繁に更新されるのでバージョン管理するのが面倒という立場もある

参考:

- [Debugging - Getting Started - Node.js](https://nodejs.org/en/docs/guides/debugging-getting-started/)
- [package-lock.jsonについて知りたくても聞けなかったこと - Qiita](https://qiita.com/yfujii1127/items/7ca887a45e0855917279)

## コマンドリファレンス
[npmコマンドの使い方 - Qiita https://qiita.com/yoh-nak/items/8446bf12094c729d00fe]
