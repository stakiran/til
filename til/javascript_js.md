# Javascript

## ●配列

```
var array = [];
array.unshift(...)     // prepend
array.push(...)        // append
array.length           // 長さ
array.shift()          // 先頭削除

// 走査
for(var i=0; i<array.length; i++){
  var elm = array[i];
}
// es6
for(const cardName of listByArray) {
    cardDisplay.add(cardName);
}
```

## `increment({ commit }){ commit('increment')}` ← 引数の `{}` 囲みはなんですか
ES2015 の引数分割束縛

- 以下を二つとも満たす
    - 1 関数 f の定義時に引数 param を `{param}` と書く
    - 2 呼び出し元では、f に「param を持つオブジェクト obj1」を与える
- すると、f の内部では param の部分が obj1.param と補われる

つまり obj1.param obj1.param obj1.param と何度も書くところが、param だけで済む。

読み方としては、`f({param})` は、**fの第一引数に渡されたxxxのうち、param プロパティについては、関数内で xxx. を省略できまっせ** ← こんなイメージ。

```
// caller

increment(context)

===

// callee
increment ({ commit }) {
  commit('increment')
}
```

- [ES2015 の引数分割束縛（argument destructuring）とは？ | 世界を変える男-やまだたろう-](https://sekaiokaeru.com/tips/javascript-argument-destructuring)
    - この記事がわかりやすかった
- [波括弧で引数をくくる「引数分割束縛」について - Qiita](https://qiita.com/nayucolony/items/0b9b0d6c8d968481c6fb)


## `obj = {[prop]: 'hey'}` この `[]` 囲みはなんですか
動的プロパティ。

`[xxx]` と書くと、xxx に入ってる値をプロパティ名として使える。

- [オブジェクト初期化子 - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Object_initializer)
    - ES2015より
- [ミューテーション | Vuex](https://vuex.vuejs.org/ja/guide/mutations.html)
    - mutation type を定数で並べるという手法もあるらしい

## `x => y => z` みたいにアローが連続しているのは何？
[JavaScript - ES6の文法でわからないところが｜teratail](https://teratail.com/questions/71006)

カリー化。

```
const f = x => y => z => x + y + z;
console.log(f(1)(2)(3));

  ↓ このように展開される

const f = (x) => {
  return (y) => {
    return (z) => {
      return x + y + z;
    };
  };
};

  ↓ ES5 では

var f = function f(x) {
  return function (y) {
    return function (z) {
      return x + y + z;
    };
  };
};
```

……わからん。暗記しても良いが、原理理解したい。C言語のポインタのポインタのポインタ的なのを思い出す……

### 一般化する

```
const f = x => y => z => x + y + z;
          ^^^^^^    ^
          1         2

1 アローの右側にある引数
2 最後のアローの右側にある引数

2 の本体にて、1 と 2 すべて使った処理を書く。
```

### 原理を自力で理解する

```
const f = x => y => z => x + y + z;

  ↓

const f = x => YYY; // YYY は y => z => x + y + z;

  ↓

var f = function f(x){
  YYY
}

  ↓

var f = function f(x){
  function(y){
    ZZZ             // ZZZ は z => x + y + z;
  }
}

  ↓

var f = function f(x){
  function(y){
    function(z){
      x + y+ z
    }
  }
}

  ↓ 本体が一行の場合、return が補われるの今知ったので、こうですね

var f = function f(x){
  return function(y){
    return function(z){
      return x + y + z
    }
  }
}

===== あとは、カリー化を復習するのみ =====

var a = f(1) すると？

    a = return function(y){
      return function(z){
        return 1 + y + z
      }
    }

    ↑こうなる

   つまり第一引数を 1 で固定した感じ

同様に var b = a(2) は？
あるいは var b = f(1)(2) でもいいけど

    b = return function(z){
      return 1 + 2 + z
    }

    ↑こうなる
```

## `...` とはスプレッド演算子
[スプレッド構文 - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

```
function sum(x, y, z) {
  return x + y + z;
}
const numbers = [1, 2, 3];
console.log(sum(numbers));    // "1,2,3undefinedundefined"
console.log(sum(...numbers)); // 6
```

- Python でいう `*args` や `**kwargs` みたいなもの
- js のスプレッド演算子ではリストもオブジェクトも同じ `...` でいける

## アロー関数
- `function(args){...}` を `(args) => {...}` と書ける
- 省略
    - 処理が一行の場合、`(args) => procedure` を略してもいい
    - 引数が一つの場合、`arg => {}` とカッコなしでもいい
    - 引数も処理も一つの場合、`arg => procedure` だけで済むことになる
    - 引数がない場合、`() => {...}` と空かっこだけ書く
- return の省略
    - 処理が一行の場合、return が自動で補われる
    - 例1:
        - ES6: `(args) => {expression}`
        - ES5: `function(args){return expression}`
    - 例2: 全部省略場合
        - ES6: `arg => expression`
        - ES5: `function(arg){return expression}`
- this
    - `var self=this;` が自動で補われる感じ
    - 他のプログラミング言語みたくレキシカルな挙動で使えるよ？

[JavaScript アロー関数を説明するよ - Qiita](https://qiita.com/may88seiji/items/4a49c7c78b55d75d693b)

## var let const
定数は const で良い。

let はローカルスコープ持ちで自然。

- var は従来のもの。再代入ok、再宣言ok。ブロックスコープなし
- let は var に加えて再宣言禁止＋ブロックスコープあり
- const は let に加えて再代入も禁止

[JavaScriptで書く「let,var,const」の違い・使い分け | TechAcademyマガジン](https://techacademy.jp/magazine/14872)

## CSV ファイルダウンロード(jQuery版)
blob をつくった後、a要素のdownload属性をclick発火で発動させる。

```
$(function(){

    // @param data ダウンロードさせたい文字列データ
    // @param filename ダウンロード時のファイル名
    function start_download(data, filename){
        // Excel で BOM 無しの UTF-8 CSV ファイルを開くと文字化けするので
        // 明示的に BOM を付けておく.
        // (Excel は BOM が付いてると UTF-8 を正しく認識できる.)
        var bom  = new Uint8Array([0xEF, 0xBB, 0xBF]);

        var blob = new Blob(
            [bom, data],
            {"type" : "text/csv"}
        );

        var downloadee_filename = filename + '.csv';

        if (window.navigator.msSaveBlob) {
            // IE には msSaveBlob という簡単にダウンロードを実現する仕組みがある.
            window.navigator.msSaveOrOpenBlob(blob, downloadee_filename);
        } else {
            // IE 以外

            var blob_url = window.URL.createObjectURL(blob);

            // HTML5 の A 要素 download 属性を用いる.
            // ただし A 要素はこのタイミングで動的に生成する.

            var a_element = document.createElement('a');
            a_element.download = downloadee_filename;
            a_element.href = blob_url;
            a_element.id = 'csv_download_temp';
            var a_jquery_obj = $(a_element);

            // 実際に append で追加してやらないと A 要素の click が効かない
            $('body').append(a_jquery_obj)
            a_jquery_obj[0].click();
            // ダウンロード後はもう要らないので消す.
            a_jquery_obj.remove();
        }
    }
});
```

## random 乱数

Math.random() が基本だから 0-1 float なので少し加工が必要.

拝借: https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Math/random

```
get_random_number_0_to_x: function(x) {
  min = 0
  max = Math.floor(x)
  return Math.floor(Math.random() * (max - min)) + min
},
```

## string reverse

```
var reversed_message = this.message.split('').reverse().join('')
```

string 自体は reverse() を持たないので、いったん array にしてから。
