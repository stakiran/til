# hosts ファイル編集
- C:\Windows\System32\drivers\etc
    - 管理者権限必要
- `192.168.1.1 hostXYZ`
    - ipaddr, hostname の順

修正したら即時反映されるはず。

ダメなら ipconfig /flushdns などいろんな手順試す（ネットで調べて）（このコマンドも管理者権限必要）

デバッグには `ipconfig /displaydns` が良い。ちゃんと認識されてれば一覧に出る。
