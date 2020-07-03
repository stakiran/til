# AWS ECR ECS container

## ECR と RCS
- ECR …… Elastic Container Registory
- ECS …… Elastic Container Service

## ECR
- ECS Cluster …… コンテナインスタンスの集合体
- Container Instance
    - フルマネージドな Fargate
    - 自分で頑張る EC2
- ECS Task …… 設計図
    - どんなコンテナをどんなスペックで起動するか
    - use Fragate? EC2?
    - 使うコンテナ
        - ECR の image uri を指定
- ECR Service …… クラスタ上で起動するタスク数を管理
    - k8sで言えば Task が Pod で、Service が Deployment みたいなもの？

[CircleCI + GitHub + Amazon Elastic Container Registry (Amazon ECR) + Amazon Elastic Container Service (Amazon ECS) (+ AWS Fargate) で継続的デリバリー環境を構成する | SEEDS Creators' Blog | 株式会社シーズ](https://www.seeds-std.co.jp/blog/creators/2019-09-11-201930/)
