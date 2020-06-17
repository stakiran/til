# レジストリエディタ

## Uninstall キー配下にアプリ情報が見当たらない
64bit 環境に 32bit 環境を入れた場合は **HKEY_LOCAL_MACHINE\Software\WOW6432Node** こっちに書き込まれる。

参考:

- [64bit環境で32bit版ソフトの情報がレジストリに書き込まれない!? - 新・かみひろぐ](https://kamihiro.net/regedit-64/)
- [第6回　レジストリのリダイレクトと仮想化およびレジストリ操作ツール：Windows OS入門 - ＠IT](https://www.atmarkit.co.jp/ait/articles/1502/19/news120.html)
    - > 32bitアプリケーションが「HKLM\SOFTWARE」へアクセスすると、実際には「HKLM\SOFTWARE\Wow6432Node」にアクセスするようにWOW64によって自動的にリダイレクトされる
    - **64ビットアプリからアクセスすると普通通り**
    - 32ビットアプリからアクセスするとリダイレクト
    - **regコマンドは32ビットアプリ**

どのキーがリダイレクトされるかは以下を。

- [WOW64 の影響を受けるレジストリ キー (Windows)](https://msdn.microsoft.com/ja-jp/windows/aa384253(v=vs.80))
    - でも uninstall は記載がないが……

## お気に入り よく使うキー
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit\Favorites

```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit\Favorites]
"User Shell Folders"="コンピューター\\HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders"
"TabProcGrowth"="コンピューター\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main"
"ShellIconOverlayIdentifiers"="コンピューター\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellIconOverlayIdentifiers"
"DirectoryBackgroundShell"="コンピューター\\HKEY_CLASSES_ROOT\\Directory\\Background\\shell"
"Folder"="コンピューター\\HKEY_CLASSES_ROOT\\Folder"
"Directory"="コンピューター\\HKEY_CLASSES_ROOT\\Directory"
"Drive"="コンピューター\\HKEY_CLASSES_ROOT\\Drive"
"CLSID"="コンピューター\\HKEY_CLASSES_ROOT\\CLSID"
"AllFilesystemObjects"="コンピューター\\HKEY_CLASSES_ROOT\\AllFilesystemObjects"
"Shell Extensions"="コンピューター\\HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Shell Extensions"
"Command Processor(AutoRun)"="コンピューター\\HKEY_CURRENT_USER\\Software\\Microsoft\\Command Processor"
"Favorites(regedit.exe)"="コンピューター\\HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Applets\\Regedit\\Favorites"
"py_auto_file"="コンピューター\\HKEY_CLASSES_ROOT\\py_auto_file"
"command(pyhon.exe)"="コンピューター\\HKEY_CLASSES_ROOT\\Applications\\python.exe\\shell\\open\\command"
"Applets>Paint"="コンピューター\\HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Applets\\Paint"
"run(localmachine)"="コンピューター\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
"Uninstall(localmachine)"="コンピューター\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall"
"Uninstall(user)"="コンピューター\\HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall"
```
