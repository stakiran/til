# draw.io
- [web](https://www.draw.io/)
- [desktop app](https://github.com/jgraph/drawio-desktop/releases)
    - draw.io-XX.XX.XX.exe

## コマンドラインで画像出力
convert.bat

同フォルダ内の xxx.drawio から images/xxx.png に変換する例。

- --export でエクスポートしますの旨
- --format でフォーマット指定。pdf, jpg, png, svg
- --output で出力先名前

```
@echo off

rem - Must be 'drawio' to the PATH as a draw.io.exe
rem - outpath must be generated beforeward.

setlocal
set outpath=images
set ext=png
set cmdline_header=drawio --export --format %ext%

for %%f in (*.drawio) do (
	echo Converting %%f...
	%cmdline_header% --output %outpath%\%%f.%ext% %%f
)
```

## コマンドライン
```
$ draw.io.exe --help
```

## グリッドを変える
右サイドバーの Diagram > Grid

## フリーハンド
配置 > 挿入 > freehand

## デスクトップ版バイナリ
`C:\Program Files\draw.io\draw.io.exe`

