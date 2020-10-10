# ファイル関連付け系コマンド

## Q: Windows Update 後に戻されるんですが？
- 原因不明
    - assoc や ftype の設定は生きている
    - レジストリ仕様調べたけどよーわからん
    - リロード的なコマンド調べたけどなさそう

結論

- 手動で反映してください
- あらかじめ戻したいファイルをセットでどこか置いておくと楽かも
    - gif jpg png を準備
    - 右クリ > プログラムから開く > 別のプログラムを選択 ...

## ftype で見る

指定するか、

```
$ ftype PhotoViewer.FileAssoc.Tiff
PhotoViewer.FileAssoc.Tiff=%SystemRoot%\System32\rundll32.exe "%ProgramFiles%\Windows Photo Viewer\PhotoViewer.dll", ImageView_Fullscreen %1
```

grep するのも良い

```
$ ftype | grep -i hidemaru
hidemaru.c="C:\Program Files (x86)\Hidemaru\Hidemaru.exe" %1
hidemaru.cpp="C:\Program Files (x86)\Hidemaru\Hidemaru.exe" %1
hidemaru.h="C:\Program Files (x86)\Hidemaru\Hidemaru.exe" %1
hidemaru.mac="C:\Program Files (x86)\Hidemaru\Hidemaru.exe" %1
hidemaru.txt="C:\Program Files (x86)\Hidemaru\Hidemaru.exe" %1
```

## ftype で新たな関連付けをつくる

```
$ ftype myviewer1="D:\bin\ore_ga_tukutta\myviewer1\myviewer1.exe" %1 %*
```

## Q: `%1 %*` って何？
Ans: **PATH と PATHEXT に頼る＆引数も指定して** 起動する時でも正しく動かすため

:o: 正しく動く例

```
hoge.py -h

  ↓ .py=py_auto_file -> ftype py_auto_file に従う

D:\bin1\python\python.exe %1 %*

  ↓ %1 は「関連付けを使って開かれるファイル名」
  ↓ %* は「すべてのパラメーター」

D:\bin1\python\python.exe hoge.py -h
```

:x: 正しく動かない例(ftype 設定で `%1 %*` ではなく `%*` にしていた場合)

```
hoge.py -h

  ↓ .py=py_auto_file -> ftype py_auto_file に従う

D:\bin1\python\python.exe %1

  ↓ %1 は「関連付けを使って開かれるファイル名」

D:\bin1\python\python.exe hoge.py ★ -h が渡されない！
```

## assoc で見る
:warning: `assoc .jpg` などは使わないこと（閲覧ではなく設定削除の意味になる）。

```
$ assoc | grep -i jpg
.jpg=PhotoViewer.FileAssoc.Tiff

$ assoc | grep -i png
.jpg=PhotoViewer.FileAssoc.Tiff
```

## assoc で設定する
:warning: 事前に ftype で関連付け設定をつくっておく必要がある。

```
$ assoc .jpg=myviewer1

$ assoc .png=myviewer1
```
