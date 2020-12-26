# Vue.js


## [Vue warn]: Invalid prop: type check failed for prop "XXXX". Expected Boolean, got String. が出る
- template 中の記載を `:bool-option=false` にする
    - `:` あるいは `v-bind:` がないと文字列扱いされてしまう

参考: [Vue.jsのpropsでBooleanを渡そうとしたときの型エラー - Qiita](https://qiita.com/smasato/items/8cf8edfbad3797c3b345)

## Invalid default value for prop "XXX": Props with type Object/Array must use a function が出る件

```js
  props:{
    objProp:{
      type: Object,
      default: () => {return {}}, // デフォ値を返す関数を指定する
    },
```

- prop で定義した object や array は参照として扱われれう
    - ので **値そのものを返したら呼び出し元で破壊されるかもしれない**
    - というわけで Vue さんが警告出してる
    - 破壊されないよう、返したい情報をつくる関数（ファクトリー）を経由しなさい

参考: [[Vue.js] なぜpropsのdefault値にObjectやArrayを指定する際にfactory関数にする必要があるのか - Qiita](https://qiita.com/hogesuke_1/items/c74463de1a1eee802ca8)

## 親コンポーネントから子コンポーネントのメソッドを呼び出す
- 子からは何もしなくていい
- 親では
    - template 読み込むところで ref する
    - 呼び出したい場所で this.$refs を見る
- $refs はハマリどころがあるので注意

[特別な問題に対処する — Vue.js](https://jp.vuejs.org/v2/guide/components-edge-cases.html#%E5%AD%90%E3%82%B3%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%8D%E3%83%B3%E3%83%88%E3%82%A4%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%B3%E3%82%B9%E3%81%A8%E5%AD%90%E8%A6%81%E7%B4%A0%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9)

> $refsはコンポーネントの描画後にデータが反映されるだけで、リアクティブではありません。子コンポーネントへの直接操作のための、退避用ハッチのような意味合いです(テンプレート内または算出プロパティから$refsにアクセスするのは避けるべきです)

[[Vue.js] $refsでコンポーネント内の子要素を触る - Qiita](https://qiita.com/1994spagetian/items/5f372fc68122ec207c78)

> 同名コンポーネントは上書きされるとか

### 子

```vue
export default {
  name: 'ChildComponent',

  methods: {
    init: function(args){……}
```

### 親

```vue
<template>
  <div>
    <ChildComponent
      :prop1="param1"
      :prop2="param2"
      ref="ChildComponent"
    />
</template>

……

  methods: {
    callChild: function(){
      const args = ……
      this.$refs.ChildComponent['init'](args)
    },
```

## 子コンポーネントから親コンポーネントに渡す

### 子
- コンポーネント名は `name: 'ChildComponentName'`
- 親から渡してもらう引数は, props で定義する
- 親にデータを渡したい場合は, `this.$emit('event-name', data)` を実行する

### 親

```vue
<template>
  <div>
    <ChildComponentName
      :prop1="'文字列の場合は囲み忘れずに'"
      :prop2="boolVar"
      v-on:event-name="method1" // ★2 method1() でも method1(args) でもない
    />
  </div>
</template>

// ……

<script>
import ChildComponent from "@/path/to/ChildComponent.vue";

export default {
  name: 'ParentComponent',

  components: {
    ChildComponent // ★1 コンポーネントとしてロードする
  },

// ……

  methods: {
    method1: function(args){ // ★3 args に emit された data が入ってくる
      // よしなに
    },

```

## Invalid prop: type check failed for prop "propName". Expected Object, got Null
prop propName の初期値が、expect のものになってないのが原因。

- prop では Object にしているのに、data 側の初期値では null にしているとか
    - 正しくは `{}`

## Vue コンポーネントから setInterval を動かしたい
- this が Vue インスタンスを指してないので `bind(this)` すること.
- ちなみに clear しているのは全画面でタイマーが有効になったままなのを防ぐため
    - see1 [Vuejs ポーリングする時の注意点 - SIerだけど技術やりたいブログ](https://www.kimullaa.com/entry/2017/08/11/114059)
    - see2 [Vue.js のmountedでaddEventListenerやsetIntervalするとき、後始末を忘れない - GAミント至上主義](https://uyamazak.hatenablog.com/entry/2018/05/21/135729)

clock.vue

```
<template>
  <div>
    <p>{{ curdatetime }}</p>
  </div>
</template>

<script>
export default {
  name: 'clock',
  data: function() {
    return {
      curdatetime: '',
      interval_id: null
    }
  },
  mounted: function(){
    this.interval_id = setInterval(function(){
      let curdatetime = Date().toLocaleString()
      this.curdatetime = curdatetime
    }.bind(this), 250) // ★ここ!
  },
  beforeDestroy: function(){
    clearInterval(this.interval_id)
  }
}
</script>
```

[javascript - how to use setInterval in vue component - Stack Overflow](https://stackoverflow.com/questions/43335477/how-to-use-setinterval-in-vue-component)
