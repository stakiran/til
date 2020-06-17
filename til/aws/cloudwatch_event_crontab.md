# CloudWatch Event の crontab 書式
- かんたん: [Rate または Cron を使用したスケジュール式 - AWS Lambda](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html)
- 詳細: [Schedule Expressions for Rules - Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)

```
cron(Minutes Hours Day-of-month Month Day-of-week Year)
```

> 日または週日の値は疑問符である必要があります (?)。 

もっというとこう:

- 曜日のワイルドカードは `?`
- 曜日がワイルドカードでない時は、日のワイルドカードも `?`
