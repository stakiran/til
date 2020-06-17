# VBS VBA WHS 学習ノート

```
■実行中に中断する文
Stop

■assert
Debug.Assert 式

引っかかった場合はブレークポイント置かれたみたいに中断する挙動になる

■ステータスバーで一時的に見せる
Application.StatusBar = "全てのテストが正常に通過しました."
' 1秒
Application.Wait (Now + TimeValue("0:00:01"))
Application.StatusBar = False

■配列を宣言と同時に定義する
Variant 使う

' nAmount_XXX は Long とする
Dim amounts As Variant
amounts = Array(nAmount_100, nAmount_50, nAmount_20, nAmount_10, nAmount_4, nAmount_1)

■引数の無い関数は Sub
Call subrootin_name()
^^^^
これがないと構文エラーになる。

■セルのめぐり方
Dim rangeobj As Variant
rangeobj = ThisWorkbook.Names("SHEET_NAME").RefersToRange

' 最大値取得
rowmax = UBound(rangeobj, 1)
colmax = UBound(rangeobj, 2)

' ランダムアクセス  rangeobj(行番号, 列番号)  1-origin
dim x as long
dim y as long
x = 1
y = 4
rangeobj(y, x)

**RefersToRange
https://msdn.microsoft.com/ja-jp/vba/excel-vba/articles/name-referstorange-property-excel

 x x x x
 x x x x
 x x x x
 ...

↓ 二次元にする

array[row][col]
array[行][列]
array[y][x]

■ubound, lbound
lbound(arrayname[, dimension])
ubound(arrayname[, dimension])

lbound が配列の下限の添字を返す。
ubound は上限。

本来は [0, 上限] のはずで len(arrayname) だけで済むはずだが、
vba は [a, b] を指定できるクソ仕様なので ubound, lbound で得るようになってる。。。
dimension を省略すると1。**1-originなのです**

■Option Explicit は変数宣言指定必須オプション
絶対使う、くらいでもばちあたらへん

■デバッグ実行 in Excel 2013
F8             ステップイン
Shift+ F8      ステップオーバー
Ctrl+Shift+ F8 ステップアウト
Ctrl + F8      カーソル行まで

ステップイン …… 一行進む。関数内に入る
オーバー     …… 一行進む。関数内入らない
アウト       …… 今実行中スコープの関数を抜ける

■Wordマクロ関連
マクロのCRUD
→ 表示 > マクロ > マクロの表示
   保存時は Normal.dotm

マクロにショートカットキーを割り当てる
→ ファイル > オプション > リボンのユーザ設定 > ユーザ設定
   分類メニューからマクロを選択。
   割り当てたいマクロを選択し、割り当てるキーを押し、割り当てボタンを押す。
   保存先は Normal.dotm を指定。

■標準入出力
WScript.StdIn

  .ReadLine()
    一行読み込むプロパティ
    読み込んだ内容を返す。

WScript.StdOut

  .WriteLine CONTENTS
    CONTENTS を標準出力。

■エラー処理
On Error Resume Next
  Onerror処理の開始。
  エラー発生時に次行を実行する。

On Error Goto 行番号
  Onerror処理の開始。
  エラー発生時に指定した行番号へジャンプする。

On Error Goto 0
  Onerror処理の終了。

■クラス
class クラス名
  ～
end class
  クラスを定義する。

Dim obj
Set obj=New classname
Set obj=Nothing
  基本的な使い方。
  1. クラス型にする予定の万能型 obj を宣言
  2. obj にクラス classname のインスタンスをセット
  (3. あれこれ処理をして…)
  4. インスタンス Obj を破棄

[private|public] 変数i
  プロパティを定義。

Private Sub Class_Initialize()
  ～
End Sub
  コンストラクタを定義。

Public [Default] Property Let|Get PROPERTYNAME
  ～
End Property
  Let    プロパティ PROPERTYNAME への代入時に呼び出される。
  Get    プロパティ PROPERTYNAME への参照時に呼び出される。
      最低でも一つ以上の引数が必要。
  Default  既定プロパティにする。

■オブジェクト
  オブジェクト
    |--- プロパティ(データ)
    |--- メソッド

  各メンバの呼び出し方
    Obj.propertie
    Obj.method
    Obj '既定プロパティ

  オブジェクトの利用（代入と破棄）
      Set obj=WScript.Arguments
      Set obj=Nothing

  With句
    With ～ End With 内については
    Obj.member ではなく .member と書ける。

■関数
Function 関数名 ([[渡し方] 引数i])
  関数内容
  [関数名=戻り値]
End Function 

  呼び出し方
    val=Function(p1)
    Function p1
    Call Function(p1,p2)

■サブルーチン
Sub サブルーチン名 ([[渡し方] 引数i])
  サブルーチン内容
End Sub

  渡し方
    ByRef  参照渡し（省略時はコレ）
    ByVal  値渡し
    Optional デフォルト引数の指定
             Optional use_hoge=True

  ・サブルーチン内からグローバル変数を操作可能
  ・サブルーチン内から抜ける場合は Exit Sub
  ・引数として配列を渡したい場合は Array() 等と記述

  呼び出し方
    Subrootin p1,p2
    Call Subrootin(p1,p2)

■明示的キャスト
CBool  ブール型（Boolean）に変換 
CByte  バイト型（Byte）に変換 
CCur  通貨型（Currency）に変換 
CDate  日付（時刻）型（Date）に変換 
CDbl  倍精度浮動小数点型（Double）に変換 
CInt  整数型（Integer）に変換 
CLng  長整数型（Long）に変換 
CSng  単精度浮動小数点型（Single）に変換 
CStr  文字列型（String）に変換 

■型種類
Empty    初期化されていない場合
Null    無効な値
Byte    0～255
Int    -32768～32767
Long    -2147483648～2147483647
Single  -3.402823E38 ～ -1.401298E-45
      1.401298E-45 ～ 3.402823E38
Double  -1.79769313486232E308 ～ -4.94065645841247E-324
      4.94065645841247E-324～1.79769313486232E308
Currency  -922337203685477.5808 ～ 922337203685477.5807
Date    西暦100年1月1日 ～ 西暦9999年12月31日 
String  任意
Boolean  True|False
Error    エラー番号
Object  オブジェクトを参照

■日付時刻
#date#

  日付リテラル。
  例) #2011/07/05#

now
date
time

  YYYY/MM/DD HH:MM:SS
  YYYY/MM/DD
  HH:MM:SS

year(now), month(now), day(now)
hour(now), minute(now), second(now)

  nowから各情報を取り出す。
  0補完は無い。
  例) 7月なら month(now) は 07 ではなく 7

weekday(日付リテラル)

  日付リテラルに指定した日付の曜日番号を取得。
    →日=1, 月=2, …, 土=7

weekdayname(曜日番号)

  曜日番号から曜日文字列(●曜日)を取得。

■乱数
randomize
  
  シードを不定に。

rnd

  0.0 ～ 1.0 の乱数を発生。
  例) int(rnd*n)    0～n-1 までの乱数を得る

■規則
・文字位置は「1」から始まる。
・文字数は半角全角問わず「1文字」カウント。
・改行は定数 vbCrLf を使う。
・連結は & を使う。
  →文字列への暗黙的型変換も搭載(つまり数値等も連結可)

■関数
Len(s)
  sの文字数を返す。

Left(s,L)
  文字列sの先頭からL文字取り出した文字列を返す。

Right(s,L)
  文字列sの末尾からL文字取り出た文字列を返す。

Mid(s,p,L)
  文字列sのp文字目からL文字取り出した文字列を返す。

Instr([p,]s,word)
  文字列sの位置p(=0)から文字列wordを探す。
  戻り値
    Hit    先頭を基点とした文字位置(1～)
    Nohit  0

Instrrev(s,word)
  文字列sの末尾から文字列wordを探す。
  戻り値
    Hit    先頭を基点とした文字位置(1～)
    Nohit  0

Replace(s,before,after)
  文字列s内のbeforeをafterに置換したものを返す。


制御構文


■IF/ELSE
if 条件式 then
  文
elseif 条件式 then
  文
else
  文
end if

  単一行にまとめて書くなら end if は不要。
  例）if b=0 then msgbox "0!" else if b=1 then msgbox "1" else msgbox "2"

■繰り返し
for i=0 to 16 step 1
  文
next

  i=0,1,2, ... ,16まで繰り返す。

for each CURVAL in ARRAY
  文
next

  ARRAY の各要素の値が順番に CURVAL に入る。

Do
  繰り返し
Loop

  条件として while|until 条件式 を記述。
  Doの後(前判定)でもLoopの後(後判定)でも良い。
  breakを実現するなら if 条件式 then exit do など。

  

■演算子
  /    割り算
  \    割り算の商（整数部分）
  mod  割り算の余り
  ^    べき乗
  =    一致
  <>    不一致
  and  論理積
  or    論理和

■変数宣言
Const 定数名
  
  定数を宣言。
  宣言と定義の同時記述も可能。

Dim 変数名
Dim 配列名([次元,次元,…])

  万能型（何でも代入可）を宣言。
  宣言と定義の同時記述は不可。
  配列の添字は 0 ～ (次元数) まで利用可。

Dim 配列名()
Redim [Preserve] 配列名(次元)

  動的配列の定義。
  動的配列の配列サイズを変更する。
  Preserveを付加すると、既存の値を保持する。
    Preserveで保持できるのは最高次元のみ。
    例）以下はエラー
      Dim intNumbers()
      ReDim intNumbers(9,9)
      ReDim Preserve intNumbers(15,9) 

Array(要素0, 要素1, …)

  各要素を持つ配列を返す。

Split(str,separator)

  文字列 str を文字列 separator で区切った配列を返す。

UBound (配列名[,次元])
  
  指定した次元の配列の大きさ(要素数 - 1)を調べる。
  次元を略すと第一次元。  

  例） '4'を出力
    dim a(4)
    msgbox ubound(a)

  例） UBound(a)==1 なら…
    a(0) と a(1) が使える


文

■規則
・大文字小文字は区別しない

■文

文1:文2:…
  ':'で区切る。

文1 _
文1 _
文1
  行末に (SPACE)_ を付けると、改行とはみなさない。

'コメント
  コメントは単一行のみ。

If false then … end if
  常に偽となる条件分岐の中に書くことで
  擬似的に複数行コメントが可能。
```
