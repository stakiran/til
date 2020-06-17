# npm

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
