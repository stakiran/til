# DPC_WATCHDOG_VIOLATION
at 2020/07/17 18:33:45

- zoom + Quiet Comfort 35 によるオンライン飲み会
- windows が死んで再起動になる
- 二回起きた
- 詳しく
    - zoom で突然オーディオが認識されなくなる
    - しばらくして画面が止まる(たぶんこれが 10s 経って起きる)
    - quiet comfort も強制的に接続が切れる

調べてる

- [DPC_WATCHDOG_VIOLATION prevention](https://dpc-watchdog-violation.dnki.co.jp/)
- [マイクロソフト クリップアート 復刻: Windows10でDPC_WATCHDOG_VIOLATIONを回避する方法](https://msclipart.blogspot.com/2015/12/pcwindows10update-dpcwatchdogviolation.html)
    - 10秒以内にデバイスから応答返ってこないと、このエラーを出す
    - win8+
- ~~ドライバーが古い~~ 違う。今までずっと win10 だが起きてない。久々に zoom 飲み会したら。

zoom 込みで調べてる

- ちらほら見つかる
    - [DPC_WATCHDOG_VIOLATION Error - while using Airpods on Zoom - Microsoft Community](https://answers.microsoft.com/en-us/windows/forum/all/dpcwatchdogviolation-error-while-using-airpods-on/b4675ec4-66a2-4f1e-ba2d-4757cd9700e0)
    - [BSOD when using Zoom with Bluetooth Headphones - Microsoft Community](https://answers.microsoft.com/en-us/windows/forum/all/bsod-when-using-zoom-with-bluetooth-headphones/153932b7-7903-4674-8195-b6e0d740e11b)
    - [Computer restart while using Zoom app with blue screen error showing DPC_WATCHDOG_VIOLATION.](https://www.windowsphoneinfo.com/threads/computer-restart-while-using-zoom-app-with-blue-screen-error-showing-dpc_watchdog_violation.336788/)
    - ……
    - いずれにせよ answer はなし
