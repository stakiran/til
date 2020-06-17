# Cron crontab

## チートシート
- [Cron cheatsheet](https://devhints.io/cron)
- [Cron Syntax Cheatsheet - Healthchecks.io](https://healthchecks.io/docs/cron/)
    - こっちが好き

## 2020/03/03 14:48:53 ちょっと試した
root の設定を確認

```
sudo crontab -u root -l
```

直に編集(`-e`するだけでエディタで開かれる)

```
sudo crontab -e
```

## コメント

```
# comment
```

## コマンドの書式

```
分　時　日　月　曜日　コマンド
```

```
 , 複数指定  例:0,10,20 -> 0,10,20分に実行
 - 範囲指定  例:1-5     -> 1-5分 に実行
 / 間隔指定  例:*/10    -> 10分毎に実行
```

曜日

```
月曜日    1
火曜日    2
水曜日    3
木曜日    4
金曜日    5
土曜日    6
日曜日    7 または 0
```

## crontab

```
crontab (file)
fileの内容を反映する

crontab -l
現在のcronの内容を見る

以下二つは -r でミスるのが怖いので使わないでいい。
	crontab -e
	編集
	crontab -r
	設定をクリア
```

## cronが動かない時
サービス立ち上がってる？

```
$ /etc/init.d/crond status
$ /etc/init.d/crond start
```

cronが立ち上げるコマンドには実行権限がある？

```
$ ll some-command
$ chmod 775 some-command
```

ログではちゃんと実行されてる？

- cronは実行できたかどうかしか見ない（実行先スクリプト自体のエラーには関知しないってこと）

/var/log/cron を見ろ

```
$ cat /var/log/cron
...
Sep 11 13:19:01 sun crond[1968]: (root) RELOAD (/var/spool/cron/root)
Sep 11 13:19:01 sun CROND[9974]: (root) CMD (/root/work/croncallee.sh)
...
```

実行先のエラーが知りたいなら以下のようにして標準エラー出力などをファイルに出す。

```
$ vim croncallee.sh
#!/bin/sh
python command 1>>./stdout.log 2>>./stderr.log
```

何を出すかだが、たとえば以下があるだろう。

```
$ vim croncallee.sh
pwd 1>>./cronenv.log
export 1>>./cronenv.log
pip freeze 1>>./cronenv.log
...
# ちなみにこちらで試した限りだと、
# export の結果、特に PATH に違いがある(cron は /usr/bin:/bin のように最小限)。
# pip freeze には違い無し
```

以下はよりニッチなもの

- `pwd` は使ってないよね？
    - →cronではなぜか `` 記法が使えない
- 環境変数はちゃんと定義してる？
    - terminal で定義してる環境変数は cron には引き継がれない。
    - cron から実行したスクリ内で改めて定義する必要アリ。

## cronプラクティス
ラッパーバッチを使う

```
$ cron.txt
15 * * * * /root/work/croncallee.sh
```

ファイル読み込みを使う

```
$ crontab cron.txt
```

- 手動実行する直接的な方法はない
    - from http://q.hatena.ne.jp/1248964459
- ダミースクリプトを1分起き実行にしといて、試したくなったら何か書け
- ダミースクリプトの中にsleep n秒の無限ループからcommand.sh呼び出しておいて、試したくなったらcommand.shに書け

## (実装依存だが)その他の記号
see also: https://en.wikipedia.org/wiki/Cron#CRON_expression

```
L
lastのこと。DOWで使える。
例: 5L で last friday を表す。(5=金曜日)

W
平日に最も近い日を表す。dayで使える。
例: 15W
    15日が土曜日の時は14日金曜日にあり、15日が日曜日の時は16日月曜日になる。
    一番近い平日が選ばれるというわけだ。

?
実装次第で2パターンある。
- * のエイリアス
- cron daemon の起動時間を表す
  (デーモン立ち上げと同時に実行したい場合に便利？)
```
