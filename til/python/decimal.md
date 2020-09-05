# Python decimal

## 他形式への変換
普通に str()、float()、int() などで囲ってやればいい。

事例:

- TypeError: sequence item 1: expected str instance, decimal.Decimal found
    - join で与えるリスト内要素は str 必須だが、decimal になっていた
    - str にすれば ok
