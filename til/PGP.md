# PGP Pretty Good Privacy
[1分でわかるPGP - 村川猛彦](http://web.wakayama-u.ac.jp/~takehiko/pgp.html)

- 米国 Philip Zimmermann 開発の暗号化ソフトウェアおよびそのアルゴリズム
    - アルゴリズムは RFC で公開されてる
    - GnuPG という OSS は上記からつくられてる(gpgコマンド)
        - Git for windows にもついてた
- 全般
    - ファイルやメールを暗号化するのに使う
    - 鍵使う
    - 鍵は当事者たちが自己管理する
    - 秘密鍵はパスフレーズ設定してくださいね(でないと秘密鍵漏れたらおしまいなんで)
- 図はよくわからん

> メッセージまたはファイルは，セッション鍵と呼ばれる乱数の値を鍵として，対称暗号により暗号化され，そのセッション鍵は，受信者の公開鍵で暗号化されます．

- 解読する
- 登場人物
    - ファイル
    - セッション鍵(乱数の値)
    - 対称暗号(共通鍵暗号)
    - 受信者の公開鍵と秘密鍵
- step
    - send
        - 1: 送りたいファイルを、共通鍵暗号 with 乱数値で暗号化する
        - 2: 乱数値を、受信者の公開鍵で暗号化する
        - 3: 暗号化された乱数とファイルを送る
    - receive
        - 1: もらった暗号(乱数)を、秘密鍵で復号する → 乱数値が得られる
        - 2: もらった暗号(ファイル)を、共通鍵暗号 with 1で得た乱数値で復号する → ファイルが得られる
- なんか2回暗号化してるけどなんで？
    - 安全性を「受信者が持ってる秘密鍵の管理次第」に帰着させたいから
