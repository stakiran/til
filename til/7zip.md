# 7-zip

## CRC SHA サブメニューを消す
7zip-FM > オプション > 7-zip > CRC SHA チェック外す

## 7-zip 圧縮 コマンドライン

```bat
@echo off
setlocal

pushd "%~dp0"

set bin="C:\Program Files\7-Zip\7z.exe"
set vsld=(バックアップ先フォルダ)
%bin% a data.zip "D:\data"
%bin% a firefox.zip "%appdata%\Mozilla\Firefox"

echo 手動でバックアップ先にコピーすること.
explorer "%vsld%"
```
