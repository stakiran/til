# Tortoise Git

## マージ
master に branch をマージしたい場合。

master を checkout。merge を選び、ブランチ branch を選択して、実行。

## ブランチ削除
tortoise git > show log を開き、左上のリンク(ここからブランチ一覧に飛べる)をクリックするとブランチ一覧画面が開く。

消したいブランチを右クリックして delete branch。

リモートブランチもここから消せる。

## ブランチ作成
ローカル

- create new branch
- checkout

リモート

- push(push画面にてremote欄はoriginを選択する。そしたらremote側のブランチも勝手に生成される)

参考: http://joelabrahamsson.com/remote-branches-with-tortoisegit/

## 競合(Conflict)を編集する
競合対象のファイルを開くと、競合内容が記されているので、それを見ながら手動で修正。

マージツール開いてもいいが使い勝手悪い。直接編集した方が早い。

終わったら tortoise git > resolve を選択後、commit する。

## 特定のリビジョンをチェックアウトする
- tortoise git > switch/checkout を開く
- switch to は commit を選び, ...ボタンからチェックアウトしたいリビジョンを選ぶ

Create New Branchにチェックを入れておくと便利(後で show log から行ったり来たりできるため)。

## rename 前のファイルをログで追いかける
Show log > Walk Behaviourボタン > renameメニュー
