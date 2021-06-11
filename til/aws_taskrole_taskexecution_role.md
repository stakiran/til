# ECSのタスクロールとタスク実行ロール

## タスクロール
- コンテナ内で動かしてるアプリに付与する権限
    - アプリに AWSCLI や AWSSDK を叩かせたい場合など
- 叩く必要がないなら「なし」でいい

## タスク実行ロール
- 中核機能(ECSコンテナエージェントとDockerデーモン)に付与する権限
    - つまり中核機能に A をさせたい場合, A に必要なポリシーをつけておく必要がある
- 基本的にマネジメントロール ecsTaskExecutionRole で事足りる
    - このロールには「ECR への push」「CloudWatch Logsへのアップロード」などよく使う権限が集められている
- ecsTaskExecutionRole で足りない場合、各自で追加してください

Q: 足りない場合って？

- たとえば「Secrets Manager に保存された DB password」を「コンテナ定義パラメーターの Secrets」で取得する場合
    - `secretsmanager:GetSecretValue"` と `kms:Decrypt` が要る
- see: 
    - [Amazon ECS タスク実行 IAM ロール - Amazon Elastic Container Service https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_execution_IAM_role.html#task-execution-secrets]
    - [タスク定義パラメータ - Amazon Elastic Container Service https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definitions]
