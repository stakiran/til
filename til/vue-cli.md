# Vue CLI

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
