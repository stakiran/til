# Javascript 非同期処理

# Promise の挙動を理解する
- [1.3. Promiseの書き方 - JavaScript Promiseの本](https://azu.github.io/promises-book/#how-to-write-promise)から拝借
- 同ページでコードも実行できるので、動かしてみるのもアリ

## 1

```js
function callback(resolve, reject){
  const req = new XMLHttpRequest();
  req.open("GET", URL, true);
  req.onload = () => {
    if (200 <= req.status && req.status < 300) {
      resolve(req.responseText);
    } else {
      reject(new Error(req.statusText));
    }
  };
  req.onerror = () => {
    reject(new Error(req.statusText));
  };
  req.send();
}

function fetchURL(URL) {
  return new Promise(callback)
}

const URL = "https://httpbin.org/get";
const promise = fetchURL(URL)
```

- Promise にはコールバック関数を渡す
    - このコールバック関数には (resolve, reject) という引数が渡されてくる
    - resolve オブジェクト「処理成功時には俺に値渡せや」
    - reject オブジェクト「処理失敗字は俺に値渡せや」
- new Promise(callback) しても、即座に関数 callback の処理結果が返されるわけではない
    - でも関数 callback はバックグラウンドで（非同期で）実行が走っている

:rabbit: 問題は、関数 callback の実行結果にどうやってアクセスするかということ

## 2

```js
function callback(resolve, reject){
  const req = new XMLHttpRequest();
  req.open("GET", URL, true);
  req.onload = () => {
    if (200 <= req.status && req.status < 300) {
      resolve(req.responseText);
    } else {
      reject(new Error(req.statusText));
    }
  };
  req.onerror = () => {
    reject(new Error(req.statusText));
  };
  req.send();
}

function fetchURL(URL) {
  return new Promise(callback)
}

function onFulfilled(responseText){
   console.log(responseText)
}

const URL = "https://httpbin.org/get";
const promise = fetchURL(URL)
promise.then(onFulfilled)

console.log('End Of Procedure')
```

> 関数 callback の実行結果にどうやってアクセスするか

- Ans: 関数 callback が **正常終了したときのコールバック関数** を定義しておく
    - このコールバック関数を onFulfilled と呼ぶ
- `promise.then(★ここに指定する)`

> Q: 正常終了した時に渡されてくる値は何？

- Ans: Promise callback の第一引数、resolve オブジェクトに指定した値
- `resolve(req.responseText)` なので、req.responseText

> Q: 正常終了した時に渡されてくる値はどこで受け取る？

- Ans: onFulfilled の第一引数

> Q: then(onFulfilled) の実行が、関数 callback が正常終了しちゃった後になったとしたらどうなるの？

- Ans: then(onFulfilled) を実行した直後に、onFulfilled が実行される
    - Promise さんは賢いので、早めに終了したとしても待機してくれている
    - で、onFulfilled がセットされてきたら「おう、終わってるぞ、ほらよ」と onFulfilled をコールしてくれる

> Q: responseText → End Of Procedure 、という順で実行されることはありえる？

- Ans: 関数 callback が一瞬で終わりそうだったらありえそうだが、実は **ありえない**
    - Promise は常に非同期で実行する仕様となっている
        - つまり `promise.then(onFulfilled)` 実行時に callback が終わっていたとしても、onFulfilled をその場で同期的に実行しない
        - いったんスルーして、バックで処理させる
        - (内部的には setTimeout をはさんでいるっぽい)
    - 詳細: [2.3. コラム: Promiseは常に非同期?](https://azu.github.io/promises-book/#promise-is-always-async)

## 長くて見づらいので端的に

```
function callback(resolve, reject){
  // args 使って処理する
  // 正常終了したら resolve(返したい値)
  // しくじったら reject(返したい値)
}

function promiseReturner(args) {
  return new Promise(callback)
}

function onFulfilled(valueFromResolve){
  // callback が正常終了した後の処理を書く
}

function onRejected(valueFromReject){
  // callback がしくじった後の処理を書く
}

args = データ
const promise = promiseReturner(args)
promise.then(onFulfilled).catch(valueFromResolve)

console.log('ここでいったん処理は終わるが, バックでは callback が動いてる')
```

# Promise chain

## 1

```js
function double_and_2sec(x) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x*2);
    }, 2000);
  });
}

function triple_and_1sec(x) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x*3);
    }, 3000);
  });
}

function plus10_and_100msec(x) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x+10);
    }, 100);
  });
}

function peak(x) {
    console.log(x)
    return x
}

const v = 1
const promise = Promise.resolve(v);
promise
  .then(double_and_2sec)
  .then(triple_and_1sec)
  .then(plus10_and_100msec)
  .then(peak) //16
  .then(plus10_and_100msec)
  .then(double_and_2sec)
  .then(peak) //52
```

- then に与える onFulfilled 関数が満たすべき性質
    - 1: promise オブジェクトを return すること
    - 2: 1 に与えるコールバック関数にて、（次のチェーンに繋ぎたい）値を resolve に渡すこと
- しかし、実は以下でもよい
    - 1: （次のチェーンに繋ぎたい）値を return すること
        - 内部的にはよしなに promise として処理してくれている
        - > returnした値は Promise.resolve(returnされた値); のように処理されるため、 何をreturnしても最終的には新しいpromiseオブジェクトを返します。
        - 参考: [2.4.2. promise chainでの値渡し](https://azu.github.io/promises-book/#ch2-promise.then)

## 2 await/async を使った場合

```js
function double_and_2sec(x) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x*2);
    }, 2000);
  });
}

function triple_and_1sec(x) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x*3);
    }, 3000);
  });
}

function plus10_and_100msec(x) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x+10);
    }, 100);
  });
}

function peak(x) {
    console.log(x)
    return x
}

async function user(){
    let v = 1
    v = await double_and_2sec(v)
    v = await triple_and_1sec(v)
    v = await plus10_and_100msec(v)
    v = await peak(v) //16
    v = await plus10_and_100msec(v)
    v = await double_and_2sec(v)
    v = await peak(v) //52
    return v
}

user()
```

- async function という「非同期処理を同期的に並べられるエリア」をつくる
    - この中で、同期的に並べたい非同期処理を await で呼び出していく

# 参考文献
- [JavaScript Promiseの本](https://azu.github.io/promises-book/)
    - これが一番わかりやすい
- [Promise - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    - 端的に思い出したい場合
- [Repl.it - Online JavaScript Compiler - Fast, Powerful, Free](https://repl.it/languages/javascript)
    - コード書いて試したいならここで
