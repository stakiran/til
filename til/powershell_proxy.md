# Powershell の proxy 設定
http_proxy 環境変数などは見てくれない

```
$ netsh winhttp show proxy
$ netsh winhttp set proxy proxy-server="SERVER:PORT"
```
