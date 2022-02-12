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

## ●アロー関数

### ケース別
tested with [Repl.it](https://repl.it/languages/javascript).

```js
assert = console.assert

// 引数が二つ以上で、処理が二行以上の場合,
// (引数) => {処理} になる.
f = function(a,b){
    var ret=a+b
    return ret
}
a = (a,b) => {var ret=a+b; return ret;}
assert(f(1,100)===a(1,100))

// 処理が一行の場合, 右辺の {} は省略できる.
// ただし return は省略できない
f = function(a,b){
    return a+b
}
a1 = (a,b) => {return a+b}
a2 = (a,b) => a+b
a3 = (a,b) => {a+b}
assert(f(1,100)===a1(1,100))
assert(f(1,100)===a2(1,100))
assert(undefined===a3(1,100))

// 引数が一つの場合, 左辺の () は省略できる.
f = function(a){
    var ret = a+100
    return ret
}
a1 = (a) => {var ret=a+100; return ret;}
a2 = a => {var ret=a+100; return ret;}
assert(f(1,100)===a1(1))
assert(f(1,100)===a2(1))

// 処理が一行で、引数が一つの場合,
// 左辺の () も 右辺の {} も省略できる
f = function(a){
    return a+100
}
a1 = (a) => {return a+100}
a2 = (a) => a+100
a3 = a => {return a+100}
a4 = a => a+100
assert(f(1,100)===a1(1))
assert(f(1,100)===a2(1))
assert(f(1,100)===a3(1))
assert(f(1,100)===a4(1))
```

### 一般論
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

## URL Parameter

```js
class URLParameter{
    // @param queryString とりあえずlocation.searchを想定。
    constructor(queryString){
        this._dict = {}
        this._raw = queryString;
        if(this._raw==''){
            return
        }

        const withoutQuestion = queryString.substring(1);
        const parameters = withoutQuestion.split('&');
        for(var i=0;i<parameters.length;i++){
            const kvs = parameters[i].split('=');
            const key = kvs[0];
            const value = kvs[1];
            this._dict[key] = value;
        }
    }

    printAll(){
        for(const [k, v] of Object.entries(this._dict)){
            console.log(`${k}=${v}`)
        }
    }
}
```

## クラス定数

```js
class Class1{
    static get CLASSVAR1(){
      return 'クラス定数1'
    }
}
```

呼び出す時:

- :o: Class1.CLASSVAR1
- :x: this.CLASSVAR1
- :x: class.CLASSVAR1

## const a,b = getTuple() 的なことがしたい 分割代入

```js
// func は [str, str] を返すとする「
const [a, b] = func()
```

- 参考: [分割代入 - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
    - 他にも rest 的にまとめたり、要らんの切り捨てたりもできるっぽい

## object を extend したい(deep merge)したい
- 無理です
- shallow merge なら `const merged = Object.assign(a, b)` でいける

## クラスのインスタンスメソッドを promise chain に渡してる場合に、this が undefined になる件
呼び出し元で .bind(this) して束縛する

```js
class{
  // ……
  method(){
    const promise = this._method1()
      .then(this._method2)
      .then(this._method3.bind(this))
  }
  // ……
```

参考: [クラス内のPromiseでundefined - Qiita](https://qiita.com/takoji3/items/35e72f19f68a50f1b323)

## template string テンプレート文字列の中でバッククォート使いたい
普通にエスケープしたらいける

```js
readme_md=`# xxx

how to use

\`\`\`
$ hoge --input fuga.txt
\`\`\`

```

## object を走査(for .. of)したい
他にもある

- [JavaScriptで配列やオブジェクトをループする良い方法を真剣に検討してみた - Qiita](https://qiita.com/endam/items/808a084859e3a101ab8f)

### Array.forEach

```js
Object.keys(obj1).forEach(
    (key) => {
        ……
    }
)
```

- Q: continue したい
    - return

## セミコロン ; は必要ですか？
- 無くても動くが……
    - 意図しない連結のされ方をすることがあってハマりがちな
    - `addfunc = (a,b) => {const ret=a+b; return ret;}` など、一行で複数文書きたい時には必須
- ハマるの防ぎたいなら、ちゃんと付けるのが確実
- ESLint などで制限するのもアリ

## named export と default export
default export

- export default する側では「デフォルト空間」に export していく
- import する側では `import 名前 from インポート先` で、インポート先のデフォルト空間に名前でアクセス
    - python の import と同じ挙動

named export

- export する側では `export 名前` で個別に export していく
- import する側では `import {名前} from インポート先` で、インポート先から個別の名前を import する

詳しくは

- [export - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Statements/export)
- [import - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Statements/import)

### 問題1: export したオブジェクトを import したら undefined になってる件
options.js

```
……
const options = new Option(……);

export { options }
```

:x: import する側（undefinedになるパターン）

```
import options from "@/options.js";
```

:o: import する側（正しい）

```
import {options} from "@/options.js";
```

解説:

- export する側では named export している
- named export したものを import する構文は `import {名前}`
- `import 名前` は、インポート先のデフォルトを読み込むって挙動になる
    - が、options.js では export default はしてないので undefined

## `@` is 何？
- webpack の記法で、`src/` で置き換える（ことが多い）。

## `increment({ commit }){ commit('increment')}` ← 引数の `{}` 囲みはなんですか
ES2015 の引数分割束縛

- `f({param})` とは
    - `f` の第一引数に渡された `xxx` のうち、`param` だけを取り出している
    - xxx のうち、param だけを使いたい場合に便利

- 普通
    - `f(xxx){……xxx.param……}`
- 引数分割束縛
    - `f({param}){……param……}`

see:

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
