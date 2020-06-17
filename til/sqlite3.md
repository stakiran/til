# sqlite3
チートシート: https://qiita.com/sotetsuk/items/cd2aeae4ba7e72faad47

# テーブル
テーブル一覧は .tables

# オプション

## 見る

```
sqlite> .show
        echo: off
         eqp: off
     explain: auto
     headers: off
        mode: list
   nullvalue: ""
      output: stdout
colseparator: "|"
rowseparator: "\n"
       stats: off
       width:
    filename: C:\...\places.sqlite
```

## 出力形式

```
.mode line
.mode csv
```

## 出力先
csv でやる例

```
.mode csv
.output your_output_filename.csv
```

# SQL

## n件取得
10件

```
$ select id,title,dateAdded from moz_bookmarks where folder_type is null limit 10;
```

## is null

```
$ select id,title,dateAdded from moz_bookmarks where folder_type is null;
```

# distory のワンライナー

```
sqlite3 -readonly -csv "%appdata%\\Mozilla\\Firefox\\Profiles\\{profile_name}\\places.sqlite" "SELECT title,url,last_visit_date FROM moz_places WHERE last_visit_date BETWEEN {range_start} AND {range_end};" > {target_datestr}.csv
```
