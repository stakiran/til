# バッチファイル コマンドプロンプト

## バッチ xxx.bat を叩くと title に - xxx が append されていく問題
原因不明だが call をかます。

起きたとき

- convert.bat
    - 内部で drawio を呼び出している
- drawio
    - alancher でエイリアス作成されたもので、PATH 通った drawio.bat
- drawio.bat
    - draw.io.exe 呼び出してる

こうしたらなくなった

- convert.bat
    - 内部で drawio を~~呼び出している~~ callで呼び出す
        - :x: `set cmdline_header=drawio --export --format %ext%`
        - :o: `set cmdline_header=call drawio --export --format %ext%`

## カレントディレクトリ内の指定拡張子のファイルをループで処理

```bat
setlocal
set outpath=images
set ext=png
set cmdline_header=call drawio --export --format %ext%

for %%f in (*.drawio) do (
	echo Converting %%f...
	%cmdline_header% --output %outpath%\%%f.%ext% %%f
)
```

