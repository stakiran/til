# Python でシンプルな HTTP サーバーを立てる
導通テスト用途。

## サーバー側
python2

```
$ python -m SimpleHTTPServer 8080
```

python3

```
$ python -m http.server 8080
```

詳しい引数（バインドなど）は調べて。

## クライアント側からアクセスしたときの挙動
- ローカルでテスト
- chrome で http://127.0.0.1:8080/ を開く

```
$ cd
...\github\stakiran\regular

$ python -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
127.0.0.1 - - [07/Jul/2020 09:28:32] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Jul/2020 09:28:32] code 404, message File not found
127.0.0.1 - - [07/Jul/2020 09:28:32] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [07/Jul/2020 09:29:13] "GET / HTTP/1.1" 200 -        ★トップページへのアクセス
127.0.0.1 - - [07/Jul/2020 09:29:17] "GET / HTTP/1.1" 200 -        ★2回目
127.0.0.1 - - [07/Jul/2020 09:29:19] "GET / HTTP/1.1" 200 -        ★3回目
127.0.0.1 - - [07/Jul/2020 09:30:15] "GET /intoc/ HTTP/1.1" 200 -  ★intocフォルダを見た
```

index.html によるガードがないので、ブラウザからはファイルシステム上のファイル構造すべてが見えている状態。

## Q: ブラウザから何か表示させるには？
index.html を適当につくる

```
$ echo "<h1>Hello<h1>" >> index.html
```

## Q: permision denied になりますが
セキュリティのため 1024 以前のポートはデフォで使えない。

linux だと root 権限必要。

[permissions - How can I start the python SimpleHTTPServer on port 80? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/24598/how-can-i-start-the-python-simplehttpserver-on-port-80)

## Q: 0.0.0.0とは？
> すべてのネットワーク・インターフェースを表します。ワイルドカードのようなもので、すべての通信を表します。こちらは別ホストからでもアクセスすることが可能です。

- リモートからアクセスできるようにするための指定
- localhost だとローカル内完結だが、0.0.0.0 なら外部から当該ポートを指定して繋げるようになる

[127.0.0.1とlocalhostと0.0.0.0の違い - Qiita](https://qiita.com/1ain2/items/194a9372798eaef6c5ab)
