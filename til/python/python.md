# Python

## datetime object を n 日ずらす
timedelta つくって足してやる。days=-1 でもいける。

```python
def today_datetimestr_short_with_dow(days=0):
    todaydt = datetime.datetime.today()
    if days!=0:
        delta = datetime.timedelta(days=days)
        todaydt += delta
    datestr = todaydt.strftime('%y%m%d')
    ...
```

## datetime dow 曜日計算

```python
def today_datetimestr():
    todaydt = datetime.datetime.today()
    datestr = todaydt.strftime('%Y/%m/%d')

    wd =  todaydt.weekday()
    dow_j = ['月',"火", "水", "木","金","土","日"][wd]
    dow_e = ['Mon',"Tue","Wed","Thu","Fri","Sat","Sun"][wd]

    return '# {}({})'.format(datestr, dow_e)

```

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

## sort は破壊的, sorted は複製
ls.sort()

newls = sorted(ls)

## [obj1, obj2, ...] をソートする sort
key に「各要素の何を使って何をする」的な比較処理関数を置く。

```
newlist = sorted(baselist, key=lambda elm:elm.timestamp)
```

## ユーザー定義例外 exception

```
class Error_SomethingFailed(Exception):
    pass
```

```
raise Error_SomethingFailed('details')
```


## dict keyerror キーの存在確認

```
if k in d:
    v = d[k]
    print(v)
```

## string to char list

```
s = 'abcde'
for c in s:
    print(c)
```

## configparser > section methods

```
['_MutableMapping__marker', '__abstractmethods__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_name', '_options', '_parser', 'clear', 'get', 'getboolean', 'getfloat', 'getint', 'items', 'keys', 'name', 'parser', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

## オブジェクトの関数判定 function type
callable(obj)

## ファイルの最終更新日時をナノで取得 stime access modifi last

```
def get_lastmodified_nanotime(filename):
    stat_result = os.stat('edita.temp')
    return stat_result.st_mtime_ns
```

## datetime unixtime microsecond
ライブラリとして用意されてないので泥臭く。

```
def dt2unixtime_micro(dt):
    unixtime_second = time.mktime(dt.timetuple())
    unixtime_micro_str = '{}000000'.format(int(unixtime_second))
    unixtime_micro = int(unixtime_micro_str)
    return unixtime_micro

def unixtime_micro_str2dt(unixtime_micro_str):
    unixtime_second = int(unixtime_micro_str[:-6])
    dt = datetime.datetime.fromtimestamp(unixtime_second)
    return dt
```

## 四捨五入
round(11.333, 1)

11.3 になる。第二位を四捨五入。

## list で n 個の要素からなるリストを新規作成

```
# [0, 0, ...]
array_with_30_elements = [0]*30
```

## range で逆順に生成する

```
>>> print(list(range(12-1, -1, -1)))
[11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
