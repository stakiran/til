# Vue.js

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
