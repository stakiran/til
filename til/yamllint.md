# yamllint
yamllint ./

## windows で実行するには
> UnicodeDecodeError: 'cp932' codec can't decode byte 0x86 in position 47: illegal multibyte sequence

このエラーが出るので、`set PYTHONUTF8=1` を実行する。

(メモ) Python のデフォエンコーディングは（open 関数なので明示的に encoding 引数に指定していなければ）windows では cp932 になる。で、yamllint は日本語想定してなくて明示的指定していないので、このエラーで死んでいた。
