# AWS CloudWatch Event

## Cron式
- 指定は UTC 基準
- 日本時間(JST)で 22 時にしたければ、UTC では -9 時間なので 13 を指定。
    - `0 13 * * ? *`

[ルールのスケジュール式 - Amazon CloudWatch Events](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/events/ScheduledEvents.html)

```
8:30
cron(30 23 * * ? *)

8:30 平日のみ
cron(30 23 ? * MON-FRI *)
```

## Cron式の動作を確認したい
- CloudWatch > イベント > ルールから新規して、Cron式のカッコの中身を貼り付ける（と直近いつ発火するかが7回分くらいまで出る）
- EventBridge 画面では出ない
