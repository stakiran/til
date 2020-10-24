# Cross Origin Resource Sharing オリジン間リソース共有

## オリジンとは
- domain + protcol + port

```
domain: yahoo.co.jp
origin: https://yahoo.co.jp:443
```

## CORSって何？
- セキュリティ上、他のオリジンからデータ読み込むのは望ましくない
    - Same Origin Policy という
    - これ破ると CSRF や XSS とか食らう
- でもそれじゃ不便
- 上手いこと許可しあったらいけるようにしよう ← これ定めたのが CORS

## 結局クライアントサイド、サーバーサイドは何をすればいい？
一言で

- サーバーサイド側で特定のレスポンスヘッダ返す実装が必要
- 細かい実装方法は Qiita 見て

サーバーサイド:

- 要求クライアントに対して `Access-Control-Allow-Origin` ヘッダ返すのが基本
- 下記の Cookie 分を許可したい場合は `Access-Control-Allow-Credentials: true` も必要

クライアントサイド:

- 基本的に何もしなくていい
- cookie 渡したい場合は追加オプションが必要
    - axios で言えば `axios.defaults.withCredentials = true` のセット

## Q: XMLHttpRequest at XXXX from origin YYYY has been blocked by CORS policy って何？
Ans: サーバーサイド XXXX は、YYYY からの別オリジンアクセスを許可してないです（or XXXX に実装したつもりでも何かミスっててちゃんと動作してない）

例:

> Access to XMLHttpRequest at 'https://outlook.office.com/webhook/...' (redirected from 'http://outlook.office.com/webhook/...') from origin 'http://localhost:8080' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

Teams の webhook が CORS 許可してない（Access-Control-Allow-Originを返してくれない）ので、localhost からは POST できない。

(ちなみにこの localhost:8080 は https://github.com/vuejs-templates/webpack-simple で npm run dev したもの)

## Q: Python requests でローカルから実行したらいけたけど、なんで？
Ans: curl も同様だが、単にプログラムから実行しただけであって、オリジンとして実行したわけではないから。

## 参考
- [CORS(Cross-Origin Resource Sharing) - とほほのWWW入門](http://www.tohoho-web.com/ex/cors.html)
    - HTTP リクエストとして何が必要かが端的にわかる
- [なんとなく CORS がわかる...はもう終わりにする。 - Qiita](https://qiita.com/att55/items/2154a8aad8bf1409db2b)
    - 実際のエラーメッセージから知りたい場合はこっち
