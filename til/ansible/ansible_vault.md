# ansible vault

## ansible-vault encrypt_string で `!` を使うと event not found
- :x: `ansible-vault encrypt_string 'pass\!word'`
- :o: `ansible-vault encrypt_string 'pass\!word'`

bash の仕様で **ダブルクォートの中に `!hoge` があると history 機能が働くらしい** ので **シングルクォートを使う** こと。

see [can not encrypt some password · Issue #47842 · ansible/ansible](https://github.com/ansible/ansible/issues/47842)

## 文字列単位の暗号化と復号化
指定文字列を暗号化する。（Vault password は `ope`）

```
$ ansible-vault encrypt_string "pass\!word"
New Vault password:
Confirm New Vault password:
!vault |
          $ANSIBLE_VAULT;1.1;AES256
          62326134303236353037313335366136343732313535343835623364343439343732613461373739
          3934623666383531353061663137633535616662336664640a363264326139663037613134363732
          64346333666463666638393936333364353634613234623239376432396261643162623338373236
          3935343862633730340a326630333335646438333866656539366135663261363866623562366532
          3663
Encryption successful
```

暗号化が正しいか復号する。

「ファイルに書いた暗号化文字列」しか復号できないので、以下のように。

```
$ vi vaulttest.yml
var1: ★ここに貼り付ける★
$ cat vaulttest.yml
var1: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          62326134303236353037313335366136343732313535343835623364343439343732613461373739
          3934623666383531353061663137633535616662336664640a363264326139663037613134363732
          64346333666463666638393936333364353634613234623239376432396261643162623338373236
          3935343862633730340a326630333335646438333866656539366135663261363866623562366532
          3663
```

復号してみる

```
$ ansible localhost -m debug -a var="vars.var1" -e "@vaulttest.yml" --ask-vault-pass
Vault password:
[WARNING]: No inventory was parsed, only implicit localhost is available

localhost | SUCCESS => {
    "vars.var1": "pass\\!word"
}
```

ハマリポイント

- `vars.var1` のように `vars.` で始めないといけない
    - ~~`var1` でもいけるかも~~ `var1` でオッケーです
    - `var1` あるいは `vars.vars.var1`
        - see: [Ansible 変数名が「vars」の場合の変数参照の仕方について - Qiita](https://qiita.com/answer_d/items/a1c28f4c664934bd03b3)
        - ややこしい（varsがシステム定義でこの中に定義された変数が並ぶという仕様）
- `vaulttest.yml` ではダメで先頭に `@` が必要
