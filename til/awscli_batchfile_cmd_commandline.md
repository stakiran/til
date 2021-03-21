# AWSCLIをバッチファイルから使う場合
- aws コマンドで実行が終了してしまう問題に遭遇することがある
    - バッチファイルの仕様、よくわからん……
    - node.js 系のコマンドでも起きてた気がする……
- 対処法
    - call で呼び出すようにする

```bat
set commandline=aws ce get-cost-and-usage --time-period ……
call %commandline%
```

