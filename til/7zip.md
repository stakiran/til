# 7-zip

## 圧縮時に指定フォルダを除外する

### 例2: git ローカルリポジトリ

```
%bin% a gitlab_team1.zip "D:\work\gitlab\team1" -xr!*node_modules* -xr!*.git*
```

.git と node_modules を省いている。

### 例1: Google Chrome

```
%bin% a chrome_default.zip "%localappdata%\Google\Chrome\User Data\Default" -xr!*Worker* -xr!*Cache* -xr!*IndexedDB*
```

特に大きな以下を省いている。

- Service Worker
- Cache
- Code Cache
- IndexedDB

**必ず両端をワイルドカードにする必要がある**。`-xr!*IndexedDB` や `-xr!IndexedDB` だと効果がなかった。

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
