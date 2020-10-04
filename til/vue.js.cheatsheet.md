# Vue.js

## v-model
つまり以下を全部やってくれるエイリアス

- value 属性をつくってくれる
- input イベント発生時、（入力されてる値を）セットしてくれる

```
<input v-model="searchText">
これは以下と同じことです:

<input
  // searchText が true なら、value クラスをつける
  v-bind:value="searchText"
  // この input タグへの入力時、$event.target.value の値を searchText に入れる
  v-on:input="searchText = $event.target.value"
>
```

## v-bind
[API — Vue.js](https://jp.vuejs.org/v2/api/#v-bind)

- 属性を動的に束縛する
    - 例: `v-bind:value` は form に value 属性つけてる
- 属性として class or style を使う場合、配列やオブジェクトを指定できる

### クラス名
- v-bind:class でクラス名を動的につける
- `v-bind:class="{ ... }"`
    - key にクラス名
    - value に真偽値
    - 真偽値が true なら、key と同名のクラスをつける
- `v-bind:class="[ ... ]"`
    - 要素にクラス名（を入れた文字列変数）

### スタイル
- `v-bind:style` で css スタイル
- `v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"`
    - ほぼ css まんま
    - ただし ` v-bind:style="styleObject"` として、data.styleObject 側で定義するのがすっきり
- ` v-bind:style="[baseStyles, overridingStyles]"`
- 複数指定
    - `v-bind:style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"`
    - ブラウザが flex しか対応してない場合、display: flex に
    - ブラウザが対応してる「一番最後のやつ」が使われる

### v-bind:key="xxx" って何？
- 指定しなくても動作はする
- ただし bind してるリストの順序が入れ替わったときに（内部でvueが正しく）追随できない
- 追随させるために、key として外部キー的なやつを指定しておくと良い

> 要はキーを指定すれば、リストの要素の順番が入れ替わったりしたときに、変更前と変更後でキーが同じ要素は同じものだとみなされて、適宜DOM要素の移動が起こります。

[html - v-bind:key を使う時と使わない時の違い - スタック・オーバーフロー](https://ja.stackoverflow.com/questions/42250/v-bindkey-%E3%82%92%E4%BD%BF%E3%81%86%E6%99%82%E3%81%A8%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E6%99%82%E3%81%AE%E9%81%95%E3%81%84)

## v-on
- `v-on:click="expression"`
- `v-on:click="methodname"`
    - ただし methods に methodname を定義する必要あり
    - methods.methodname 側には event 引数が渡される
        - event.target.value で値取ったりとか
- `v-on:click="methodname(arg)"`
    - インライン表記
    - 引数を渡したい場合はこちら
    - event を渡したい場合、`v-on:click="warn(..., $event)"` $event が使える
    - とはいえロジック側で event を解釈するのは好ましくないので、後述の EVENT.MODIFER で済ましたい
- `v-on:EVENT.MODIFER="Value about this modifier"`
    - preventDefault とか呼び出すために、修飾子が使える
    - 例
        - `<form v-on:submit.prevent="onSubmit"></form>`
        - `<a v-on:click.stop="doThis"></a>`
        - :point_up: onSubmit や doThis はただのメソッド名なので注意（そういう特殊キーワードがあるのかと悩んでた）

### キー検出 キーコード keycode keyboard
- `<input v-on:keyup.enter="submit">`
    - >`key` が `Enter` のときだけ、`vm.submit()` が呼ばれます
- キーコードは？
    - https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values
    - ここのキー名をケバブケースにする
        - `PageUp` → `page-up`
    - > KeyboardEvent.key で公開されている任意のキー名は、ケバブケースに変換することで修飾子として直接使用できます。
    - 修飾キーのエイリアスとか定義したければ [keyCodes - API — Vue.js](https://jp.vuejs.org/v2/api/#keyCodes) いじる
- modifier
    - .ctrl .shift .alt .meta がある
        - .meta は win なら win、macos なら command
    - `<div v-on:click.ctrl="doSomething">Do something</div>` ctrl + click
    - `<input v-on:keyup.alt.67="clear">` alt + c
    - :x: **が、いつ検出されるかなどにクセがあるっぽいのでよく調べねば（.ctrl と .17 も違うみたいだし）**

## v-for
v-for

- インスタンス側で data.array や data.object を定義
- テンプレート側で
    - `v-for="elem in array"`
    - `v-for="(elem, index) in array"`
    - `v-for="value in object"`
    - `v-for="(value, key) in object"`
    - `v-for="(value, key, index) in object"`

### なるべく key を与えよ
- `<div v-for="item in items" v-bind:key="item.id">`
- for がバインドしてるデータの並び順が変わった時、に備えるため
- :x: in-place patch、ここ何言ってるかわからんなー（図を描いてほしい
- つまり dom の値がスカラだったら key なしでいいが、object なら key で外部キー相当のものを指定せいってこと？(vueがリアクティブに並び替えを追えるように

### その他
- オブジェクトに対する for の場合、パース順は不定
    - >順序は Object.keys() の列挙順のキーに基づいており、全ての JavaScript エンジンの実装で一貫性が保証されていません。
- バインドしたオブジェクトや配列に使えるの
    - 破壊的: push pop shift unshift splice sort reverse
    - 非破壊的: filter concat slice など
- range みたいなのもある
    - `v-for="n in 10"` これで range(10,1)、つまり 1～10（0-9じゃない）
- v-if と v-for の混在も可能だが……
    - 以下理由によりおすすめしない
        - テンプレート側にロジックが入ってしまっている
        - パフォーマンスがクソ
    - じゃあどうする？
        - x for x in obj if (cond-of-x) の場合は、computed 側で x を抽出する getter をつくる
        - if boolean then for x in obj の場合は、boolen（に相当する v-if）をテンプレート側のコンテナ要素に移動する
    - see: [スタイルガイド — Vue.js](https://jp.vuejs.org/v2/style-guide/#v-for-%E3%81%A8%E4%B8%80%E7%B7%92%E3%81%AB-v-if-%E3%82%92%E4%BD%BF%E3%81%86%E3%81%AE%E3%82%92%E9%81%BF%E3%81%91%E3%82%8B-%E5%BF%85%E9%A0%88)


## v-if vs v-show
- v-if は遅延描画、true になってはじめて描画処理が走る
- v-show は即描画 + true/falseによる表示非表示は内部的にはcssのdisplay
- ゆえに
    - 表示を頻繁に切り替えたい → show
    - あまり切り替わらない → if

## computed vs watch vs methods
- computed
    - getter setter、特に data.xxxx を使って何か求める場合（xxxxをバインドしてくれる）
- watch
    - 計算式にユーザーの入力値など「いつ来るかわからんX」がある場合(xをwatchする)
- methods
    - 上記以外汎用
    - `{{ }}` で呼ぶたびに実行走る
    - 節約したいなら computed も
