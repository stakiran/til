# Swagger REST WEB API

## Swagger UI で API をテストする
- Swagger UI のページにアクセスする
- try it out ボタン
    - このときパラメータがあれば入力必要
- curl や URL が発行されるので、それをコピペして実行してみる
    - たとえばブラウザアドレスバーに URL 貼り付けてみる
    - レスポンスが raw で表示されるはず

ポート転送でアクセスしている場合、このテスト用 URL が（Swagger UI とは）別ポート（デフォは 3000）なので、このポートも転送設定が必要。

## Swagger のプレビュー方法
- Swagger サーバーの Swagger Editor にアクセスすれば良い
- オンラインでいいなら https://editor.swagger.io/

## VSCode でプレビュー表示する
- Swagger Viewer
- インストール後、YAML プラグインが有効でないならリロード再起動走る

プレビュー

- yaml 開いて
- preview swagger コマンド
