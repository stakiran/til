# タスクスケジューラー
`control schedtasks` が早い。

## 定期的に実行する処理を登録したい
- `\` にでも新しくつくる
- トリガー例
    - 毎日 hh:mm 時に起動、n分毎に繰り返し、無期限
- 操作
    - プログラムの開始
    - **処理したい内容を書いたバッチファイル** のフルパスを指定
- 全般 > **ユーザーがログオンしているかどうかにかかわらず実行する** を選ぶ
    - :memo: これしないと実行ごとに DOS 窓出て邪魔くさい
    - → [タスクスケジューラに登録したバッチがうまく実行できない時に確認すること](http://sogohiroaki.sblo.jp/article/178281845.html)

