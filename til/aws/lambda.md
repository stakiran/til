# AWS Lambda 

## CloudWatch Event とタイムゾーンについて
- CloudWatch Event crontab で指定するのは UTC
- モニタリング画面で表示されるのはデフォ UTC だが、カスタムで現地タイムゾーンに切り替え可能

## いつ実行されたかを見る
モニタリング > logs insights > recent invocations

注意点:

- describe instances など何らかの aws 処理叩かないと計測されないもよう？
- 表示される timestamp を現地にしたければ右上のカスタム > UTC を現地タイムゾーンに、その後更新ボタン

## スタートアップ
- 関数 > 関数の作成
    - 関数名は適当に
    - ランタイムは boto3 叩くので python
    - 基本的な Lambda アクセス権限で新しいロールを作成

これで関数ができる。

- 基本設定 > タイムアウト > 5秒デフォは短いので15秒など適当に変える

あとはいじるだけ。

- 関数コード > lambda_function.py の中に実装していく
- 書き終えたら Save
- 実行は Test
    - 初回実行時はテストイベントの設定が出るので、
    - hello world テンプート、イベント名は適当に、中身はデフォで良い、で作成

とりあえず describe_instances 試す

- この関数の role 見に行って、describe instances の権限つける
- lambda function に実装する
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances

:point_up: ハマリポイント

- Execution results が **最新の数十件分 "のみ" しか表示しない** ので、大量に stdout する系の処理だと途中の結果が見えない