# xlrd
- [Python の xlrd ライブラリを用いて Excel ファイルのシート内容を Markdown に落とす - stamemo](https://stakiran.hatenablog.com/entry/2018/06/26/212020)
- https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.get_rows
- https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell

## get_rows() の値をスライスすると 'generator' object is not subscriptable
いったんリストに変更する

```
rows = sheet.get_rows()
rows_by_list = list(rows) # rows は generator で slice できないので、いったん list にする
row_itemnames = rows_by_list[4]
```

## xlrd.biffh.XLRDError: Can't find workbook in OLE2 compound document
- Excel ファイルにパスワードがかかっている
- IRM 化されている

前者の場合、パスワードを投入する処理も書けるみたいだからググること。

後者はぐぐっても解得られなかった。Excel 側で IRM 解除するしかない。ちなみに「プログラムを使用してブックにアクセスする」は Excel 内マクロからアクセスできるようにするって話なので関係ない。

## 単位
- book
- sheet
- row
- cell

## ざっくりパース

### v2 コマンドとして使えるもの
文字列値が入ってるセルを列挙する例

```
# encoding: utf-8

from decimal import *
import json
import os
import sys

import xlrd

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)

def get_sheet_object(filename, sheet_index_with_zero_origin):
    ''' @return [sheetobj, debugobj] '''
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(sheet_index_with_zero_origin)

    debugobj = {
        'sheet_count' : book.nsheets,
        'sheet_names' : book.sheet_names()
    }
    return sheet, debugobj

def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-i', '--input', default='xxxxx.xlsm')
    parser.add_argument('-n', '--sheetindex', default=0, type=int)

    args = parser.parse_args()
    return args

args = parse_arguments()

src_filename = args.input
src_fullpath = os.path.join(MYDIR, src_filename)
sheet_index = args.sheetindex

sheet, info = get_sheet_object(src_fullpath, sheet_index)
print(info)

rows = sheet.get_rows()
rows_by_list = list(rows) # rows は generator で slice できないので list にする

for idx_y,row in enumerate(rows_by_list):
    cells = row
    for idx_x,cell in enumerate(cells):
        v = cell.value
        if isinstance(v, int):
            continue
        if isinstance(v, float):
            continue
        if v.strip() == '':
            continue
        print('({},{})'.format(idx_x, idx_y))
        print(v)
```

使い方:

```
$ python parseexcel.py

$ python parseexcel.py -i hogehoge.xlms

$ set TARGET_SHEET_INDEX = 3
$ python parseexcel.py -i hogehoge.xlms -n %TARGET_SHEET_INDEX%
```

### v1
```python
def zero_origin(idx):
    return idx-1

def get_sheet_object(filename, sheet_index_with_zero_origin):
    ''' @return [sheetobj, debugobj] '''
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(sheet_index_with_zero_origin)

    debugobj = {
        'sheet_count' : book.nsheets,
        'sheet_names' : book.sheet_names()
    }
    return sheet, debugobj

sheet, _ = get_sheet_object(target_fullpath, zero_origin(TARGET_SHEET_INDEX))
rows = sheet.get_rows()
```

- rows は [row, row, ……]
- row は [cell, cell, ……]
- cell は cell.value を持つ

## その他の選択肢
[PythonでExcelファイルを扱うライブラリの比較 | note.nkmk.me](https://note.nkmk.me/python-excel-library/)

- xlrd：pandas使うまでもない場合
- xlwt：xlsファイル読みたいなら
- openpyxl：excelファイルの書式保ったままいじりたいなら
- pandas：データ分析したいなら
