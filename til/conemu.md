# ConEmu

## ConEmu のキーボードショートカット設定時の注意点
- **あらかじめ用意されてる操作に対して**、何らかのキーを割り当てる(operation first)という形
    - あるキーに対して、ある操作を割り当てる（key first）ではない

## modifier + cursor でタブ移動したい
デフォのアサインでは

- <kbd>ctrl</kbd> + <kbd>tab</kbd>
- <kbd>ctrl</kbd> を **押しっぱなし** にしたまま <kbd>cursor</kbd>
- 確定したら <kbd>ctrl</kbd> を離す

これでいける。Predefined として Systme, Ctrl+Left, Switch tab to left などで割り当てられてる。

## タブをコンパクトにする
- general > appearance
    - show buttons in tab bar オフ
    - show search field in tab bar オフ
    - 少しでもタブ広げるため
- general > size & pos
    - auto save window size ... on exit
- general > tab bar
    - tab templates > console は %s にする（titleのみ）
    - skip words... に「|管理者:」を追加

## ConEmu を指定ディレクトリをカレントディレクトリにして呼び出す

[ConEmu | ConEmu.exe Command Line Switches](http://conemu.github.io/en/ConEmuArgs.html)

上記リファレンスを見て頑張れば実現できるけれど、いちいち試すのもかったるいので、よく使うものを挙げてみた。

```
タブで新規
"C:\Program Files\conemu\ConEmu.exe" /Dir "c:\your_workspace" /Single

ウィンドウで新規
"C:\Program Files\conemu\ConEmu.exe" /Dir "c:\your_workspace" /NoSingle

タブ名を変える
"C:\Program Files\conemu\ConEmu.exe" /Dir "c:\your_workspace" /Single -cmd -new_console:t:"ConEmu Running Test"

新規した後に指定コマンドを実行(一つ)
"C:\Program Files\conemu\ConEmu.exe" /Dir "c:\your_workspace" /single -cmd cmd /k dir

新規した後に指定コマンドを実行(複数)
"C:\Program Files\conemu\ConEmu.exe" /Dir "c:\your_workspace" /single -cmd cmd /k "date /t & time /t & cd & prompt $G$G$G"
"C:\Program Files\ConEmu\ConEmu64.exe" -Dir "c:\your_workspace" -Single -cmd cmd /k "title workspace1 & cd"
```

### open conemu here

```
@echo off

set mydir=%~dp0
set conemu_path=C:\Program Files\conemu\ConEmu.exe
set start_command=prompt $$$S
rem new tab: /Single
rem new wnd: /NoSingle
set new_tab_or_new_window=/single

"%conemu_path%" /Dir "%mydir%" %new_tab_or_new_window% -cmd cmd /k %start_command%
```
