# 勝手に英語キーボードになるとか言語バーどうやって出すんだっけとか on win10
たまに Google 日本語入力が動かなくなってデフォの MS-IME に戻されたり、勝手に英語キーボードになったりして非常にうっとうしい。

## 言語バーを出す
まずは「テキストサービスと入力言語」を出す。

```
; これは拙作 alauncher の設定
; 「lang」コマンドで起動できるようにしている
[lang]
rawbin=Rundll32 Shell32.dll,Control_RunDLL input.dll,,{C07337D3-DB2C-4D0B-9A93-B722A6C106E2}
alias=langbar
```

その上で、

- 言語バータブ
- 言語バー > デスクトップ上でフロート表示するを選ぶ
- 言語バーのテキストラベルを表示するをオン
    - これしないと「IMEを選ぶ部分」が表示されない

## 勝手に英語キーボードになる
言語バー出して、EN を JP に切り替えれば OK

## 言語バーがなぜか出ない場合
- Google 日本語入力の設定を開く
- その他タブ > 規定の IME から ctrl + shift を有効にする
- ctrl + shift 押して google に戻す
- 有効にしたのを無効に戻す

```ini
; 以下は alauncher 時のメモ
[googleja]
rawbin=start "" "C:\Program Files (x86)\Google\Google Japanese Input\GoogleIMEJaTool.exe" --mode=config_dialog
```
