# mscorsvw.exe
- .NET Runtime Optimization Service
- .NET がらみの最適化処理を行うプロセスで、たまに動作して cpu ゴリゴリ削る
- タスクスケジューラはここ
    - `\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319`
    - `\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64`
    - `\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 Critical`
    - `\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64 Critical`
    - トリガーは空、操作もカスタムハンドラーでありいじれない
    - 無効にはできる
    - Critical？
        - Criticalはアクティブ時、無しはアイドル時に実行するみたい
        - [【 ディスク使用率100% 】.NET Runtime Optimization Service ( mscorsvw.exe ) が原因、対処法【 Windows10 】](http://dspckn.blogspot.com/2018/12/100-net-runtime-optimization-service.html)

## diary
- 2020/07/22
    - Critical は既に無効だった
    - .NET アプリあまり使ってないと思うし、無印も無効にしといた
    - 何よりアイドル時に勝手に動いてゴリゴリ鳴るのがうっとうしいので
