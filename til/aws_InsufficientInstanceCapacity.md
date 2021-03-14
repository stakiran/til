# InsufficientInstanceCapacity
[インスタンスの起動に関する問題のトラブルシューティング - Amazon Elastic Compute Cloud https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/troubleshooting-launch.html#troubleshooting-launch-capacity]

> 現在 AWS にはリクエストに対応するために必要とされる十分なオンデマンドキャパシティーがありません。

対処方法

- 時間を置いて起動を試してみる
- AZ やインスタンスタイプを変えて起動する
    - これ、運用上、今すぐにはできないことが多いんだよな
    - それに「どの値使えば確実に成功するか」も運ゲー感
- リクエストの粒度を下げる
    - >たとえば、15 インスタンスを起動する 1 つのリクエストを行っている場合、代わりに 5 つのインスタンスに対する 3 つのリクエストを作成するか、1 つのインスタンスに対する 15 のリクエストを作成してみてください。
- RI(Reserved Instance)を使いなさい
