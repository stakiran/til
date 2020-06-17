# 環境変数 env var

#E export 環境変数 グローバル global 変えるには？
コマンドではできない。

- bashrc やら /etc/profile ← こういうやつの定義を修正
- source コマンドでリロード

[How to permanently export a variable in Linux? - Stack Overflow](https://stackoverflow.com/questions/13046624/how-to-permanently-export-a-variable-in-linux)

## set env var 環境変数
ローカルは `varname=value`

子プロセスにも引き継がせたいなら `export varname=value`

確認は `set`
