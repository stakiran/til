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
