# GitLab Merge Request について

## :memo: Merge Request とは
- **私がつくったブランチ xxx を、あなたのブランチ yyy にマージしてください** リクエスト
- yyyy は大体 master

レビュー依頼を出す人:

- 修正内容をブランチ xxxx でつくる
- gitlab にアクセスして MR を選び、
    - source: xxxx を選ぶ
    - target: マージ先ブランチを（普通はmasterかしら？）
- 観点とか書いて投下

レビューする人:

- gitlab にアクセスして MR 開く
- 画面上で diff を見て「discussion」や「行単位コメント」にコメントを書く

その後のやり取り:

- レビュー依頼出した人は、適宜修正を push する
- discussion エリアでやり取りする
- 行単位コメントは、解決したら resolve する

参考: [仕様書のレビューをGitlabのMerge Requestでやろう！ - Qiita](https://qiita.com/chaspy/items/a4fe44fecf6b8fb0e587)
