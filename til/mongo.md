# Mongo Shell

## ●関係
- database
    - collection
        - document

## ログイン

```
mongo -u username -p password
```

## DB とコレクション確認

```
show dbs
```

```
use (DB名)
show collections
```

## コレクションの中身

```
use (DB名)
db.(Collection名).find()
```

use はデータベースの新規作成も兼ねている。

### 指定キーだけ表示する

```
db.collectionXYZ.find({}, {keyname:1})
```

### pretty print

```
db.collectionXYZ.find({}, {keyname:1}).pretty()
```

## ファイルにも出力したい
mongo shell コマンドの段階で tee する。

```
$ mongo -u …… | tee output.txt
```
