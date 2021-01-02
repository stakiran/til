# 資格情報の virtualapp/didlogical って何？
- Microsoft Live 系で使っているらしい
- 使ってないなら消せばいい
- cmdkey /delete では消せないので、コンパネの資格情報マネージャーから消す
- 当該資格情報のユーザー名がマルウェアっぽい文字列だが、そうではない

[「virtualapp / didlogical」とは何ですか？](https://qastack.jp/superuser/234537/what-is-virtualappdidlogical)

> Virtualapp / Didlogicalは、Windows Live製品のいずれかを使用するときに保存される資格情報です。これには、Windows Live Messenger、Windows Live Mail、Windows Live Sign-In Assisstant、Windows XP Mode、およびその他のMicrosoftサービスが含まれます。

diary:

- 2020/12/27 消した
    - 2つとも消せば復活しない
    - インストール済の office も問題なく使える
    - 結局いつ入ったのかは不明（Live 使った覚えない
