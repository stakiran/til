# AWSCLI log

## create
- loggroup, stream, event
    - groupとstream
        - 成功すると何もoutput出さない
        - 重複だとエラーで停止する
- event は最初の一回以降は全部 token からやる
- event の timestamp は unixtime の **ミリ秒**
    - unixtime 自体は秒なのでこれでやっちゃうと `tooOldLogEventEndIndex` エラーで怒られる

```
$ aws logs create-log-group --log-group-name group1

$ aws logs create-log-stream --log-group-name group1 --log-stream-name stream1

$ h putlogevent1.json
[
  {
    "timestamp": 1634799714000,
    "message": "event1"
  }
]

$ aws logs put-log-events --log-group-name group1 --log-stream-name stream1 --log-events file://putlogevent1.json
{
    "nextSequenceToken": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

$ aws logs put-log-events --log-group-name group1 --log-stream-name stream1 --log-events file://putlogevent2.json --sequence-token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
{
    "nextSequenceToken": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
}
```
