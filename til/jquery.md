# jQuery

## テンプレ

```
$(function(){
    function func1(){
    }

    $("#button_hoge").click(function(){
        func1()
    });
});
```

## 動的に追加された要素のイベントも発火 / 
[html - Jquery click event not working after append method - Stack Overflow](https://stackoverflow.com/questions/15420558/jquery-click-event-not-working-after-append-method)

```
// #cardContainer は ul
$('#cardContainer').on('click', 'li', function(){
    let jqElement = $(this);
});
```

## on で取得した click の要素が何番目かを取得する
index() で照合できる。

```
// #cardContainer は ul
$('#cardContainer').on('click', 'li', function(){
    let jqElement = $(this);
    const idx = $('#cardContainer > li').index(this); // ★要素が n 個並ぶセレクタの書き方じゃないとダメ
    console.log(`idx: ${idx}`);
    console.log(jqElement);
});
```

## pタグにテキストを入れる

```
$('p_tag_selector').text(hogestr);
```

## 0番目の要素だけ remove

```
cur_selectbox.children('option').eq(0).remove();
```

## 複数要素の値をまとめてクリア(inputなど)

```
$('input').each(function(idx, dom){
    $(dom).val('');
});
```

## filter による and 検索、大文字小文字無視検索

```
// AND 検索したいキーワードが配列で返ってくるとする
var keywords = split_search_query(this.value);

// :contains フィルタは大文字小文字区別するので
// filter 関数で頑張る.
// filter 関数は、マッチするパターンについて return true を返す、という使い方
var count = $('#search_target_area .entry').filter(function(){
    var text = $(this).text().toLowerCase();
    var are_all_included = true;
    for(var i=0; i<keywords.length; i++){
        var keyword = keywords[i].toLowerCase();
        if(text.indexOf(keyword) == -1){
            are_all_included = false;
            break;
        }
    }
    return are_all_included;
}).show().length;
```

## contains による and 検索, or 検索
from https://stackoverflow.com/questions/2416803/jquery-contains-selector-to-search-for-multiple-strings

```
$('li:contains("mary"), li:contains("john")'). // either mary OR john
$('li:contains("mary"):contains("john")'). //li, which contains both
```

## クラス名を動的に追加する
`$li.addClass("toc-sub");`

## title属性に動的に入れる
`$(target_id).prop("title", text);`

## 他ページを動的に取得する

```
<html>
<head>
<title>ヘルプの文言を動的に取ってくるサンプル</title>
<meta charset="UTF-8">
<script src="./lib/js/jquery-3.2.1.min.js"></script>
<script type="text/javascript">
function get_and_callback(url, callback){
    //var response = $.get(url, callback);

    var response = $.ajax({
        url: url,
        type : 'GET',
        dataType: "text",
        success: callback
    });
}
function redraw(data){
    console.log(data)
    $("#result").text(data);
    //$("#result").html(data);
}
$(function(){
    $("#getter").click(function(){
        get_and_callback("help.html", redraw)
    });    
});
</script>
</head>
<body>
<button id="getter">get</button><br>
<hr>
<pre id="result">
</pre>
</body>
</html>
```

ただし IE11 だと DOM7011 が出て取得できない。ハマリポイント多そう…… at 2018/04/16

## クリップボードに文字列コピー

```
$(function(){
    function do_copy(){
        // [1/2] コピーしたい文字列を用意して,
        var data = "title,,\n" +
                   "col1, col2, col3\n" +
                   "name1, val1, val2\n"
        console.log(data);

        // [2/2] document.execCommand('copy') を使ってコピー.
        // ただし「選択中のテキストがコピーされる」という仕様なので,
        // テキストエリアを作って、そこにコピー文字列を入れ、全選択をさせている. 
        $('body').append('<textarea id="clipboardcopyworkarea" style="" />');

        // これ(最初から display:none でテキストエリアを非表示にしとく)だと動作しない.
        // 実際は一瞬で表示→消去となり人間の目には見えないので問題ないと思う.
        //$('body').append('<textarea id="clipboardcopyworkarea" style="display:none;" />');
        $('#clipboardcopyworkarea').val(data).select();
        document.execCommand('copy');
        $('#clipboardcopyworkarea').remove();
    }

    $("#button_copy").click(function(){
        do_copy()
    });
});
```

## selectbox combox コンボボックス操作

```
<html>
<head>
<meta charset="UTF-8">
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="./utils.js"></script>
<script type="text/javascript">
function append_to_selectbox(select_jobj, value, itemname){
    select_jobj.append($('<option>').html(itemname).val(value));
}
$(function(){
    $("#toselect_get").click(function(){
        var got_value = $('#selectbox1').val();
        c(got_value)
    });

    $("#toselect_set").click(function(){
        $('#selectbox1').val("abc");
    });

    $("#toselect_set_by_index").click(function(){
        $('#selectbox1').prop("selectedIndex", 0); //先頭要素(index=0)を選択
    });

    // selectbox自体の編集.
    // 普通にhtmlをいじってやればよい.
    $("#toselect_update").click(function(){
        var value = 'hoge';
        var showstr = '新しく追加した項目です!';
        append_to_selectbox($('#selectbox1'), value, showstr)
    });

    // 選択肢変更時に実行するイベント.
    $('#selectbox1').change(function(){
        var selected_value = $('#selectbox1').val();
        var selected_itemname = $('#selectbox1 option:selected').text();
        c('selected value    : ' + selected_value)
        c('selected itemaname: ' + selected_itemname)
    });

});
</script>
</head>
<body>
<select id="selectbox1">
    <option value=1>値:1</option>
    <option value="1">値:"1"</option>
    <option value="abc">値:"abc"</option>
    <!-- selected="selected" でデフォルト値 -->
    <option value="あいうえお" selected="selected">値:"あいうえお"</option>
</select>
<br>
<button id="toselect_get">選択された値を取得</button><br>
<button id="toselect_set">指定した値を選択</button><br>
<button id="toselect_set_by_index">指定した値を選択(index値を使用)</button><br>
<button id="toselect_update">内容を更新する(append)</button><br>
</body>
</html>
```

## チェックボックス checkbox 操作

```
<html>
<head>
<meta charset="UTF-8">
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="./utils.js"></script>
<script type="text/javascript">
function is_checked(checkbox_dom){
    if($(checkbox_dom).prop('checked')){
        return true;
    }
    return false;
}
function do_check(checkbox_dom){
    $(checkbox_dom).prop('checked', true);
}
function do_uncheck(checkbox_dom){
    $(checkbox_dom).prop('checked', false);
}

$(function(){
    // 選択肢変更時に実行するイベント.
    // コードから .prop で変更した場合は呼ばれない.
    $('#checkboxes1 input').change(function(){
        var thistext = $(this).attr('value');
        var outmsg = thistext;
        if(is_checked(this)){
            outmsg += ' to be ON!';
        }else{
            outmsg += ' to be OFF!';
        }
        c(outmsg);
    });

    // checkboxの情報をひと通り取得
    $('#get_checkbox_info').click(function(){
        var target = $('#checkboxes2 input:eq(0)');
        c('checkされてる? > ' + is_checked(target));
        c('name/value => ' + target.attr('name') + '/' + target.attr('value'));
        c('.val() means value attribute => ' + target.val());
        c('表示文字列を直接取得する手段はない .text()/.html() =>' + target.text() + '/' + target.html());
    });

    // チェックボックス反転 = 状態判定 + 状態変更
    $('#toggle_checkboxes').click(function(){
        $('#checkboxes1 input').each(function(i, elm){
            if(is_checked(elm)){
                do_uncheck(elm);
            }else{
                do_check(elm);
            }
        });
    });

});
</script>
</head>
<body>
チェックボックス 複数
<form id="checkboxes1">
    <input type="checkbox" name="id1" value="this_value_will_be_post1">選択肢1
    <input type="checkbox" name="id1" value="this_value_will_be_post2">選択肢2
    <input type="checkbox" name="id1" value="this_value_will_be_post3" checked>選択肢3
</form>
チェックボックス 単一
<form id="checkboxes2">
    <input type="checkbox" name="id2" value="on_or_off">有効/無効
</form>
<br>
<button id="get_checkbox_info">単一チェックボックスの情報を取得する</button><br>
<button id="toggle_checkboxes">複数チェックボックスのチェック状態を反転する</button><br>
</body>
</html>
```

## escキーの押下を検出する

```
$("body").keypress(function(e){
    var keycode = e.keyCode;
    // Esc
    if(keycode == 27){
        sort_textarea(textarea);
    }
});
```

keypress だと文字キーは検出できないので keydown を使うこと in Firefox 55

## textarea がフォーカスされたら全選択する

```
$('#searchbox').focus(function(){
    $(this).select();
});
```

## ダブルクリック検出

```
$('body').dblclick(function(){
    $('#searchbox').focus();
});
```

## textarea のクリア

```
$('textarea').val('')
```

## textarea への append/prepend

```
var txt = $("textarea#idhere");
txt.val( txt.val() + "\nSomething here\n\nAgain");
```

要するに val() で取得した値に対してprependなりappendなりして、それを val(ここに渡す) ことで反映する。

from http://stackoverflow.com/questions/2159622/jquery-textarea-append-newline-behavior

## 擬似的にクリックさせる

```
$('#some_element').click();
```

どの要素に click イベントを実行させればよいかは対象次第なので、親要素や子要素を試してみるなど試行錯誤が必要かもしれない。

## appendとprepend
htmlタグ内の先頭に p タグを入れる。

`$('html').prepend("<p>hogehoge!</p>");`

## eachによる繰り返し ループ

```
// i と elm を受け取れる.
// elm は DOM オブジェクトなので $(elm) にしないと jQuery obj にならない.
$("#mytable tr").each(function(i, elm_trs){
    $(this).children("th").each(function(i, elm_ths){
        if(i==target_column_index){
            toggle_display($(elm_ths));
        }
    });
});

return true;  で continue、
return false; で break
```

## ReferenceError: $ is not defined
jquery が上手く読み込まれていない。

- jqueryを一番最初に読み込む
- urlやパスが正しいか調べる
- http://… ではなく //… と書いている
