# Vue CLI

## vue.config.js の中身が人によって違うのでバージョン管理どうすればいいっすか？
- そもそも optional config なので必須設定を書かない
    - [Configuration Reference | Vue CLI](https://cli.vuejs.org/config/#vue-config-js)
- .env.local を使う

## .env.local で環境変数を定義する
環境変数は独自ファイルで定義するようになっている。

[Modes and Environment Variables | Vue CLI](https://cli.vuejs.org/guide/mode-and-env.html#environment-variables)

```
.env                # loaded in all cases
.env.local          # loaded in all cases, ignored by git
.env.[mode]         # only loaded in specified mode
.env.[mode].local   # only loaded in specified mode, ignored by git
```

- ignored by git はよくわからん。,gitignore に明示的に書かないと無視されなかったですけど。
- mode はまだ試してない。ビルド時に `vue-cli-service build --mode development` みたいに与えることで選ぶ感じらしい

以下は .env.local を試してみた例

.env.local

```
VUE_APP_VARNAME1=123
VUE_APP_VARNAME2="string"
VUE_APP_YOUR_LOCAL_PROXYADDRESS="http://127.0.0.1:12345"
```

vue.config.js

```
module.exports = {
	devServer: {
		proxy:process.env.VUE_APP_YOUR_LOCAL_PROXYADDRESS
	}
}
```

## devServer.proxy って何？
- https://cli.vuejs.org/config/#devserver-proxy

```
module.exports = {
  devServer: {
    proxy: 'http://localhost:4000'
  }
}
```

> This will tell the dev server to proxy any unknown requests (requests that did not match a static file) to http://localhost:4000.

静的ファイルアクセスに該当しないすべての通信を、ここで指定したアドレスとポートに飛ばせ、という意味。

つまり、

- npm run serve で localhost:8080 が出たとする
- devServer.proxy で localhost:4000 を指定したとする
- この場合の動作は、
    - localhost:8080 上で発生した通信のうち、
    - 静的ファイルアクセスでないものは、
    - 全部 localhost:4000 に飛ばす

何が嬉しい？

- たとえばバックエンドがリモートにある場合
    - ポート転送で 4000 にバックエンドを繋いでおく
    - そしたら、実質 localhost;8080 で動かしてるローカルサーバ内通信を、バックエンド側に遅れる

まとめ

- そもそも npm run serve は localhost:8080 から開いてるポートを割り当てる
- でもこれじゃポート番号変えたい時に不便だよね
- そのために devServer.proxy で変えることができるよ


## npm run serve 後のポート番号はどうやって指定する？
これ

```
  App running at:
  - Local:   http://localhost:8080
  - Network: http://10.xxx.xxx.xxx:8080
```

この 8080 を自由に変えたいという話。

- Ans: できません
    - というか空きポートが自動でアサインされる
    - 8080 から順番に見ていく感じ
    - 既に 8080-8082 が使われてたら、上記は ;8083 になる

## vue init が downloading template から進まない
- 原因不明、たぶんプロキシか何か
- ぐぐっても解決策出てこない
- 環境変数 http(s)_proxy、pnpm -g config set proxy|https-proxy もダメ

仕方ないのでオフラインで対処する

```
$ git clone https://github.com/vuejs-templates/webpack-simple
$ mkdir %userprofile%\.vue-templates
$ move webpack-simple %userprofile%\.vue-templates

$ vue init webpack-simple YourProject --offiline
```
