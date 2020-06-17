# Doxygen

## sjis の日本語でも文字化けしないようにする
INPUT_ENCODING = "CP932"

## doxygenコメントの書いてない関数も対象にしたい

```
EXTRACT_ALL            = YES
```

## コールグラフを書く(Windows版GUIベース)
必要なツール

- Graphviz
- インストールして、dot.exeのあるパスを控えとく

必要な Ooxy 設定

```
SOURCE_BROWSER         = YES
RECURSIVE              = YES
HAVE_DOT               = YES
DOT_NUM_THREADS        = 4    # 0でもいいがスレッドがあると処理が早い
CALL_GRAPH             = YES
CALLER_GRAPH           = YES
DOT_PATH               = "C:/Program Files/Graphviz2.38/bin"
```

## 使い方

```
$ doxygen -g
$ yorueditor Doxygen
(いじる)
$ doxygen
```


## doxygen コマンド
doxygen 設定ファイルパス

省略時はカレントディレクトリのファイルが探索されて読み込まれる。

## 探索先の指定: INPUT
探索先ディレクトリをスペース区切りで指定。

指定無しならカレントディレクトリを探索。

例) `INPUT                  = ./ ../src`

## 文法
- コメント無き定義は無視され, 一切表示されない
- コメントはどこに書いてもいい(hでもcppでも)
 - doxygenが自動的に辿って全て表示してくれるから
 - 辿れないと表示されない(includeが足りない, 修飾子が足りない等)

## briefとdescription
briefコメント

- 一行の「@brief hoge」or「/// hoge」or「int variable; ///< hoge」のこと
- クラスページのメソッド一覧, 変数一覧に表示される

descriptionコメント

- \n で区切った複数行の「@brief hoge」あるいは「/// hoge」のこと
- クラスページの関数の項, 変数の項に詳細説明が表示される

## 書き方
- ファイルの識別
    - 先頭付近に「/// @file myclass.cpp」を書けばよし
- 定数/マクロ
    - briefは普通にbriefコメントで
  - descriptionは「@def 定数名 \n /// 説明」or「(#define HOGE に対しては)単なるdescriptionコメント」で
- 表示場所
    - ファイル > ファイルメンバ > 全て|マクロ定義
    - 定義を書いたファイルのファイルページ内

## モジュール

```
@addtogroup MODULE_NAME
@{
…
@}
```

モジュール MODULE_NAME の中身に … が記述される。

@fileを含めればファイル名、関数を含めれば関数の説明が表示される。

```
/** @addtogroup HogeController
 * @{
 * @file hogecontrollerImpl.h
 * pImplイディオム用ヘッダ
 */
```
