# MsMpEng.exe
- ~~Microsoft Antimalware Service~~ 古い情報であり win 10 1809 では該当しない
- 詳細は [windows_defender.md](windows_defender.md) を参照
- ここは MsMpEng.exe というプロセスが絡むネタのみ扱う

## リアルタイム保護オフってるのに MsMpEng.exe が出てくるんですけど
- オフにしても即時反映されない
- 5分くらいは見て

内部実装どうなってるのかは知らないが、挙動としてはそんな感じ。

## プロセスを除外対象に含める
- `C:\Program Files\Windows Defender\MsMpEng.exe`
- `C:\ProgramData\Microsoft\Windows Defender\platform\x.xx.xxxx.xxx\MsMpEng.exe`
    - こっちもありえる

windows defender から除外してやることである程度軽くなる。完全無効化は不可能。
