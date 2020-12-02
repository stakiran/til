# Javascript 非同期処理
マジでピンと来なくてヒーヒー言ってる。

- [Repl.it](https://repl.it/languages/javascript) で MDN のコードをいじりながらすると理解が捗る

# 非同期処理をチェーンさせたい場合

## async/await で書く場合

```js
function f1(value) {
    return new Promise(resolve => {
        setTimeout(() => {
            const result = value*2
            resolve(result);
        }, 1000);
    })
}

function f2(value) {
    return new Promise(resolve => {
        setTimeout(() => {
            const result = value*10
            resolve(result);
        }, 1000);
    })
}

function f3(value) {
    return new Promise(resolve => {
        setTimeout(() => {
            const result = value*value
            resolve(result);
        }, 1000);
    })
}

async function sample() {
    const f1_result = await f1(5);
    const f2_f1_result = await f2(f1_result)
    const f3_f2_result = await f3(f2_f1_result)
    const result = f3_f2_result
    return result;
}

sample().then(result => {
    console.log(result); // 約3秒後に 10000
});
```

# 非同期処理を待たせたい場合の async await の書き方
from [async/await 入門（JavaScript） - Qiita](https://qiita.com/soarflat/items/1a9613e023200bbebcb3)

まとめると

- 1 そもそも非同期処理が promise を返すようになっていること
- 2 待たせたい非同期処理 f のラッパーをつくる
    - async function としてつくる
- 3 async function ラッパーの中で、1の処理を呼び出す
    - このとき await をつける
- 4 呼び出し元では、2 のラッパーの then() にて、待たせた後の続きを書く

## 1 普通に書くと
> 普通にやろうとすると
>
> value is [object Promise] ← 10 が入るはず

↑ こうなる。待たれない。

```
// しばらくしてから結果が返ってくる, promise を返す関数
// (ここでは2秒後に value を 2 倍にした値が返ってくる)
function sampleResolve(value) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(value * 2);
        }, 2000);
    })
}

console.log('普通にやろうとすると')
const value = sampleResolve(5)
console.log(`value is ${value} ← 10 が入るはず`)
```

## 2 async/await で書くと？
2秒経った後に

> 10

こうなる。ちゃんと待ってくれる。

```
// しばらくしてから結果が返ってくる関数
// (ここでは2秒後に value を 2 倍にした値が返ってくる)
function sampleResolve(value) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(value * 2);
        }, 2000);
    })
}

async function sample() {
    const result = await sampleResolve(5);
    return result;
}

sample().then(result => {
    console.log(result);
});
```

# await なくても非同期処理書けるけど、なんで必要なの？
Ans: その非同期処理で結果が出るまで待たせるために必要

[await - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/await) の「promiseの解決を待つ」より

await がある場合。

- resolveAfter2Seconds という非同期処理で結果が出るまで待つので、2秒後に 10 が print される

```
function resolveAfter2Seconds(x) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x);
    }, 2000);
  });
}

async function f1() {
  var x = await resolveAfter2Seconds(10);
  console.log(`Output: ${x}`); // 10
}

f1();
```

await がない場合。

- console.log が即座に `Output: [object Promise]` となる
- 2秒後に処理が終了する
- 待てない

# ==== 理解編 ====

## つまり非同期って？
- いつ終わるかわからない処理を、同期的に直感的に書けるようにしたい
- 2020 年現時点では、promise/async/await 

## Q: promise とは何を返すもの？
Ans: 未来のある時点で値を持つオブジェクト

[Promise - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise)

> これにより、非同期メソッドは、最終的な値を返すのではなく、未来のある時点で値を持つ Promise を返すことで、同期メソッドと同じように値を返すことができるようになります。

**未来のある時点で値を持つ Promise**。

### Q: promise は値を持っていない時はどうなるの？
Ans: 別にどうもならない。

```
obj = axios.get(……)
```

この obj は promise オブジェクトであり、get した結果が代入されたり、後から代入されたりすることはない。あくまでも obj には promise オブジェクトが入っているだけ

### Q: じゃあ値が入る時はどこで受け取るの？
Ans: then() で指定したコールバック関数

## Q: promise チェーンって何なの？
azu さんの本が一番わかりやすかった

- https://azu.github.io/promises-book/#chapter2-how-to-write-promise
- 2.4.1. promise chain

つまり

- then() のチェーンは順に呼ばれます
- ただし以下はチェーンの最後に一度定義するだけでいいです
    - catch
    - finally(最後のthen)
        - `….catch().then()` でも `….then().catch()` でもいい
- then(a).then(b) で a から b に値を渡すには、a で return し、b の引数で受け取ります
    - もっというと new Promise 時にわたす `resolve(xxx)` も、xxx を return している
- チェーンで繋げることを前提とした関数をつくる場合、then() の結果を return するつくりにする
    - :x: `return promise;`
    - :o: `return promise.then(…)`

## Q: then() は何を返す？
Ans. Promise

[Promise.prototype.then() - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)

## コールバック地獄とは

### 2 waitからの例(2013年だが)
[JavaScriptとコールバック地獄 - Yahoo! JAPAN Tech Blog](https://techblog.yahoo.co.jp/programming/js_callback/)

- js には sleep がなく、setTimeout で頑張る必要がある
- 処理1, sleep1, 処理2, sleep2 ……これだけでも setTimeout のネストにならざるをえない

コールバック地獄から逃れる手段はないの？

- ないです
- 理論的に無理です
    - 非同期したいなら「処理が終わったら実行する関数」 ← これを定義するというアプローチしかありえない
    - つまり「処理が終わったら実行したい関数」を一つ定義するのに、関数一段分のネストが必要
- :rabbit: 詳しい理論や証明はわからんが、まあ情報工学的にも無理なんだろうと思われる

2013年時点では以下があった

- yeild による一時停止
    - いわゆる generator
    - yield 実行語、呼び出し元で next() が呼ばれるまで待機する
    - つまり
        - 並列処理の羅列は yeild はさみながら定義して、
        - 呼び出し側で、next() の呼び出し方をコントロールすることで順に実行していく
- jQuery.Deferred

### 1 ファイル読み込みからの例
[コールバック地獄からの脱出 - Qiita](https://qiita.com/umeko2015/items/2fdb2785eac8f4117f23)

> 例えば、複数のデータの読み込みが完了してから読み込んだデータに対して処理をかけたいという場合

- fs.readFile(filename, funcAfterLoading)
    - 読み込み終えた後の処理を funcAfterLoading に指定
- ゆえに「data1 → data2 → data3 の順で読みたい」場合にネスト地獄になる

```
fs.readFile('data1.txt', function(data1) {
     fs.readFile('data2.txt', function(data2) {
         fs.readFile('data3.txt', function(data3) {
             fs.readFile('data4.txt', function(data4) {
                 fs.readFile('data5.txt', function(data5) {
                     console.log(data1 + data2 + data3 + data4 + data5);
                 })
             })
         })
     })
 })
```

これが最終的には以下のようにシーケンシャルに書ける

```
async function readFiles() {
    let data1 = await readFile('data1.txt');
    let data2 = await readFile('data2.txt');
    let data3 = await readFile('data3.txt');
    let data4 = await readFile('data4.txt');
    let data5 = await readFile('data5.txt');
    console.log(data1 + data2 + data3 + data4 + data5);
}

readFiles()
.catch(error) {console.log(error)}
```

この過程で色々悩み書いてあるが、まだわからん……（`_dataX` は `_data` みたいに同名で良い気がする）

## 最低限2 MDN
- Promise チェーンのところから一気にわからん
    - doSomething じゃなくてもっとわかりやすい例にしてほしい
    - Audio処理の例で説明してほしい
    - そもそも「コールバック地獄」がピンと来ない

===

[Promiseを使う - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Using_promises)

```
createAudioFileAsync(audioSettings, successCallback, failureCallback);

//  ↓ これがこうなる

createAudioFileAsync(audioSettings).then(successCallback, failureCallback);

//  ↓ 略さずに書くとこう

const promise = createAudioFileAsync(audioSettings); 
promise.then(successCallback, failureCallback);
```

## 最低限1 Promiseの本
[JavaScript Promiseの本](https://azu.github.io/promises-book/#chapter1-what-is-promise)

登場人物

- Promise
    - 非同期処理を抽象化して上手いこと扱う仕組み
    - 使い方がちょっとむずい
- async
    - Promise 使って非同期関数を実現する
- await
    - async 関数内で使える「この処理が戻ってくるまで待ちまーす」的な宣言

歴史

- もともとコールバック関数で非同期処理していたが、好き勝手かけるのでごっちゃ
- Promise という統一的なやり方が整備された
- まだ書き方ちょっとだるいので、async/await という簡単に書ける書き方が使えるようになった
    - ので Promise の知識が前提として必要

Promise の定義と実行

```
function fetchURL(URL) {
    // ★ 以下は定型句
    //    return new Promise((resolve, reject){……}
    return new Promise((resolve, reject) => {
        const req = new XMLHttpRequest();
        req.open("GET", URL, true);
        req.onload = () => {
            if (200 <= req.status && req.status < 300) {
                // ★ 処理が成功して return したい場合、こう書け
                //    return xxx
                //    ↓
                //    resolve(xxx)
                resolve(req.responseText);
            } else {
                // ★ 処理が失敗して fail したい場合、こう書け
                //    throw new Error(xxx)
                //    ↓
                //    reject(new Error(xxx))
                reject(new Error(req.statusText));
            }
        };
        req.onerror = () => {
            reject(new Error(req.statusText));
        };
        req.send();
    });
}

// 実行例
const URL = "https://httpbin.org/get";
// ★ promise.then(onFulfilled, onRejected)
//    これの onfullfileed と onRejected を定義すべし
//
// promise.then(onFulfilled)
// promise.then(onFulfilled).catch(onRejected)
//   → メソッドチェーンになるのでこっちがちょっとスッキリする
//      catch(xxx) は then(undefined, xxx) の糖衣構文
fetchURL(URL).then(function onFulfilled(value){
    console.log(value);
}).catch(function onRejected(error){
    console.error(error);
});
```

Thenable

- VSCode 拡張機能でちょい見かけたのでついでに
- then() を持つ、Promise でないオブジェクトのこと
- Thenable であるとは **Promise オブジェクトと同じように使えますよ** の意
