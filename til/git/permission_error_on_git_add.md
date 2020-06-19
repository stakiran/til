# git add 時に permission error が出て add できない about pptxファイル

```
error: open("~$hogehoge.pptx"): Permission denied
```

対処:

- gitignore で `~*` を除外する

原因:

- office製品はファイル開いているときに `~filename` という一時ファイルをつくる
    - これが bind されてるせいで open に失敗しているのだと思われる
