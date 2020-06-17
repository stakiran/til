# xcopy

## 事例1 webアプリ

```
@echo off
setlocal

set DIST_FOLDER_NAME=public

set thisdir=%~dp0
set COPYCMD=xcopy
set COPYOPT_FILE=/-Y
set COPYOPT_FOLDER=/-Y /S /E /I
set DIST_FOLDER_FULLPATH=%thisdir%%DIST_FOLDER_NAME%

if exist %DIST_FOLDER_FULLPATH% (
	rmdir /s /q %DIST_FOLDER_FULLPATH%
	if exist %DIST_FOLDER_FULLPATH% (
		echo 古い出力先 "%DIST_FOLDER_FULLPATH%" を削除できません.
		echo 他のプログラム等から開いている場合は閉じてください.
		pause
		exit /b
	)
)

mkdir "%DIST_FOLDER_FULLPATH%"
%COPYCMD% "%thisdir%index.html" "%DIST_FOLDER_FULLPATH%" %COPYOPT_FILE%
%COPYCMD% "%thisdir%help.html" "%DIST_FOLDER_FULLPATH%" %COPYOPT_FILE%
%COPYCMD% "%thisdir%*.js" "%DIST_FOLDER_FULLPATH%" %COPYOPT_FILE%
%COPYCMD% "%thisdir%*.css" "%DIST_FOLDER_FULLPATH%" %COPYOPT_FILE%
%COPYCMD% "%thisdir%lib" "%DIST_FOLDER_FULLPATH%\lib" %COPYOPT_FOLDER%
%COPYCMD% "%thisdir%data" "%DIST_FOLDER_FULLPATH%\data" %COPYOPT_FOLDER%
```

## 事例2 ポメラのやつ
指定ドライブ配下の全フォルダをコピー。

これで `g:\pomera` や `g:\pomera_memo` フォルダがコピーされて、`%dstdir%\pomera`, `%dstdir%\pomera_memo` という感じでコピーされる。

```
@echo off
setlocal

set pomera_root=g:\
set dstdir=%~dp0
set commitmsg= %date% %time:~0,8%

pushd %pomera_root%
if ERRORLEVEL 1 pause & exit /b
popd

xcopy %pomera_root% %dstdir% /I /F /E /Y

pushd %dstdir%
git add -A
git commit -m "%commitmsg%"
git push origin master
popd

pause
```
