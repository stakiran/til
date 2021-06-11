# aws s3

## sync

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

同期の挙動について

- exclude に基づいて同期されるわけではない
    - exclude `node_module/*` したからといって、既にアップロードされた `node_modules/*` が削除されるわけではない
    - include/exclude は **これからアップロードしようとしてるファイル達のうち、どれを選ぶか選ばないか** を指定しているにすぎない
- Q: じゃあミラーリングはどうやる？
    - ローカル側に存在しないファイルを消したい場合は、`--delete` をつける

ベストプラクティス

- アップロードしたいものは1フォルダにまとめて、`sync ./(そのフォルダ)`にする
    - include, exclude であれこれ除外するのはしんどい
    - なので、アップロードしたいものをフォルダ毎まとめて、そのフォルダ一つ指定すればいいだけにする

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
