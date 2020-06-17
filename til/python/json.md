# Python json

## json dumps dict to string
```
option_jsondump = {
    'ensure_ascii' : False,
    'indent' : 4,
}
outstr = json.dumps(basedict, **option_jsondump)
str2file(save_filename, outstr)
```

## json で json.decoder.JSONDecodeError が出る

```
jsonstr = libutil.read_from_file(self._fullpath)
self._data = json.loads(jsonstr) # ← ここでエラーが出る
```

こんなエラー

```
  ...
  raise JSONDecodeError("Expecting value", s, err.value) from None
  json.decoder.JSONDecodeError: Expecting value: line 1 column 64 (char 63)
```

扱ってる jsonstr のフォーマットが不正なので、よく確かめること。
