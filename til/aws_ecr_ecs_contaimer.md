# AWS ECR ECS container

## 基礎用語整理
そもそもプレーンを理解する

- Data plane …… コンテナが動く場所
    - Fargate or EC2
- Control plane …… コンテナを管理する場所
    - ECS or EKS

ECS

- Elastic Container Service

ECR

- Elastic Container Registory
- コンテナイメージのレジストリ

Fargate

- EC2 部分を隠蔽するデータプレーンサービス
- EC2 を意識する必要がなくなる(マネコンにもEC2インスタンスが現れない)
- Q: お高い？
    - yes
- Q: Lambda との違いは？
    - まあサーバーレスとフルマネコンテナの違い
    - 一般的に軽い処理なら lambda、それ以上なら fargate
    - see: [Fargate VS Lambda 両者の違いをスタートアップCTOが本気で考えてみた！ | Ragate ブログ](https://www.ragate.co.jp/blog/articles/1566)

EKC

- AWS フルマネの k8s

Task Definition と service

- 1 つ以上の Container Config
- Container Config の例
    - どの docker image を使うか
    - どのポートを晒すか
    - cpu やメモリ
    - ログ記録方法
    - 環境変数
- この定義をインスタンス化すると service になる

cluster と instance

- Cluster
    - ECS Container Instance(DockerやAgentを持ったEC2)
    - ECS Container Instance(DockerやAgentを持ったEC2)
        - task
        - task

service と task と container

- service
    - task
    - task
        - container
        - container

cluster と service

- service に含まれる task は、**複数の instance にまたがって配置＆実行される**

参考:

- [amazon ecs - What is the difference between a task and a service in AWS ECS? - Stack Overflow](https://stackoverflow.com/questions/42960678/what-is-the-difference-between-a-task-and-a-service-in-aws-ecs)
- [AWS コンテナサービス「Fargate」「ECS」「EKS」の違いを解説 - サーバー構築と設定 ～初心者にも分かりやすく解説～](https://xn--o9j8h1c9hb5756dt0ua226amc1a.com/?p=2025)
