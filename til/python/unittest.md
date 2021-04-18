# Python unittest ユニットテスト

## ●基本テンプレ

```
# -*- coding: utf-8 -*-

import datetime

import unittest

import YOUR-TESTEE-MODULE as ALIAS

class TestHelper(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lines(self):
        ...
        actual_lines = ALIAS.getLines()

        self.assertEqual(expect_lines, actual_lines)

if __name__ == '__main__':
    unittest.main()
```

## 例外を投げる

```
        with self.assertRaises(RuntimeError):
            state.is_in_code_block()
```

## list の assert
assertEqual() に渡すだけでいける。

## datetime.datetime.today() の結果を固定するモック
- unittest.mock を使う系はうまくいかなかった
    - ビルトインモジュールは mock でも上書きできない
- なので単純に継承してオーバーライド + datetime.datetimeをオーバーライドした側に変える、で


```
import datetime

class datetime_FixedToday(datetime.datetime):
    @classmethod
    def today(cls):
        return cls(2020, 4, 1, 12, 34, 56)
datetime.datetime = datetime_FixedToday
```

