# Windows パスワード無期限確認などユーザー情報取得系

```
$ net user username1
```

パスワード部分ならこれで

```
$ net user username1 |  findstr /i "パスワード有効"
```
