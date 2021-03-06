# デザインパターン 勉強ノート

## 最近の学習し直し

```
GoFの23のデザインパターンを，Javaで活用するための一覧表　（パターンごとの要約コメント付き） - 主に言語とシステム開発に関して
http://d.hatena.ne.jp/language_and_engineering/20120330/p1

事例で学ぶデザインパターン
https://www.ogis-ri.co.jp/otc/hiroba/technical/DesignPatternsWithExample/index.html
基本的なパターン5つほど。

TECHSCORE デザインパターン
http://www.techscore.com/tech/DesignPattern/Strategy.html/
before/after と、javaを用いたサンプルコードとクラス図。

IT専科 デザインパターン入門
http://www.itsenka.com/contents/development/designpattern/
実装方法と java ソースとクラス図。
before/afterやメリットデメリット等の解説は乏しい。
```

## Decorator

```
概要:
既存のクラスに対する追加処理を、そのクラスに手を加えないで実現する。
由来は、処理の追加を飾り付け(デコレート)にたとえて。

イメージ:
インスタンス生成時に decorator と decoratee を指定する感じ。
	例:Aでデコレート、それをBでデコレート、それをCでデコレート。
	DecoratorC.new(
		DecoratorB.new(
			DecoratorA.new(
				Decoratee.new()
			)
		)
	)

実装上のポイント:
- decorator は decoratee をコンポジションする
 - このおかげで decorator は decoratee の処理をラップできる
- decorator と decoratee は共通のインタフェースを実装する
 - decorator と decoratee を同一視できる
```

## Builder

```
概要:
何かを作るロジックを「材料」と「作成者」とに分けるパターン。
材料を規定する builder と、どう作るかを規定する director がいる。

director は常に同じやり方で作ろうとする。
ただ与えられる材料が違えば、作られるものも違うってだけ。

イメージ:
材料 hoge で作リたい場合、hoge builder を作って、材料をしこしこ登録してく。
んで director を、hoge builder を与えて初期化して、あとは construct を呼ぶ。

実装上のポイント:
- builder はインタフェース
 - 具体的な材料は concrete builder として準備する
- director は builder をコンポジションする

メリット:
- 利用者は hoge builder を選ぶだけで hoge を作れる
  (hogeが作れるようそっちで頑張ってパラメータを指定してくださいね、ではなく)
  ->矢沢久雄の早わかりGoFデザインパターン
    http://itpro.nikkeibp.co.jp/article/COLUMN/20051222/226711/

メモ
builder と template method の違いは、インスタンス生成の責務が誰か
->builder は director、template method はスーパクラス
```

## Strategy

```
概要:
アルゴリズムを交換可能にする。
アルゴリズムのインタフェースクラスを作り、
各アルゴリズムはそれを実装するようにすることで実現。

実装1
Strategy   : アルゴリズムのインタフェースを定義
StrategyA  : Strategyを元にアルゴリズムAを実装。
Context    : Strategyを使用するクラス。利用者はこれを使う。
             使用するアルゴリズムとして StrategyX を ctor 等で渡す。
             保持はコンポジションかな。

実装2 ducktypingによる実装
StrategyA  : 具体的なアルゴリズムA
StrategyB  : 具体的なアルゴリズムB
Context    : StrategyXを使用するクラス。利用者はこれを使う。
             StrategyX 使用部分は duck typing で書いておく。

メリット)
- アルゴリズムの交換が容易
 - StrategyXを作って、Contextに与えるだけで済む
- 利用者をアルゴリズム実装部分から分離できる
 - 利用者に影響を与えずにアルゴリズムの内部実装を変更できる
 - …まあインタフェース使う際のメリットやな.
```

## Factory, FactoryMethod

```
概要:
生成したいオブジェクトを, ファクトリと呼ばれる専用クラス/メソッド経由で生成する.

メリット)
- 生成処理がファクトリに分離されるため, 利用者側の依存度が減る
 - 利用者はファクトリを使うだけでよく, 生成処理の詳細を意識せずに済む
 - 生成処理を変更しても, 利用者側には波及しない.
  - 利用者側インタフェースを変えないように内部処理を変更できるから.
- 生成オブジェクト及びそのファクトリがインタフェース化されているため, 交換が用意
 - Mock用を作ってテストしたりとかもできちゃう.

Factory Method パターンの説明例)
- template method をインスタンス生成に応用したもの
 - インスタンス生成の枠組だけを作り、詳細はサブクラスに投げる
 ->http://xaro.hatenablog.jp/entry/2014/09/28/154225
- 一緒に使ってほしいオブジェクトを生成するためのメソッド
 - "クラスを new して返すメソッド" を用意するというもの
 - クラスのメンバの中に、他のクラスのオブジェクトを返すメソッドがあるのです
 ->http://itpro.nikkeibp.co.jp/article/COLUMN/20051202/225609/

メモ)
- Q: 生成部分と使用部分の分離ってどういうこと?
 ->A: 生成はファクトリ内で行い、使用者はファクトリに生成を依頼するだけでいい. 使用者は生成に関する詳細を意識しなくていい. 分離できてるじゃん?
- Factory パターンと FactoryMethod パターンの違いは?
 ->A: factory パターンはどのオブジェクトを生成するかの判断も使用者から隠す。ファクトリ内部で動的に判断する感じ。FactoryMethod パターンは、生成するオブジェクトの種類毎にファクトリを用意して、そいつらのスーパクラスを設けて、利用者はそれを使うようにする。ただしどのオブジェクトを生成するかは利用者側で決めなあかん。
```

## Proxy

```
概要:
本人の代わりに代理人クラスを立てる。
目的は「本人の負荷分散」や「本人の挙動に手を加える」など。
まあ一言で言うなら処理のフック。

メリット)
- 利用者は、利用するものが本人なのか代理人なのかは気にしない
 ->proxyパターンは利用者に気付かせずこっそり代理を立ててるイメージ

実装上のポイント
- 本人クラスと代理人クラスは同じインタフェースを実装
- 代理人クラスは本人クラスを包含

メモ: decoratorパターンとの違いは？
- decorator はクラス作成者が使うもの、proxyはクラス利用者が使うもの
- decorator 利用者はどのように改造されたか知っているが、proxy 利用者は知らない

語源
webサーバの負荷を軽減するために置く proxy サーバから。
```

## Composite

```
概要:
中身と容器を同一視して、統一的に扱えるようにする。
ファイルとディレクトリは典型例。

メリット)
- 同一視できるので扱いやすく、変更にも強い

実装上のポイント
- 中身クラスも容器クラスも共通のインタフェースを実装する
- 容器クラスは中身クラスを(共通インタフェースで)包含する
```

## Bridge

```
概要:
機能と実装を分離することで、機能の拡張を容易にする。

メリット)
- 機能と実装が分かれるので、各々の機能拡張がしやすい
- 機能を使う利用者は、実装の詳細を意識しなくてよくなる

デメリット)
- 機能の拡張は、実装階層にあるクラス(もっというとインタフェース)で実現可能な機能に限られる
 - 実装階層のインタフェースはしっかり設計してやらないといけませんね

由来:
機能階層と実装階層とを繋ぐ橋渡しとなるクラスがあるから。
→機能階層の大元クラスのこと。
 こいつは実装階層のインタフェースを包含してるわけだが、
 これをクラス図で見てみると、両階層に渡る橋のように見える。

実装のポイント:
- 実装階層と機能階層に分かれている
- 実装階層には、実装の大元となるインタフェースと、それを実装する実装者クラス達がある
 - ex. クリップボードインタフェースと、OS毎の実装クラス
- 機能階層には、実装を利用して機能を実現したクラスがある
 - このクラスは適宜拡張できる(拡張は継承の形で行われる)
- 機能階層の大元クラスは、実装インタフェースを包含する
 - どの実装を使うかは、大元クラスのctorなどで渡すことで実現

参考:
http://thinkit.co.jp/article/936/1/page/0/2
http://hamasyou.com/blog/2004/06/06/bridge/
http://www.ie.u-ryukyu.ac.jp/~e085739/java.it.7.html
```

## Command

```
命令をオブジェクトとして扱うことで、管理や保守性を柔軟にする。

メリット
- 各命令の仕様を統一できる
- 各命令に内部状態を持たせることができる
- 利用者側は、命令を保持し、好きなタイミングで使うことができる

実装のポイント
- Command: コマンドのインタフェースを既定するインタフェースクラス
- ConcreteCommand: その実装クラス

Command にどんなメソッドを規定するか次第で用途は幅広い
- execute() と unexecute() を規定すれば、undo/redo を実現できる
- execute() と description() を規定すれば、execute の結果を出力する機構が作れる
```

## Observer

```
概要:
観察対象が観察者に更新通知を送ることで、観察者は観察対象を監視できる。

イメージ:
観察対象「俺を観察したい奴は名乗れ。俺が更新された時に通知してやるからよ」

実装のポイント
- 観察対象(サブジェクト)は、add_observer, remove_observer, notify_observers を持つ
 - サブジェクトの何らかの更新処理から notify_observers を適宜呼び出す
- 観察者(オブザーバ)
 - インタフェースクラスとして update(subject) メソッドを持つ
  + update メソッドの設計方法は二通り
   - pull型: update(subject) のようにサブジェクトを丸ごと渡す
   - push型: update(subject, p1, p2) のように必要データを引数で渡す
```

## Mediator

```
概要:
複雑な依存関係を解決するために、仲介者(mediator)を介させる。

collegue collegue
    |    |
    |    |
   mediator---collegue
      |
      |
  collegue

誰と誰がどう依存してるかは全部 mediator が管理する。
相談者(collegue)は、自分が何かした時に mediator に知らせるだけ。
→状態が変わったら通知という使い方が多い。

実装のポイント
- mediator は collegue 全員を包含する
- 各 collegue も mediator を包含する
- mediator は各 collegue の詳細を知っている
 - スーパクラス単位で抽象的に扱う必要はない
 - むしろ SubClass1 と SubClass2 はこういう風に制御する、みたいな詳細を知っている
 - それゆえ ConcreteMediator はつぶしがきかない(再利用できない)。

参考
http://www.techscore.com/tech/DesignPattern/Mediator.html/
http://www.ie.u-ryukyu.ac.jp/~e085739/java.it.18.html
http://www.hyuki.com/dp/cat_Mediator.html
```

# 古い

## Bridgeパターン

```
Abstraction
←RefinedAbstraction1
←RefinedAbstraction2
…

Implementor
←ConcreteImplementor1
←ConcreteImplementor2
…

Abstraction◇---Implementor

使い方はこんな感じ。
	new RefinedAbstraction(new ConcreteImplementor2)
	new Abstraction(new ConcreteImplementor1)
使いたい追加機能を持つクラスのインスタンスをつくり、
初期値として使いたい実装機能を与えてやる。
```

## 201301学習分

```
アルゴリズムと同じで、完璧に覚える必要はない。
要点とメリットデメリットを抑えておいて、使いたいときに調べながら使えるように。
[覚えるもの]
・どんなパターンにどんな名前が付いているか(元々名前を共通化して話しやすくするのが目的)
・大体どういうふうに実装するか
・どういう時に使ったらどう嬉しくなるか
```

## 130106 Stateパターン

```
Stateパターン
一状態を一クラスで管理するパターン。

メリット)
状態に応じて条件分岐して処理…みたいな記述を無くす

考え方)
状態を表すクラスのインタフェースをつくり、状態数だけ実装クラスをつくる。
現状態を保持し、状態を用いた処理を持つクラスをつくる。

作り方)
State: 状態を表すクラスのインタフェース
ConcreteState: 同上実装。状態数だけ定義。シングルトンにする。
Context: 状況判断を行うクラス
	現状態を保持。
	利用者へのインタフェースを提供
	状態を変更するメソッドを提供

状態の変え方には色んな方法がある。
呼び出し側で変えるとか、次状態への遷移関数を各状態が持つか。
後者の場合、各状態は(状態を管理する)Contextにアクセスすることになる。
→Contextオブジェクトを引数渡ししないといけない。結合度が高くなっちゃうのが欠点。
```

## 130106 Observerパターン

```
あるオブジェクトの状態変化を監視したい場合に使えるパターン。

メリット)
同期を楽に取ることができる。

考え方)
観察対象オブジェクトを観察する観察者クラスをつくる。
観察対象クラスは観察者を複数個保持できるようにし、
自身の何らかの処理の後に、観察者達に通知するようにする。
→観察者が観察対象を見るというよりも、観察対象が観察者に教えてやるイメージ。

作り方)
Subject: 観察対象インタフェース
	観察者オブジェクトを複数個保持するデータ構造。
	観察者を追加する機能。
	観察者たちに通知を送る機能(各観察者の更新メソッドを, 自分自身を渡して呼ぶ)。
	自身の状態を返す抽象メソッド。
ConcreteSubject: 観察対象の実装クラス
	自身の状態を返す抽象メソッドを実装。
	観察対象自体が持つ, 何らかの処理を行う機能。
		この中から観察者たちへの通知機能を呼び出す。	
Observer: 観察者インタフェース
	自身の状態を更新する抽象メソッド(観察対象がこれを呼んでくれる)
ConcreteObserver: 観察者の実装クラス
	自身の状態を更新する抽象メソッドを実装。
		観察対象オブジェクトが渡ってくるので、それを元に何かする。
		やつには自身の状態を返すメソッドがあるのでそれを使うことになるかと。

使い方)
観察者と観察対象をインスタンス化。
観察対象に観察者を登録。
観察対象は普通に処理を行う。
```

## 130106 Mementoパターン

```
あるオブジェクトの状態を記憶し、あとで前状態に戻したい場合に使えるパターン。

メリット)
Undoを実現できる

デメリット)
状態を大量に保存するのでメモリを食う(設計次第で容量を抑えることは可能)

考え方)
あるオブジェクトの一状態を表すクラスをつくり、
それをスタック構造などで管理する。

作り方)
Originator: あるオブジェクト。
	自身の現状態を表すMementoオブジェクトを返す機能。
	与えられたMementoオブジェクトを自身の状態に反映する機能。
Memento: あるオブジェクトの一状態を表すクラス
	コンストラクタ、メンバ変数、セッターゲッターはプライベート。
	関係無いクラスからアクセスさせないため。
	(OriginatorはMementoを編集するので, friend属性を付加する)
	容量を抑えるため、状態管理に必要な最低限のデータのみ定義すること！
Caretaker: 状態を保持するクラス
	Mementoオブジェクトを保持するデータ構造。
	Originatorの状態を変更する機能。
	※個人的にはCaretakerにOriginatorも持たせて、
	  利用者はCaretakerオブジェクトのみの操作で済むようにしたらいいかと思う。
	  CaretakerがOriginatorをラップしてるイメージ。

使い方)
	※以下は上記個人的な作り方に従った使い方
	Originatorインスタンスを生成。
	Caretakerインスタンスを生成。
	CaretakerにOriginatorを渡す。
	Caretakerを使う。
```

## 130106 Mediatorパターン

```
オブジェクト同士の通信時に仲介役を介させることで、オブジェクト同士の通信の複雑化を防ぐ

メリット)
オブジェクト同士の通信がなくなる
	[before]o1: o2, o3を呼び出す/o2: o1, o3を呼び出す/o3: o1, o2を呼び出す
	↓
	[after ]o1: mediatorを呼び出す/o2: mediatorを呼び出す/o3: mediatorを呼び出す

デメリット)
mediator自体が複雑になる

作り方)
Colleague: 同僚インタフェース。相談役のセッター及び保持(一人)機能、相談役が呼び出す窓口を持つ。
ConcreteColleague: 同上実装
Mediator: 相談役インタフェース。同僚のセッター及び保持(相談してくる人全員)機能、同僚が呼び出す窓口を持つ。
ConcreteMediator: 同上実装

使い方)
同僚と相談役のインスタンスを作る。
各同僚インスタンスに相談役インスタンスをセットする
相談役インスタンスに各同僚をセットする
利用する(同僚に"相談役に相談するメソッド"をつくり、その内部で自身が持つ相談役を呼び出すイメージ)
```

## 130105 Iteratorパターン

```
コンテナオブジェクトの要素を列挙する方法を提供する。

メリット)
コンテナオブジェクトから列挙機能を切り離すことで、
利用者が列挙機能を使う際にコンテナの内部仕様を気にする必要が無くなる。

Iterator: イテレータの利用側インタフェース
ConcreteIterator: 同上の実装クラス
Aggregate: イテレータに必要な機能のインタフェース
ConcreteAggregate; 同上の実装クラス

作り方)
Iterator
	次の要素を返すnext抽象メソッド
	次の要素の有無を返すhasNext抽象メソッド
Aggregate
	Iteratorオブジェクトを返す抽象メソッド
ConcreteAggregate
	Iteratorオブジェクトを返すメソッド。
	あとはイテレータを実現する機能とかデータ構造とか。
ConcreteIterator
	ConcreteAggregateオブジェクトを保持する。
	ConcreteAggregateの機能を使って、nextとhasNextを実装する。

使い方)
ConcreteAggregateインスタンスaを作る。
aの機能を使ってデータを登録。
aの機能を使ってイテレータオブジェクトを取得。
取得したイテレータオブジェクトを使って走査。
	→制御文の書き方例. while(it.hasNext()){ curData = it.next()}
```

## 130105 Commandパターン

```
命令とそれに伴うパラメータをカプセル化する。

考え方)
命令をオブジェクトとして扱う。
命令の処理内容とパラメータを持つクラスを作り、
そのオブジェクトを管理クラスで管理するような構造。

メリット)
命令オブジェクトをスタックで管理すればUndoを実現できる。
他にも色々あるみたいだがよくわからん…。
まあ命令をオブジェクトとして管理できることの恩恵が色々あるんだろ。

デメリット)
コード量が増える。
普通、あるクラスCに命令を送るには obj.command1(arglist); などと書くが、
このパターンでは command1 の部分を別クラスにするんだよ。

作り方)
Command: 命令を表すクラスのインタフェース
ConcreteCommand: 命令を表すクラス
Receiver: 命令を受け取るクラスのインタフェース
ConcreteReceiver: 命令を受け取るクラス
Invoker: Commandオブジェクトを管理(命令の登録, 削除, 登録された命令を順番に実行等)するクラス

使い方)
ConcreteなReceiverとCommandのインスタンスを作る。
(Commandインスタンスには受取先としてReceiverインスタンスを渡す)
Invokerのインスタンスを作る。
CommandインスタンスをInvokerに登録していく。
Invokerの実行メソッドを呼ぶ。
```

## 130105 Chain of Responsibility(CoR)パターン

```
ある処理を行えるオブジェクトを連鎖させ、そこに依頼すれば誰かが処理してくれるような構造を実現する。

メリット)
利用者側も処理側の役割分担を明確にできる。
	利用者側：連鎖を作って、処理の依頼を出すだけ
	処理側：流れてきた依頼を処理できるなら処理し、ダメなら次のオブジェクトに垂れ流すだけ

デメリット)
・連鎖が深いと保守性が悪くなる(どのオブジェクトが処理してるかがわからない)
・連鎖が深いほど実行速度が遅くなる

作りかた)
連鎖を形成する一要素のインタフェースHandlerをつくる
	依頼を受ける機能(抽象)
	次のオブジェクトの受け取って保持&返却する機能
Handlerを実装したConcreteHandlerをつくる
	依頼を受ける機能を実装する。
	内部では自分の処理できるもののみ処理し、
	できないものは自身が持つ次のオブジェクトに依頼する
	次のオブジェクトが無い場合はエラー吐くなりなんなり。

使い方)
連鎖を構成する要素をそれぞれ初期化する。
初期化した要素たちを繋いで鎖にする。
鎖の最初の要素に依頼する。
```

## 130105 Template Methodパターン

```
ある処理の共通手順をテンプレート化しておくことで、関連する処理の実装に統一感を持たせる。

共通手順の例)
1. 開く→処理する→閉じる
2. 初期化→処理→後処理

考え方)
共通手順を定義したクラスを作り、それを実装or継承させる。

作り方)
共通手順を持つクラスを作る
  持たせるのは純粋仮想関数でもいいし、単なる仮想関数でもいい。
  実装漏れはなくなるが全部実装しないといけないか、
  全部実装しなくてもいいが実装漏れが起こりえるかの違い。
共通手順に従うクラスがそれを実装or継承する
```

## 130105 Interpreterパターン

```
何らかのフォーマットを解釈して、その結果に則って処理したい場合に、小さなインタプリタを実装する。

作り方)
AbstractExpression    抽象的な表現
TerminalExpression    終端となる表現
NonterminalExpression 非終端となる表現
Context               文脈・状況判断
Client                利用者

Contextはフォーマットを走査する。次のトークンを取得、読み終えたかどうかの判定などのメソッドを持つ。
AbstractExpressionはContextを解釈するための共通インタフェースを定義。
TerminalとNonterminalはこれを実装する。
TerminalはContext内の終端となるトークン一つを保持する。
NonterminalはContextを読み進めて、状態を遷移させたり、終端を保持したりする。
ClientはContextオブジェクトを持ち、解析を呼び出す利用者。

使い方)
ClientはContextオブジェクトをつくる。
それをNonterminalExpressionに渡してインスタンス化する。
インスタンスの解釈メソッド(expression.interprit(context)みたいな)を呼ぶ
結果を出力(expression.toString()みたいな)する
結果に対してあれこれ処理
```

## 130105 Proxyパターン

```
あるオブジェクトの負荷を軽減するため、その代理で働くオブジェクトを用意する。

色んな活用例があるけどここでは「使う直前のインスタンス化を心掛ける」ことを取り上げる。
作り方)
・RealSubject(本人)クラスとProxy(代理人)クラスのインタフェースSubjectをつくる。
・RealSubjectは普通に実装し、Proxyは自身でRealSubjectのオブジェクトを保有する機能を持つ
  ただしRealSubjectをインスタンス化するのはその機能を使う直前
                                           ~~~~~~~~~~~~~~~~~~
RealSubjectインスタンスのリソースが大きいor生成に時間がかかる場合、
直前になってインスタンス化することで負荷を軽減できている。
Proxyが使用タイミングを代理してくれている。

他の使用例)
複雑で巨大なオブジェクトをFlyweightで唯一存在させ、
複数のProxyオブジェクト(各々当該オブジェクトへの参照を持つ)で使い分けるというやり方もある。
```

## 130104 Flyweightパターン

```
インスタンスを使いまわすことで省リソース化を図る。

考え方)
クラスAのインスタンスを使いまわしたい場合。
Aのインスタンスを生成・保持するファクトリFをつくる。
・FはAのインスタンスを生成して自身で保持する機能を持つ
  (保持機構として, Aへのポインタ配列を使うのが普通)
・Fは利用者から要求されたインスタンスを返す機能を持つ
・Fはシングルトン

使い方)
利用者はファクトリのインスタンス取得メソッドを(パラメータを与えて)呼ぶ。

メソッド内部では以下のように動く
・与えられたパラメータに対応するインスタンスを保持していない
  →生成して保持し、生成したものを返す
・保持している
  →保持しているものを取り出して返す

語源)
Flyweightはフライ級の意。
ボクシングで最も軽い階級であり、いかに体重を落とすかが重要。
```

## 130104 Facadeパターン

```
複雑な処理をラップして、一つの口から使わせたい時に。
Facade(ファサード)とは「窓口」という意味。

実現方法)
複雑な処理をラップした静的関数を持つクラスFacadeを作る。

利用者は Facade::method() を呼ぶだけで使える。
内部がどのように複雑になってるかを知る必要は無い。

※wikipedia等に細かい注意事項がつらつら。使う際は要チェックかと。
```

## 130104 Decoratorパターン

```
既存のクラスに対する追加処理を、そのクラスに手を加えないで実現する。
追加処理を飾り付ける(デコレート)するようにすることからDecoratorという名前。

クラス)
ConcreteComponent: デコレート対象のクラス
Component: 同上インタフェース
ConcreteDecorator: デコレートを行う用のクラス
Decorator: 同上インタフェース

作り方)
Component, ConcreteComponentは既存。
Componentを継承したDecoratorをつくる
	DecoratorはConcreteComponentを保持する。
	ここではComponentの純粋仮想関数は実装しない。
Decoratorを実装したConcreteDecoratorをつくる
	Conmponentの純粋仮想関数を実装する。その際、
	既存処理には自らが保持するConcreteComponentのオブジェクトを使い、
	追加処理を独自に書く。

使い方)
デコレータXとYで飾り付けたい場合は、こんな感じで書く。
	Component* obj = 
		new ConcreteDecoratorY(
			new ConcreteDecoratorX(
				new ConcreteComponent(…)
			)
		);
これは以下のように呼び出される
	obj.method()
		Y::前処理
		Y::自身が持つXのオブジェクトのMethod
			X::前処理
			X::自身が持つConcreteComponentのMethod
				ConcreteComponent::処理
			X::後処理
		Y::後処理
```

## 130104 Compositeパターン

```
中身と容器を同一視することで、再帰構造の扱いを楽にする。

活用例)
ファイルシステム。
ディレクトリは容器or中身で、ファイルは中身なので、同じ削除でもその処理内容は異なる。
compositeを適用して、ディレクトリだろうとファイルだろうと、同じメソッドを削除できるようにすると便利。

実現方法)
共通のインタフェースを用意。
ディレクトリクラスもファイルクラスもそれを実装する。
利用者はインタフェースへのポインタを使って、ディレクトリやファイルのインスタンスを扱う。

ディレクトリにしか存在しない機能は、以下の二通りの実現方法がある。
・インタフェースに純粋可能関数を定義し、ディレクトリでのみ実装する
  (ファイルでは何もしないなり、エラー処理をするなり、状況に応じて何かを…)
・ディレクトリにその機能を定義する。
  (呼び出し側ではディレクトリクラスにダウンキャストする必要がある)

ディレクトリはファイルを包含しており、そいつらにまとめて処理したいケースがある。
でもインタフェースが共通であるから、ディレクトリとしてはインタフェースとして使うだけで済む。
そしたら後は各ファイルのインスタンスが自分の処理を実行してくれる。
```

## 130104 Adapterパターン

```
あるクラスが提供しているインタフェースを、別のクラスのインタフェースに差し替える。

背景)
あるインタフェースIを継承したあるクラスAがある。
Aのオブジェクトは既に利用されているが、aに不具合が見つかった。
不具合を直したクラスBをつくったが、Aを使っている部分を差し替えるのは面倒だ。
差し替えを最小限に済ませるにはどうするか。
→Aと同じインタフェースを持ち、Bの機能を使うクラスAdapterをつくればいい。

実現方法)
・Adapter自身のメンバ変数としてAのオブジェクトを持たせる。
  提供するインタフェースはAと同じにし、内部処理はBの機能を使う
・AdapterはAとBを継承し、Aの機能を呼び出した時にBの機能が呼ばれるように実装する

いずれにせよAdapterはIを実装しなければならない。
利用側では I* obj = new A(…); としているはずなんで。
```

## 130103 singletonパターン

```
プログラム中でただ一つしか存在しないインスタンスをつくるのに使う。

作り方)
こんなクラスを作る
・自身のインスタンスを保持するprivateメンバ変数を持つ
・privateなコンストラクタを持つ
・自身の保有するインスタンスを返すpublicな関数(getInstance)を持つ

使い方)
Singleton::getInstance() にてインスタンスを取得する。

## 130103 prototypeパターン
インスタンスを生成する際、既存のインスタンスの複製を作ることで代用する。
普通の生成方法(newなど)では時間がかかる場合に重宝する。

作り方)
複製用の抽象メソッドcreateCloneを持つ抽象クラスPrototypeを作り、
本パターンを使いたいクラスConcretePrototypeがPrototypeを実装する。

使い方)
ConcretePrototype obj,obj2;
obj1.procedure(); //内部状態が変わるが、とても時間のかかる処理
//obj2.procedure(); //時間のかかる処理を何度もやるのはバカらしい
obj2 = obj1.clone(); //一度出来たオブジェクトを複製すればいい
```

## 130103 builder パターン

```
オブジェクトの生成や初期化を共通化し、利用者にその手順に関知させなくする。

必要なもの)
・生成・初期化手順のインタフェースを定めたBuilder
・それを実装したConcreteBuilder
・Builderオブジェクトと、それを用いて生成・初期化処理を呼び出すメソッド(construct)を持つDirector

使い方)
DirectorにConcreteBuilderを渡してインスタンス化する。
Directorインスタンスのconstructを呼ぶ。
生成されたもの、初期化の結果などが返されてくる。

メリット)
生成・初期化する際、利用者はDirectorに頼むだけで済む。
利用者は生成・初期化手順に関知しない。
```

## 130103 abstract factory パターン

```
製品クラス(複数可)とそのファクトリを抽象化したもの。
製品クラス達の生成手順を一つのファクトリに集約できる。
factoryパターンと違い、一つのファクトリは複数の製品を生成できる。

利用するには)
製品クラス達を実装したクラスを用意し、それらを生成するファクトリを実装する。
```

## 130102 bridge パターン

```
機能追加も機能実装もされた抽象クラスAに適用する。
Aに機能を追加するクラス階層と、Aの機能を実装するクラス階層を分ける。
Aが両者のクラス階層の架け橋となっていることからBridge。

Aに機能を追加するには、追加機能を持ったサブクラスを作ればいい。
Aの機能を実装するには、実装機能を持ったサブクラスを作ればいい。
いずれにせよ他方のクラス階層には影響が無い。

Aに実装した機能は、追加機能を持ったクラス全てからも使える。
Aに追加した機能は、追加機能を持ったクラスからしか使えない。
```

## 130102 factory パターン

```
あるクラスからそのオブジェクトの生成を追い出すことで、そのクラスの再利用性を高める。
(オブジェクト生成はクラスに特化した処理であるため再利用性を削ぐ)

あるクラスのオブジェクトを生成する用のクラス(ファクトリ)をつくり、
そのオブジェクトはファクトリから生成するようにする。
```
