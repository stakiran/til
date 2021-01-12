# AWS ALB application load balancer

## 概念
- alb
    - target group...
        - port
        - protocol
        - target...
            - name
            - type(instance or ipaddr or lambdafunction)
            - tags
    - listener...
        - port
        - protocol
        - default action
        - listener rule...
            - 優先度 prio
            - 処理 action
                - どこに: target group の arn
                - どうするか: forward、redirect、fixed-response
            - 条件 condition(host-header、http-request-method、path-pattern、source-ip……http-header、query-string)

つまり？

- [Application Load Balancer のターゲットグループ - Elastic Load Balancing](https://docs.aws.amazon.com/ja_jp/elasticloadbalancing/latest/application/load-balancer-target-groups.html)
- ルールの条件が満たされると、トラフィックが「該当するターゲットグループ」に転送されます。
    - ルールで判定して、
    - ターゲットグループに転送する

プロトコルとポート

- target group
- listener
- ★両方に設定できるんだけどどういうこと？
