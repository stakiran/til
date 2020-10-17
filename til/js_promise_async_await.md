# Javascript 非同期処理
マジでピンと来なくてヒーヒー言ってる。

## つまり非同期って？
- いつ終わるかわからない処理を、同期的直感的に書けるようにしたい
- 2020 年現時点では、promise/async/await 
- promise
    - :rabbit: ここがマジでわからん
    - コード見てて promise が出たら「ウッ」てなる
    - 「えーっと、promise は resolve と reject を指定するやつで、……」 ← こうなる
    - 毎回頭パンクして先に進めん
    - 「こういうことなんだよ」とスッと理解できる解釈が欲しい
    - `promise.then(A,B).then(C,D).then(E,F)`
        - もっというとこれをすんなり理解する解釈

## promise とは何を返すもの？
Ans: 何も返しません（と理解した方がわかりやすそう）

- :x: ~~その場で何らかの値やオブジェクトが戻ってくる~~ この発想はやめよ
- :o: promise をつくってる ← 非同期な処理を **セットしていったん放置する**、と考える

## promise チェーンって何なの？
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
    - もっというと new Promise 時にわたす  `resolve(xxx)` も、xxx を return している
- チェーンで繋げることを前提とした関数をつくる場合、then() の結果を return するつくりにする
    - :x: `return promise;`
    - :o: `return promise.then(…)`

## then() は何を返す？
Promise

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
        - 

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
- ちょっと重い


===

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
