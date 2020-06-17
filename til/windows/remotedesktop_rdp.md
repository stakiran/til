# リモートデスクトップ

## RDP でログイン後に一部ウィンドウの表示が大きくなる
ログイン先の pc で、

- HKEY_CURRENT_USER\Control Panel\Desktop
- Win8DpiScaling を 1 にする
- 要再起動

参考: [リモートデスクトップ接続するとフォントがにじむ、ぼやける、一部のフォントが大きく表示される](https://www.ipentec.com/document/windows-different-font-size-on-remote-desktop-connection)

## RDP ウィンドウ内に表示を収めたい（スクロールバーやめたい）
システムメニュー > スマートサイズ指定
