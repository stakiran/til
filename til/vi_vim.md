# Vi Vim Editor
稀にしか使わないからいつも忘れる

# 検索
`/キーワード`

- ctrl + g で次
- ctrl + G で前
- Enter で確定（今合ってるキーワードにカーソルを移動）

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

# 複数行インデント
- :set shiftwidth=2
- shift + v でライン選択
- shift + > でインデント
- . でさらに繰り返し
