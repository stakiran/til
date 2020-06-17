# WinSAT.exe Windows エクスペリエンスインデックス
\Microsoft\Windows\Maintenance\WinSAT

性能測定して microsoft に報告する系。

- 2020/02/23 07:06:03 homeで動いてたので無効にした。上記データストアにはなにもないが
- 2020/04/16 19:33:24 mp300 つないだあと動くのこれっぽいが。無効にしてるんだけどなー。

## winsat formal コマンド実行して計測
[【Tips】Windows 10でエクスペリエンスインデックスを確認する方法 | ソフトアンテナブログ](https://www.softantenna.com/wp/tips/windows-10-experience-index/)

```
$ winsat formal

$ powershell -Command "Get-CimInstance Win32_Winsat"
CPUScore              : 7.5
D3DScore              : 9.9
DiskScore             : 5.9
GraphicsScore         : 5.4
MemoryScore           : 7.8
TimeTaken             : MostRecentAssessment
WinSATAssessmentState : 1
WinSPRLevel           : 5.4
PSComputerName        :
```

[Windows10でパソコンの性能測定（エクスペリエンスインデックス）をする方法 | HYZ STUDIO BLOG（ハイズスタジオブログ）](https://hyzstudioblog.com/topic/5013/)

> 1.0から9.9まで(Windows 8以降)

## 計測結果
C:\windows\Performance\WinSAT\DataStore
