# Python sys.argv, GetCommandLine(), PATHEXT, PATH の関係
結論:

- sys.argv は、補われると 0 番目がファイルのフルパスになる
- GetCommandLine は、補われると「"FULLPATH_BIN" "FULLPATH_FILE"  ...」となる

```
$ python sys_argv_print.py hoge fuga 1
Raw: [python  sys_argv_print.py hoge fuga 1]
0: [sys_argv_print.py]
1: [hoge]
2: [fuga]
3: [1]

$ sys_argv_print.py hoge fuga 1
Raw: ["C:\bin1\Python27\python.exe" "C:\work2_ws\slot\python\sys_argv_print.py"  hoge fuga 1]
0: [C:\work2_ws\slot\python\sys_argv_print.py]
1: [hoge]
2: [fuga]
3: [1]

$ sys_argv_print hoge fuga 1
Raw: ["C:\bin1\Python27\python.exe" "C:\work2_ws\slot\python\sys_argv_print.py"  hoge fuga 1]
0: [C:\work2_ws\slot\python\sys_argv_print.py]
1: [hoge]
2: [fuga]
3: [1]
```
