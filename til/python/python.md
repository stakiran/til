# Python

## 関連付けで開く

```py
def open_file_with_assoc(filepath):
    # - ブロッキングを防ぐために start 経由で開く
    # - 関連付けはファイルパスを指定するだけで開けるので
    #   プログラム名は指定しない
    os.system('start "" "{}"'.format(filepath))
```

## windows ファイル名に使えない無効文字 invalid char をなくす 

```py
    @staticmethod
    def remove_invalid_char_based_on_hidemaruscb(filename):
        # from https://github.com/stakiran/hidemaru_scb/blob/master/scb_new_or_open.mac#L157
        after = filename
        afterchar = '_'
        after = after.replace('\\', afterchar)
        after = after.replace('/', afterchar)
        after = after.replace(':', afterchar)
        after = after.replace('*', afterchar)
        after = after.replace('?', afterchar)
        after = after.replace('\"', afterchar)
        after = after.replace('>', afterchar)
        after = after.replace('<', afterchar)
        after = after.replace('|', afterchar)
        after = after.replace(' ', afterchar)
        return after
```

## 正規表現 日付時刻やリンク文字列 マッチ
- findall で n 回分のマッチを全部拾える
- マッチするとキャプチャごとに分かれてタプルで格納される

```py
RE_LINK_ANOTHER_PAGE = re.compile(r'\[([^\-\*/])(.+?)\]([^\(]|$)')
def get_linked_filename(line):
    # '[動揺日記]'
    #   |
    #   V
    # [('動', '揺日記', '')]
    #
    # キャプチャの都合上、こんな風に \1 \2 \3 でマッチする
    NO_FILENAME = ''

    matched_all = re.findall(RE_LINK_ANOTHER_PAGE, line)
    is_empty = len(matched_all)==0
    if is_empty:
        return NO_FILENAME

    # findall なので [...] が n 個あっても検出できるが
    # まだテストしてない＆想定もしてないので、1 個だけ書いてあるとみなす
    matched = matched_all[0]

    filename = f'{matched[0]}{matched[1]}.scb'
    filename = Util.remove_invalid_char_based_on_hidemaruscb(filename)
    return filename

RE_DATE_STRING = re.compile(r'(20[0-9]{2})\/([0-9]{2})\/([0-9]{2})')
def get_datetime_strings(line):
    NOT_MATCHED = ''

    matched_all = re.findall(RE_DATE_STRING, line)
    is_empty = len(matched_all)==0
    if is_empty:
        return NOT_MATCHED

    datestrs = []
    for matched in matched_all:
        datestr = f'{matched[0]}/{matched[1]}/{matched[2]}'
        datestrs.append(datestr)

    return datestrs
```

## file markdown list glob

```
def get_markdown_filenames_only_currentlevel(fullpath_of_directory):
    query = '{}/*.md'.format(fullpath_of_directory)
    fullpaths = glob.glob(query, recursive=False)

    filenames = []
    for fullpath in fullpaths:
        filename = get_filename(fullpath)
        filenames.append(filename)
    return filenames
```

## datetimestr

```py
def today_datetimestr():
    todaydt = datetime.datetime.today()
    dtstr = todaydt.strftime('%Y%m%d_%H%M%S')
    return dtstr
```

## csv read

```py
def csvfile2csvobj(filepath, encoding='utf8'):
    csv_file = open(filepath, 'r', encoding=encoding, errors='', newline='' )
    reader = csv.reader(csv_file, delimiter=',')
    return reader

fullpath = os.path.join(rootdir, targetfilename)
reader = csvfile2csvobj(fullpath, encoding='cp932')

for i,row in enumerate(reader):
    if i==0:
        continue
    code = row[1]
    name = row[2]

    not_found = not code in pj_dict
    if not_found:
        pj_dict[code] = {}
    cur = pj_dict[code]
    cur['name'] = name

```

## list の指定位置に list を insert する
- extend は list の append なので違う
- かといってスライスをn個使って器用に入れ込む関数もつくりたくない
- `[i:i]` でいけるの知らなかった

```py
list1[i:i] = list2
```

see: [python - How to insert multiple elements into a list? - Stack Overflow](https://stackoverflow.com/questions/39541370/how-to-insert-multiple-elements-into-a-list)

## datetime YYYY-MM や YYYY-MM-DD 文字列つくる系

```python
def today_datetimeobj():
    return datetime.datetime.today()

def walked_datetimeobj(days):
    dt = today_datetimeobj()
    delta = datetime.timedelta(days=days)
    dt += delta
    return dt

def datetimeobj2datestr(datetimeobj):
    return datetimeobj.strftime('%Y-%m-%d')

def yesterday_str():
    dt = walked_datetimeobj(days=-1)
    s = datetimeobj2datestr(dt)
    return s

def enumerate_datetimestr_in_month(datestr):
    """ @param datestr must be YYYY-MM format.
    - 当月1日から始めて +1 日しながら追加していく
    - 次月になった = おしまいなので抜ける. """
    y, m = datestr.split('-')
    y = int(y)
    m = int(m)

    delta_1day = datetime.timedelta(days=1)
    basedt = datetime.datetime(year=y, month=m, day=1)
    dt = basedt
    this_month = m

    lines = []
    while True:
        datetimestr = datetimeobj2datestr(dt)
        lines.append(datetimestr)
        dt += delta_1day

        is_over_this_month = dt.month != this_month
        if is_over_this_month:
            break

    return lines
```

## csv 出力
- 1行1要素で出力する
- 1要素がn要素リストの場合、n列にする
    - n=1の場合、csvモジュールがエラーを吐くので明示的に「1要素からなるリスト」にする必要がある

```py
import csv

def list2csv(filepath, ls):
    with open(filepath,  encoding='utf8', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')

        for element in ls:
            is_not_element_list = not isinstance(element, list)
            if is_not_element_list:
                element = [element]
            writer.writerow(element)
```

## パスワードポリシー突破
必要な文字をランダムに1文字ずつつくる

```py
import secrets
import string

def generate_alnumark():
    alphabet = secrets.choice(string.ascii_letters)
    number = secrets.choice(string.digits)
    mark = secrets.choice(string.punctuation)

    s = '{}{}{}'.format(alphabet, number, mark)
    return s
```

## パスワードをつくるセキュリティ用乱数モジュール
- secrets モジュールを使う
- random はセキュリティゆるいので使わない
- 文字列候補は string モジュールの定義を拝借すると楽

```py
import secrets

using_chars = '{}{}'.format(
    string.ascii_letters,
    string.digits,
)
def generate_password(length):
    ls = [secrets.choice(using_chars) for _ in range(length)]
    s = ''.join(ls)
    return s
```

## 端から指定文字列を消したい場合は strip 系はダメ
- strip, lstrip, rstrip は文字単位で探して消す挙動
- lstrip('abc')
    - :x: abc を探して消す
    - :o: a を探して消す、bを探して消す……
- ゆえに意図した結果にならない
- 意図した結果がしたいなら、replace('abc') を
    - まあ abc が端以外にも含まれてたら詰むが
    - そこは適当に工夫して

[今まで勘違いしていたPythonの.strip(), .lstrip(), .rstrip() - Qiita](https://qiita.com/github-nakasho/items/aef2f3b0024f97a1e216)

## unixtime to datetime

```py
def create_datetime_from_unixtime(number):
    return datetime.datetime.fromtimestamp(number)
```

## json alias, loads dumps kwargs

```
def jsonstr2dict(s):
    return json.loads(s)

def dict2str(d, **kwargs):
    return json.dumps(d, **kwargs)
```

## getattr リフレクション グローバルに定義した関数名を使いたい場合は？
globals() とか locals() でリーチできる。

```
def globalfunc1(var):
  print(var)

def refrection_test():
  funcname = 'globalfunc1'
  f = globals()[funcname]
  f('yeah!')

```

## 式を複数行に分けて書く

```
a = 1.0 \
+ 2.1 \
+ 3.3
print(a)
```

行末に `\` つけて続きあることを示す。

## sha256 ハッシュ

```python
def hash(s):
    import hashlib

    unicode_string = s
    byte_string = s.encode('utf-8')

    hashed_str = hashlib.sha256(byte_string).hexdigest()
    return hashed_str
```

## 日本語変数名も使用可能

### 活用例: Excel 製のアンケート項目から計算プログラムをつくる
Excel からコピペした項目名をそのまま変数として使う感じ

筆者事例1

- `私は～～のためなら～～するべきだと考えている` ← こういう項目が100以上ある
- 全部変数名（メンバ変数名）に落とす必要がある
- 英語名考えて打つのしんどくない？
- コピペした日本語項目名をそのまま変数にする感じでプログラミングしちゃろ ← こっちの方が楽だった

## float 浮動小数点 計算 精度が Excel と合わない
- decimal ライブラリを使う
- float は内部的に 2 進数なので精度ガバガバ

```
Type "help", "copyright", "credits" or "license" for more information.
>>> from decimal import *
>>> print(Decimal(1)/Decimal(3))
0.3333333333333333333333333333
```

数全部 Decimal で囲ってあげれば良い感じ。

### xlrd との兼ね合い
- 文字列にするときは str ではなく repl にする
- 文字列にしたい場合に、Decimal を使う必要はない

参考: [精度を失うことなくPython FloatをStringに変換する](http://www.366service.com/jp/qa/6a6dd6759e1fcc8d55abd8b7aced14da)

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

## dict の sort
- items() に対してソートする
- item は (key, value) タプル

```
    # 慣れないのでメモ
    # - 辞書のソートは items() ベースじゃないとできない
    # - items() は「(key, value) の tuple」から成るリスト
    #
    # item を print してみるとこうなってる
    #   ('今日のタスク(実行中)', {'count': 1})
    #   ('--- 明日以降のタスク hold:1', {'count': 1})
    #   ('明日のタスク', {'count': 3})
    ranking_asc_sorted_items = sorted(
        ranking_dict.items(),
        key=lambda item:item[1]['count']
    )
    ranking_desc_sorted_items = reversed(ranking_asc_sorted_items)

    for item in ranking_desc_sorted_items:
        taskname, count = item[0], item[1]['count']
        print('- {}: {}'.format(count, taskname))
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

## 四捨五入 round
round(11.333, 1)

11.3 になる。第二位を四捨五入。

round(floatv) で floatvの小数点第一位を四捨五入。結果はintになる。

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
