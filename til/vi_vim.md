# Vi Vim Editor
稀にしか使わないからいつも忘れる

# 置換
:%s/before/after

[vim 文字列置換 基本的な事 - Qiita https://qiita.com/shirochan/items/a16487d0739f455b5e8a]

# 行コピペ
- yy でコピー
- p でペースト

# 複数行インデント
- :set shiftwidth=2
- shift + v でライン選択
- shift + > でインデント
- . でさらに繰り返し

# 検索
`/キーワード`

- n で次
- N で前

# vim 複数行コメントアウト
入れる

- ctrl + v で矩形モード
- 範囲選択して
- shift + i で入力モード
- `#` とかでコメント追加
- esc

解除する

- ctrl + v で矩形モード
- 範囲選択して
- d

# 行番号
:set number

:set nonumber
