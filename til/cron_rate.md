# cron rate AWS

## rate？
- AWS CloudWatch で用意してる「cron式よりもかんたんにかけるやつ」かな？

```
rate(5 minutes)
rate(5 hours)
rate(5 days)
```

ちょっとややこしいが 1 minute と 1 minutes みたいに s の有無はちゃんとしないとダメみたい（ドキュメント読んだだけ）。

- [Rate または Cron を使用したスケジュール式 - AWS Lambda](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/services-cloudwatchevents-expressions.html)
- [Schedule Expressions for Rules - Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)

