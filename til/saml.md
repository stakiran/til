# SAML Security Assertion Markup Language

## 基礎概念
参考:

- [SAML認証を勉強せずに理解したい私から勉強せずに理解したい私へ - Qiita](https://qiita.com/khsk/items/10a136bded197272094a)
- [やさしい言葉で理解するSAML認証のまとめ - Qiita](https://qiita.com/pasta_kun/items/4a57bd3b71ac8bf5d736)

要点

- SSO を実現するために使われてる技術の一つ
- 技術というか標準規格
- というかXML形式の仕様
    - ユーザの認証情報をXML形式で記述したもの
- この規格に従えば、A 社と B 社とで SSO を実現できる

人物

- SP
    - Service Provider。認証使いたいWebサービス
- Idp
    - Identity Provider。認証を提供する側
- SP「うちにログインしてもらうのに、Idpさんとこの認証情報使いたいんですけど」
- Qiita「GitHubアカウントでうちにログインできるようにしたいんですけど」
    - Qiita が SP
    - GitHub が Idp
    - (まあ実際、QiitaはSAMLではなくOAuth使ってるだが)

SP-initiated SAML

- User > SP > Idp
- User を Idp にリダイレクトして、そこで認証
- User に渡された「認証応答」を、SPが、Idpの秘密鍵で検証することで認証になる

IdP-initiated SAML

- SP-initiated と全体的な流れは同じ
- SP-initiated は、始まりが「User が SP にアクセスする」「SP が Idp に、User をリダイレクトする」
- Idp-initiated は「Idp が User に認証せいとリクエストする」「認証応答を User が SP に渡す」

OpenID との違い

- 利用者側に選択させることなく SSO を実現する

