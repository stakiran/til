# scp コマンド

## 基本
`scp i (pem) (local-source-file) (remote-user)@(remote-ip):(remote-destination-path)`

```
$ scp  -i pj1.pem ./data.zip ec2-user@10.0.0.1:/home/ec2-user
data.zip                                  100%   27MB  33.9MB/s   00:00
```

ip と path の間の `:` は必須なので注意。

(remote-destination-path) の指定バリエーション

```
/home/ec2-user       絶対指定(/home/ec2-user/data.zip)
renamed.zip          リモートのホーム基点(/home/ec2-user/renamed.zip)
testdir/renamed.zip  /home/ec2-user/testdir/renamed.zip
                     ただしリモート側で testdir ディレクトリまでが存在しないとエラー
```

(local-source-file) は *.key みたいにワイルドカードも使える。
