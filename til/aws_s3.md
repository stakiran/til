# aws s3

## cp(download)

```
$ aws s3 cp s3://bucket1/file1.ext ./
```

- `src dst` の形式で指定する
    - local s3
    - s3 s3
    - s3 local
- これはバケットのファイルをカレントディレクトリに持ってきている例

## sync(upload files and directories)

```
$ aws s3 sync ./ s3://bucket1 --exclude "*" --include "*.txt"
```

- カレントディレクトリの `*.txt` を、s3 のバケット bucket1 にアップロード
    - デフォは include all なので、 **まず exclude all を明示的に指定したあと**、include で指定する必要がある

## sync 詳細

```
aws s3 sync ./dist/ s3://$S3_BUCKET_NAME/ --include "*"
```

- ./dist 内の全ファイルを送信する
- 送信するもの、しないものは include と exclude で制御する
    - あとに書いたものが上書きされる仕様
    - deny的 …… 最初に `include *` して、個別に exclude する
    - allow的 …… 最初に `exclude *` して、個別に include する
- exclude folder
    - :x: `node_modules`
    - :x: `node_modules/`
    - :o: `node_modules/*`

### 同期の挙動について
- exclude に基づいて同期されるわけではない
    - exclude `node_module/*` したからといって、既にアップロードされた `node_modules/*` が削除されるわけではない
    - include/exclude は **これからアップロードしようとしてるファイル達のうち、どれを選ぶか選ばないか** を指定しているにすぎない
- Q: じゃあミラーリングはどうやる？
    - ローカル側に存在しないファイルを消したい場合は、`--delete` をつける
- Q: exclude したファイル達は、--delete による削除の対処からも外せる？
    - yes

ベストプラクティス

- アップロードしたいものは1フォルダにまとめて、`sync ./(そのフォルダ)`にする
    - include, exclude であれこれ除外するのはしんどい
    - なので、アップロードしたいものをフォルダ毎まとめて、そのフォルダ一つ指定すればいいだけにする

### include も exclude も略したらどうなる？
`include *` の扱い

> Note that, by default, all files are included. This means that providing only an --include filter will not change what files are transferred.

- デフォでは all included
- なので include だけ指定してもフィルタされないです

see: https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters

## sync するバケットに必要なバケットポリシー
- パブリックアクセスが以下のとき、
    - 新しいACLをブロック: on
    - 新しいポリシーをブロック: on
    - 任意のACLをブロック: off
    - 任意のポリシーACLをブロック: off
- ListBucket も必要ってところではまった


```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
        },
        {
            "Sid": "PublicListBucket",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME"
        }
    ]
}
```
