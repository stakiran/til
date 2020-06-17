# Taraterm マクロ
[MACRO Help Index](https://ttssh2.osdn.jp/manual/4/ja/macro/)

## チュートリアル
- 文字列変数定義時は "" で囲む
- 参照時は "" か変数名を列挙する
    - **その際、space は自動でつかないので sp 変数使うなどして見やすく

```
prm1="i-xxxxxxxx"
prm2="i-ssssssss"
sp=" "
sendln "echo" sp prm1 sp prm2
end
```

## バッチファイルベースで使うには
ttermpro.exe に `/M=%~dp0macro_test.ttl` みたいにして与える

- 絶対パスじゃないと exe の相対パスになるので注意

macro_test.ttl

```
msgbody="Teratermウィンドウ側のログインが完了した後、OK ボタンを押してください"
msgtitle="操作指示"
messagebox msgbody msgtitle

sendln 'ls -la'
end
```

ポイント

- マクロはteratermウィンドウに対してあれこれ操作する形になるので、**ちゃんと teraterm 側がログインされた状態を担保してから** 次に進む必要アリ
    - 案1: 上記みたいにユーザーに OK 押してもらう
    - 案2: ttl に connect 命令使って繋ぐ処理を書く
        - まだ試してない
        - これすると ttermpro.exe では /M だけ渡して、実際の接続は全部 ttl の connect 処理に書くことになるはず
        - 個人的には好きじゃない（バッチファイルで書いた or バッチファイルに渡されるパラメータを持ってこれない）
        - :memo: TTPMACRO.exe を直に呼び出すようにすればいけそう(普通にコマンドラインとしてパラメータ渡せる＆ttlからは param2, param3,... でアクセスできる模様)
