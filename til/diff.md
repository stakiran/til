# diff コマンド

## 一般的に
left（before）の行（範囲）に、Operationの操作をした結果、right（after）の行（範囲）になった

```
(left-target-line)(operation)(right-target-line)
(before)
---
(after)

operationはc(Changed), d(Deleted), a(Add)などがある
```

- d の場合は before と区切り線が丸々省略される
