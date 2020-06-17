# Python string format

## format に dict を指定する

### 2 こっちが簡単かも dict じゃないが

```
print('{year}年{month}月{day}日'.format(year=2018, month=1, day=11))
# 2018年1月11日
```

### 1 引数にdictを与えるパターン

```
d = {
  "k1" : "test",
  "k2" : 123
}
s = '{0[k1]} {0[k2]:05d}'.format(d)
print(s)
```

test 00123


## keyword dict で

```
commandline_template = 'sqlite3 -readonly -csv "%appdata%\\Mozilla\\Firefox\\Profiles\\{profile_name}\\places.sqlite" "SELECT title,url,last_visit_date FROM moz_places WHERE last_visit_date BETWEEN {range_start} AND {range_end};"'
commandline_params = {
    'profile_name' : profile_name,
    'range_start' : ut_start,
    'range_end' : ut_end,
}
commandline = commandline_template.format(commandline_params)
```

## % 使うやつ

```
'%s %02d' % (str1, int1)

↓

'{:} {:02d}'.format(str1, int1)
```

ただし int1 が int 以外の型だと Unknown format code 'd' for object of type ... が出る

## なぜか KeyError が出る

```
jsonstr = '{"property":{"etag":"{:}"},"body":{:}}'.format(etag, bodytext)
```

format構文が {} に特別な意味もたせてる。jsonstr みたいに {} を持つ文字列をそのまま読み込ませると死ぬ。

from https://stackoverflow.com/questions/2755201/str-format-raises-keyerror
