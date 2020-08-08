# storsvc.exe 高速スタートアップ

停止方法

- 電源オプション > 電源ボタンの動作を選択する > 現在利用可能ではない設定を変更します
- レジストリならここ
    - HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power
    - HiberbootEnabled
    - 0なら無効

日記

- 2020/08/05
    - 停止してるのに storsvc.exe 動いてやがった、アイドル状態に
    - 高速スタートアップちゃうわ
        - 元記事 [Windowsのサービス「StorSvc」って具体的には何をしているのでしょう... - Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14180953624)
        - これ鵜呑みにしすぎた
        - 高速スタートアップと相性悪いかもってだけで
    - storage service？
        - [【Windows 10】 Storage Service サービス起動の必要性 | 個人PCの性能とセキュリティ向上](http://tooljp.com/Windows10/doc/Service/Storage_Service.html)
        - >ストレージ設定と外部ストレージの拡張を有効にするためのサービスを提供します
        - 停止していいか微妙なライン……
        - 調べても出てこない
        - ……やめとく
