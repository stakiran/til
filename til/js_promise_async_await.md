# Javascript 非同期処理

## とりあえず最低限の知識
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
