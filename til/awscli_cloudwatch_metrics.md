# AWSCLI Cloudwatch 系

## 全般
- period
    - 秒単位
    - 1分単位なら `60`
    - 1時間単位なら `3600`
    - 1440 datapoint 制約に注意

### 使える Dimension を調べる
list-metrics を使う

```
aws cloudwatch list-metrics --namespace "AWS/AutoScaling" --metric-name GroupInServiceInstances

aws cloudwatch list-metrics --namespace "AWS/RDS" --metric-name CPUUtilization
```

## 特定 AutoScalingGroup の起動個数
- 事前に有効にしておく必要がある

```
aws cloudwatch get-metric-statistics --namespace AWS/AutoScaling --metric-name GroupInServiceInstances --start-time 2021-03-01T00:00:00Z --end-time 2021-03-31T23:59:59Z --period 3600 --statistics Sum --dimensions Name=AutoScalingGroupName,Value=your-asg-name
```

## 特定 RDS の起動個数
- 直接取れるメトリクスはないので、適当なメトリクスを使う
    - メトリクス取れる≒起動している、とみなす

```
aws cloudwatch get-metric-statistics --namespace AWS/RDS --metric-name CPUUtilization --start-time 2021-03-01T00:00:00Z --end-time 2021-03-31T23:59:59Z --period 3600 --statistics Sum --dimensions Name=DBInstanceIdentifier,Value=your-db-instance-identifier
```
