# xlrd
- [Python の xlrd ライブラリを用いて Excel ファイルのシート内容を Markdown に落とす - stamemo](https://stakiran.hatenablog.com/entry/2018/06/26/212020)
- https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.get_rows
- https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell

## 単位
- book
- sheet
- row
- cell

## ざっくりパース

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
