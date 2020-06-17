# Golang Go言語
- [Go 言語に関するブックマーク - Qiita](https://qiita.com/spiegel-im-spiegel/items/98d49ac456485b007a15)
- [他言語プログラマがgolangの基本を押さえる為のまとめ - Qiita](https://qiita.com/tfrcm/items/e2a3d7ce7ab8868e37f7)
- [golang チートシート - Qiita](https://qiita.com/jca02266/items/56a4fb7b07b692a6bf34)
- [逆引きGolang](https://ashitani.jp/golangtips/index.html)
- [Goプログラミング言語仕様 - golang.jp](http://golang.jp/go_spec) 古いが
- [avelino/awesome-go: A curated list of awesome Go frameworks, libraries and software](https://github.com/avelino/awesome-go#command-line)
- [Big Sky :: Golang で物理ファイルの操作に path/filepath でなく path を使うと爆発します。](https://mattn.kaoriya.net/software/lang/go/20171024130616.htm)
- [Go言語の初心者が見ると幸せになれる場所　#golang - Qiita](https://qiita.com/tenntenn/items/0e33a4959250d1a55045)
- [a-know/a-know: CLI tool about me (a-know)](https://github.com/a-know/a-know)
  - github release 方法とか実践的tipsが端的に

# 2019/09/27

## ファイル名無効判定 for windows

```
func sectionname2filename(sectionName string) string {
	invalidChars := []string{"\\", "/", ":", "*", "?", "\"", "<", ">", "|"}
	AfterChar := "-"
	ReplaceCountIsUnlimited := -1
	Extension := ".md"

	ret := ""

	ret = strings.TrimSpace(sectionName)

  // ★ここメイン
	// replace invalid chars on windows filename
	for _, invalidChar := range invalidChars {
		ret = strings.Replace(ret, invalidChar, AfterChar, ReplaceCountIsUnlimited)
	}

  // ★おまけで replace の他の使い方も
	// replace spaces for easy to handling as a filename
	ret = strings.Replace(ret, " ", AfterChar, ReplaceCountIsUnlimited)
	ret = strings.Replace(ret, "\t", AfterChar, ReplaceCountIsUnlimited)
	// replace () because the conflict on markdown grammer
	ret = strings.Replace(ret, "(", AfterChar, ReplaceCountIsUnlimited)
	ret = strings.Replace(ret, ")", AfterChar, ReplaceCountIsUnlimited)
	// add the extension
	ret = ret + Extension

	return ret
}
```

## interface

### 今日学んだもの
慣れるまでに時間かかりそー…… at 2019/09/27 09:56:45

```
type FileInfo struct {
	LineCount int
}

// ★ 1. 型名とメソッドのテンプレを定義する
type RefreshCallbackee interface{
	onRefresh(string, FileInfo)
}

type LinesSaver struct {
  ...
	onRefreshCallbackees   []RefreshCallbackee //★ 2. 使う側 インタフェースの型で扱う
}

func (saver *LinesSaver) Refresh(newFilename string) {
  ...
	for _, obj := range saver.onRefreshCallbackees {
		obj.onRefresh(filename, fileinfo)  //★ 2.
	}
}

type IndexSaver struct {
  ...
}

// ★ 3. 普通にインタフェースが持つメソッドを実装しておく
//      (この定義部分でインタフェースを extend するとかそういう構文は無い)
func (saver *IndexSaver) onRefresh(filename string, fileinfo FileInfo){
	saver.addFileInformation(filename, fileinfo)
}

func main() {
	linesSaver := NewLinesSaver()
	// ★4. 使う時
	// - a) まず「インタフェースを実装したインスタンス」を普通につくる
	// - b)「インタフェースの型を受け付けるヤツ」に渡す時は
	//     「a) のポインタ」を使って「インタフェースの型」として定義したものを使う
	indexSaver := NewIndexSaver("_index.md")
	var refreshCallbackeeIndexSaver RefreshCallbackee = &indexSaver
	linesSaver.AddCallbackOnRefresh(refreshCallbackeeIndexSaver)
  ...
```

### 6月のゴミ
- [他言語プログラマがgolangの基本を押さえる為のまとめ - Qiita](https://qiita.com/tfrcm/items/e2a3d7ce7ab8868e37f7#%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89)
- [Go の interface 設計 - Block Rockin’ Codes](http://jxck.hatenablog.com/entry/20130325/1364251563)
- [Golang: 構造体がインタフェースを実装しているかコンパイル時にチェックする - tetsuok の旅 blog](https://tetsuok.hatenablog.com/entry/2013/03/01/114957)


```
// 1 定義する
// ----------
type Printable interface {
	GetPrintable() string
}

// 2 実装する
// ----------

// ここでは Task struct に実装
func (task *Task) GetPrintable() string{
	ret := fmt.Sprintf("Task[%s]: is_done=%t", task.name, task.IsDone)
	return ret
}

// 3 使う
// ------
t1 := Printable(Task{})
fmt.Printf("%s\n", t1.GetPrintable())
```

ただし t1 は interface で定義されたメソッド(ここでは GetPrintable() )しか見えない。
(元々 Task struct の公開レシーバとして存在するメソッドたちには t1 からはアクセスできなくなる)

……わかったような、わからんような。

# 2019/09/26

## invalid method expression T.N (needs pointer receiver: (*T).N)
T に N というメソッドはないですよ、というエラー。

今回ハマったのは
  x LinesSaver.AddCallbackOnRefresh(...
  o linesSaver.AddCallbackOnRefresh(...
インスタンスではなく型名を指定しちゃってた

[Methods in Go (part II) - golangspec - Medium](https://medium.com/golangspec/methods-in-go-part-ii-2b4cc42c5cb6)

## golang の変数は必ず初期化される
[ゼロ値を使おう #golang - Qiita](https://qiita.com/tenntenn/items/c55095585af64ca28ab5)

string は ""
int系、rune系 は 0
bool 系は false
error は nil

## const のコーディング規約
[eption because it was borrowed directly from POSIX.](https://stackoverflow.com/questions/22688906/go-naming-conventions-for-const)

例外名やエラー定数名は SNAME_CASE
あとは CamelCase が一般的みたい

# 2019/08/01

## go get でアップデートしたい
go get -u github.com/stakiran/alauncher

# 2019/07/22
winapi ゲー

## 自力で書く
とりあえず getwindowtext

```
package main

import (
	"fmt"
	"syscall"
	"unsafe"
)

func main() {
	user32, err := syscall.LoadDLL("user32.dll")
	if err != nil {
		panic(err)
	}
	defer user32.Release()

	procGetForegroundWindow, err := user32.FindProc("GetForegroundWindow")
	if err != nil {
		panic(err)
	}
	hwnd, _, _ := procGetForegroundWindow.Call()

	procGetWindowTextLength, err := user32.FindProc("GetWindowTextLengthW")
	if err != nil {
		panic(err)
	}
	textLength, _, _ := procGetWindowTextLength.Call(hwnd)
	textLength = textLength + 1

	procGetWindowText, err := user32.FindProc("GetWindowTextW")
	if err != nil {
		panic(err)
	}
	// LPTSTR が *uint16
	buf := make([]uint16, textLength)
	procGetWindowText.Call(hwnd, uintptr(unsafe.Pointer(&buf[0])), textLength)

	text := syscall.UTF16ToString(buf)
	fmt.Println(text)
}

```

参考:

- [goでWindows APIを実行する覚書 - Qiita](https://qiita.com/sky_jokerxx/items/3e0254de4994fc75ac3f)
- [windows - GoDoc](https://godoc.org/golang.org/x/sys/windows)
- 参考にできそうなソース: github.com/AllenDang/w32/
  - [GetWindowTextLengthW](https://github.com/AllenDang/w32/blob/master/user32.go)
  - [w32/typedef.go](https://github.com/TheTitanrain/w32/blob/master/typedef.go)

## win32api github.com/AllenDang/w32
cannot use flag (type uint32) as type uintptr in argument to procRedrawWindow.Call

https://github.com/AllenDang/w32/issues/83
https://github.com/AllenDang/w32/issues/80

comp win7 で発生。面倒くさいな。flag 書いてるところが uintptr(flag) にすればいいとか。
別の fork を使えばいいらしいが、うーん。安定してないの嫌いよ。

# 2019/07/12

## err の型は error
参考: https://qiita.com/nayuneko/items/3c0b3c0de9e8b27c9548

interface になってるらしい。

```
type error interface {
    Error() string
}
```

# 2019/07/10

## 無限ループは for{} だけ

# 2019/07/09

## 関連付けでコマンドライン実行
windows は start でラップするのか、なるほど賢い。

```
if doEditIni {
	err := exec.Command("cmd", "/c", "start", "", filepathAlaIni).Start()
	if err != nil {
		fmt.Printf("Fail to read file '%v'", err)
	}
	success()
}
```

参考: https://github.com/skratchdot/open-golang/blob/master/open/exec_windows.go

# 2019/07/08

## 空文字比較
s == "" でも len(s) == 0 でも良い。

https://twitter.com/kaoriya/status/482871589076099072 公式も混在して使ってるみたい。

# 2019/07/01

## getenv 環境変数取得
https://golang.org/pkg/os/#Getenv

os.Getenv("HOME")
見つからない場合は empty string。
空値なのか未定義なのかの区別はわからんので LookupEnv を使う。

```
	dirHome := os.Getenv("HOME")
	if dirHome == ""{
		dirHome = os.Getenv("USERPROFILE")
		if dirHome == ""{
			abort("Fail to search home directory.")
		}
	}
	fmt.Printf("dirHome is '%s'\n", dirHome)
```

## ini
https://ini.unknwon.io/docs/intro/getting_started

go get "github.com/go-ini/ini"

section オブジェクトなどオブジェクトで頑張る系。
基本上記 doc で事足りるが、section.Name() など一部載ってないので
  https://github.com/go-ini/ini/blob/master/section.go
ソースも見て。読みやすいから。

```
	ini, err := ini.Load("alias.ini")
	if err != nil {
		fmt.Printf("Fail to read file '%v'", err)
		os.Exit(1)
	}

	sections := ini.Sections()
	for _, section := range sections {
		sectionName := section.Name()
		rawbin := section.Key("rawbin")
		bin := section.Key("bin")
		dir := section.Key("dir")
		prm := section.Key("prm")
		alias := section.Key("alias")
		disable := section.Key("disable")
		fmt.Printf("[%s]\n", sectionName)
		fmt.Printf("rawbin : %s\n", rawbin)
		fmt.Printf("bin    : %s\n", bin)
		fmt.Printf("dir    : %s\n", dir)
		fmt.Printf("prm    : %s\n", prm)
		fmt.Printf("alias  : %s\n", alias)
		fmt.Printf("disable: %s\n", disable)
	}
```

# 2019/06/27

## go get と go clean -i
go clean -i github.com/stakiran/intoc で bin 配下は消せる。
src配下は消えないので自分で消す。

 -i バイナリを消す(go install と対応してるみたい)
 -n 削除コマンド表示するだけ

https://golang.org/pkg/cmd/go/internal/clean/

$ go clean -n github.com/stakiran/intoc
cd C:\bin1\gopath\src\github.com\stakiran\intoc
rm -f intoc intoc.exe intoc.test intoc.test.exe intoc intoc.exe intoc_test intoc_test.exe
↑
でも go clean しても src 配下消えてくれないんだけど。

# 2019/06/19

## crlf のファイルには crlf で write したい
python の時は維持されていたが golang だと lf 固定になる。

[os: output CR LF for \n on Windows · Issue #28822 · golang/go](https://github.com/golang/go/issues/28822)

議論されてる。mattn さんは「移植性の観点から lf で統一したい」「win10 notepad も lf 対応したし」って感じ。

で、結局

> We aren't going to do this, so closing.

しないだと。ひー。

# 2019/06/18

## クロスプラットフォームビルド
[Installing Go from source - The Go Programming Language](https://golang.org/doc/install/source#environment)

GOOS と GOARCH 環境変数をセットした上で build する。

よーわからん。とりあえず windows 386 でいいか。
ビルドしたら zip にしてマニュアルで release にアップするか、ghr https://github.com/tcnksm/ghr 使って自動化。

# 2019/06/17

## ビルド
makefile が恒例。

[Go言語開発を便利にするMakefileの書き方 - Qiita](https://qiita.com/yoskeoka/items/317a3afab370155b3ae8)

だが windows では make 無いよね。

[golang でのクロスコンパイルの留意事項 — KaoriYa](https://www.kaoriya.net/blog/2015/03/06/)

と思ったら golang に make.bat が付属してる。
C:\bin1\Go\src\make.bat

[golangで色々なOSのバイナリを作る - write ahead log](https://twinbird-htn.hatenablog.com/entry/2016/04/17/231039)

> GOOS=windows GOARCH=386 go build

goarch は 386 と amd64

とりあえず make.bat 見つけたけど、

make.bat

```
@echo off
%GOROOT%\src\make.bat %*
```

```
$ make
指定されたパスが見つかりません。
ERROR: Cannot find C:\Users\1134140363071\Go1.4\bin\go.exe
"Set GOROOT_BOOTSTRAP to a working Go tree >= Go 1.4."
```

こうなる。make.bat はただでは使えないみたいねー……？
というより %userprofile% 直下へのインストールを前提としている感じ

……素直に test.bat とかつくるか

## 構造体のcloneができぬ
元は argparse が一度しか呼べない(もっというと flag)から、一回だけ読んでデフォルト値の塊にして、あとはそこから clone してテストで使うことを考えてる……

clone はここやってるけど
https://qiita.com/ymgyt/items/892c357971c7dd7bb675
どうも上手くいかん
→だよなぁ。ポインタの指す先をコピーしてるだけだもん

たぶん
https://github.com/jinzhu/copier
これとか使わないとダメだと思う。

## 復数行文字列の定義 multiline string
multiline = `#intoc
intoc is the...

but its`

ただし backtick はエスケープできないので、backtick 含めたいなら  + "`" 的に普通の文字列として連結する。

## string join と split
strings.Join(tocLines, "\n")

strings.Split(aString, "\n")

## python の list extends を golang array で
append に ... 付けて与える。

```
package main

import (
	"fmt"
)

func main() {
	a := []string{"a","b","c"}
	b := []string{"1","2","3"}
	a = append(a, b...)
	for _,elm := range a{
		fmt.Println(elm)	
	}
}
```

https://stackoverflow.com/questions/16248241/concatenate-two-slices-in-go

# 2019/06/13
ガシガシ進める。文字列系ノウハウまとめとく。

## godoc 使ってみる

```
/*
  パッケージの説明はここに
/*
package main
...

// aaa is ....
// 空行を空けずにコメントを書いていく。
// 最初は定義名と同じで始める。
// 英語で、端的に文章を述べる感じ。
func aaa(){

}
```

intoc.go だけ表示したい場合どうすればええ？
go doc でも godoc -http 3000 でもダメなんだが。

sarama の見てみる
- https://github.com/Shopify/sarama/blob/master/broker.go
- https://godoc.org/github.com/Shopify/sarama#NewBroker

cron
- https://godoc.org/github.com/robfig/cron#Cron
- https://github.com/robfig/cron/blob/master/cron.go

## utf8 string で先頭1文字をslice
peekfirst = string([]rune(strings.TrimSpace(line))[:1])

これは trim しているが、肝は rune すること。

## string replace
ret = strings.Replace(ret, " ", "-", -1)

第四引数は置換回数。0 未満なら無限回。

## lowercase tolower
ret = strings.ToLower(ret)

## startswith, endwith 
import "strings"

startsWith := strings.HasPrefix("prefix", "pre") // true
endsWith := strings.HasSuffix("suffix", "fix") // true

## cannot take the address of が出る
&NewDeplicator()

↑ こんな感じで直接ポインタを得ることはできない。
いったん変数に代入すること。

## strip 
strings.TrimSpace()

## "a"*32 ← こういう繰り返し
strings.Repeat("a", 32)

# 2019/06/12
上々。やはり目標があった方が早い at 2019/06/12 15:58:01

~~正規表現~~
~~文字列整形~~
~~unittest でガシガシやりたい、もう intoc 作り始める~~
~~1ファイルで済ませたい~~
~~自身のパス取得~~
~~パス操作全般~~

## unittest 2ファイルのシンプル構成
intoc.go と intoc_test.go があるとする。

intoc.go:

```
packeage main

...

func main(){
  ...
}
```

intoc_test.go:

```
package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestDuplicator(t *testing.T) {
	dup := NewDuplicator() // ★ intoc.go 側の関数やクラスを呼び出す

	assert.Equal(t, dup.Add("key1"), 0)
	assert.Equal(t, dup.Add("key1"), 1)
	assert.Equal(t, dup.Add("key1"), 2)
	assert.Equal(t, dup.Add("key22"), 0)
	assert.Equal(t, dup.Add("3key3"), 0)
	assert.Equal(t, dup.Add("3key3"), 1)
	assert.Equal(t, dup.Add("key22 "), 0)
}
```

実行:

```
$ go test intoc_test.go intoc.go
ok      command-line-arguments  0.144s
```

## utf8 string を slice する
Golang は string が byte 列なので、そのまま slice すると「1-文字 1-index」にならない。
Python3 の string みたいに「1-文字 1-index」で頑張りたい場合は、[]rune 型にキャストしてから行う。
で、最後に string にキャストし直す。


```
func line2sectioninfo(line string) (int, string){
	sectionlevel := 0
	body := ""
	runeLine := []rune(line) // ★計算用に使う rune

	for {
		cnt := sectionlevel + 1
		comparer := strings.Repeat("#", cnt)
		runeComparer := []rune(comparer)

		if string(runeLine[:cnt]) == string(runeComparer){ // ★比較する時も string に戻す
			sectionlevel += 1
			body = string(runeLine[sectionlevel:]) // ★使う時は string に戻す
			continue
		}
		break
	}

	return sectionlevel, body
}
```

ちなみに == 比較のところを string にキャストしてないとこうなる。
rune 型は == による文字列比較をサポートしてないのかな？

> invalid operation: runeLine[:cnt] == runeComparer (slice can only be compared to nil)

→ 違う。**slice は(あとmapも) nil としか比較できないようになってる。初期化されてない or なんか入ってるの二択** from [golangのequalityの評価について - podhmo's diary](https://pod.hatenablog.com/entry/2016/07/30/204357)

## map
- [【Go言語】assignment to entry in nil map - DRYな備忘録](http://otiai10.hatenablog.com/entry/2014/08/09/154256)
- [【go】golangはmapは宣言だけだと `panic: assignment to entry in nil map` に...なることがあるよのメモ - tweeeetyのぶろぐ的めも](https://tweeeety.hateblo.jp/entry/2017/04/11/005321)

```
type Duplicator struct{
	dict map[string]int //★string key, int value な map
}

func NewDuplicator() Duplicator {
	dup := Duplicator{}
	dup.dict = map[string]int{} // ★mapはGolangが初期化してくれないので明示的初期化必要
	return dup
}

func (dup *Duplicator) Add(key string) int {
	_, isExist := dup.dict[key] // ★存在確認はこう
	if !isExist {
		dup.dict[key] = 1 // ★代入すれば新しくつくれる
		count_before_adding := 0
		return count_before_adding
	}
	count_before_adding := dup.dict[key] // ★既存キーにアクセス
	dup.dict[key] += 1 // ★既存キーの値を更新
	return count_before_adding
}
```

## map parse
range で k と v を取り出せるので楽

```
	for k, v := range deployer.mymap{
		query := fmt.Sprintf("%%%s%%", k)
		afterstr = strings.Replace(afterstr, query, v, -1)
	}
```


## "" と `` の違い
\n などのエスケープ要否。

`...` だと要らない。`...` の中で改行したらそれはそのまま反映される。

[go - What is the difference between backticks (``) & double quotes ("") in golang? - Stack Overflow](https://stackoverflow.com/questions/46917331/what-is-the-difference-between-backticks-double-quotes-in-golang?rq=1)

# 2019/06/11

## 文字列 format
Sprintf を使う。

```
s := fmt.Sprintf("%s-%d", ret, dupCount)
```

## fmt format 書式指定子
[忘れがちなGo言語の書式指定子を例付きでまとめた - Qiita](https://qiita.com/Sekky0905/items/c9cbda2498a685517ad0#t-%E5%8D%98%E8%AA%9Etrue%E3%81%BE%E3%81%9F%E3%81%AFfalse)

bool    %t
string  %s
int 10  %d

# 2019/06/10

## class
[Go 言語の値レシーバとポインタレシーバ | Step by Step](https://skatsuta.github.io/2015/12/29/value-receiver-pointer-receiver/)

- 値レシーバだとコピー遅い＆中で書き換えても呼び出し元には影響されない

## package できたので改めて
- go run class_main.go だけでいい（sampleclass ディレクトリ等は指定しなくていい）
  - build もこれで成功した

```
-root
  -class_main.go
  +sampleclass
    -class.go
```

class_main.go

```
package main

import "./sampleclass" ★ディレクトリ名を指定する

func main() {
	t1 := class.Task{Name: "バックアップ"}  ★パッケージ名を指定する
	t2 := class.Task{Name: "掃除"}
	t1.Print()
	t2.Print()
	t1.Name = "バックアップ @1"
	t1.Print()
}
```

class.go

```
package class  ★import元から参照する名前

import (
	"fmt"
)

type Task struct{
	Name string
	date string
	starttime string
	endtrime string
	is_done bool
}
func (task Task) Print(){
	fmt.Printf("Name=%s\n", task.Name)
}
```


## (試行) class と package
公開性見たいので package にしてみたがアクセスできない

- root
  - class_main.go
  - class.go

class.go にアクセスできない。

https://qiita.com/qt-luigi/items/e1ccc82e4000a850ab1b

ディレクトリ化しないとダメ？

https://blog.eksy.tokyo/post/import-self-made-packages-in-golang/

> 各リポジトリには1つ以上のパッケージが含まれています。

ルートから一段掘らないとダメ？

[golangでC言語のincludeみたいにカレントディレクトリのファイルを読み込めないのか？ - my coredump](http://mycoredump.hatenablog.com/entry/2014/07/29/231846)

謎解けた

- ビルド時に **ビルド対象ファイルは全部指定する**
- include したい場合は「サブディレクトリ作ってパッケージ化する」か「同じパッケージ名（たとえば main）を指定して別ファイルにする」か

[Goのパッケージパスとパッケージ名は異なってもよいか？ - Qiita](https://qiita.com/qt-luigi/items/e1ccc82e4000a850ab1b)

import ではパスの方を見るので .go ファイル側の package XXXX この部分はなんでもいいらしい？

```
$ go run class_main.go sampleclass\class.go
named files must all be in one directory; have ./ and sampleclass\
```

## 引数解析 flag で intoc.py 真似た

- flag.Xxxx がポインタを返す → Parse() の後に各ポインタに値が入る仕様なので、ポインタを使わないと保持できない
- Required はサポートしてないので自力で
- ググればサクサク見つかります
  - https://golang.org/pkg/flag/ なんだかんだ公式リファレンス優秀

```
type Args struct {
	debugPrintAll *bool

	input        *string
	parseDepth   *int
	indentDepth  *int
	useAsterisk  *bool
	usePlainEnum *bool
	noLinkformat *bool

	useEdit      *bool
	editTarget   *string
}

func argparse() Args {
	args := Args{}

	args.input = flag.String("input", "", "A input filename.")

	args.parseDepth = flag.Int("parse-depth", -1, "The depth of the TOC list nesting. If minus then no limit depth.")
	args.indentDepth = flag.Int("indent-depth", 2, "The number of spaces per a nest in TOC.")

	args.useAsterisk = flag.Bool("use-asterisk", false, "Use an asterisk `*` as a list grammer.")
	args.usePlainEnum = flag.Bool("use-plain-enum", false, "Not use Markdown grammer, but use simple plain section name listing.")
	args.noLinkformat = flag.Bool("no-linkformat", false, "Not use `- [text](#anochor)`, but use `- text`.")

	args.useEdit = flag.Bool("edit", false, "If given then insert TOC to the file from `-input`.")
	args.editTarget = flag.String("edit-target", "<!-- TOC", "A insertion destination label when `-edit` given. NOT CASE-SENSITIVE.")

	args.debugPrintAll = flag.Bool("debug-print-all", false, "[DEBUG] print all options with name and value.")

	flag.Parse()

	// Preprocess
	// ----------

	printOption := func(flg *flag.Flag) {
		fmt.Printf("\t%s=%s\n", flg.Name, flg.Value)
	}
	if *args.debugPrintAll {
		fmt.Println("[Options]")
		flag.VisitAll(printOption)
	}

	// Required
	// --------

	if *args.input == "" {
		fmt.Println("-input required.\n")
		flag.PrintDefaults()
		os.Exit(2)
	}

	return args
}

func main() {
	args := argparse()
	fmt.Println(*args.input)
}
```

## 引数解析
- [Goでflagを使ってコマンドライン引数を扱う - Qiita](https://qiita.com/Yaruki00/items/7edc04720a24e71abfa2)
- [flag - The Go Programming Language](https://golang.org/pkg/flag/)

```
package main

import (
    "flag"
    "fmt"
)

func main() {
    var (
        i = flag.Int("int", 0, "int flag")
        s = flag.String("str", "default", "string flag")
        b = flag.Bool("bool", false, "bool flag")
    )
    flag.Parse()
    fmt.Println(*i, *s, *b)
}
```

a := flag.Xxxx でオプション一つずつ指定する感じ。
で、*a を見れば指定有無がわかる。デフォ入れておけば未指定時にデフォ値入れられる。

[Go言語でコマンドラインオプションを扱う - Qiita](https://qiita.com/jagio/items/a44c11d79aba0b229fcf)

`-h` もサポートしてる。

……が、required とかないし、うーん。

https://github.com/akamensky/argparse

python argparse 向き。star 95 くらいだが。
でも numbers parsing もまだサポートしてないのか。ダメだ。

[Big Sky :: Re: Goでコマンドライン引数と環境変数の両方からflagを設定したい](https://mattn.kaoriya.net/software/lang/go/20170609110526.htm)

flag 推しですね。
とりあえずは flag でいいか。
required はゴリ押しで頑張る。

# 2019/06/07

## list2file

```
func list2file(filepath string, lines []string) {
	fp, err := os.Create(filepath)
	if err != nil {
		abort(err.Error())
	}
	defer fp.Close()

	writer := bufio.NewWriter(fp)
	for _, line := range lines {
		writer.WriteString(line + "\n")
	}
	writer.Flush()
}

```

改行入らないが \n 共通で良さげ
Flush() 忘れちゃダメ

あと trunc も忘れちゃダメ。
これしないと前の内容が一部残ってしまう at 2019/06/18 11:22:10 半日ハマった

→ [Golang ファイル入出力メモ - Qiita](https://qiita.com/matthewlujp/items/c95fe46097688adfb5b3) [[Go言語]Golangの上書き処理が少し慣れない[memo] | 鈍色スイッチ](https://donsyoku.com/programming/golang-overwrite.html) [golang trunc - Twitter検索](https://twitter.com/search?f=tweets&q=golang%20trunc&src=typd)

# 2019/06/06

## for
lines は []string だとして。

```
	for _,line := range lines {
		fmt.Println(line)
	}
```

i 使ってないので _ で伏せてる。ふせないと unused でエラーなので。

## X golint

```
$ go get -u golang.org/x/lint/golint
package golang.org/x/lint/golint: unrecognized import path "golang.org/x/lint/golint" (https fetch: Get https://golang.org/x/lint/golint?go-get=1: proxyconnect tcp: EOF)
```

なんかネットワークの問題っぽいが。
https://github.com/golang/lint/issues/288
手動で gopath に git clone しろとか書いてる。えー。

C:\bin1\gopath\src\github.com\golang\lint
入ってんだがなー。。。

[go getが失敗する場合の対処(unrecognized import path) - Wakotech Blog](http://yutaszk23.hatenadiary.jp/entry/2015/04/26/145106)
goroot おかしいから？でも

  GOPATH=C:\bin1\gopath
  GOROOT=C:\bin1\Go\

設定してんだけどなぁ。よくわからん

## 命名大文字小文字
public は CamelCase
private は camelCase
ctor は NewXxxx
i/f は Xxxxer

https://golang.org/doc/effective_go.html#mixed-caps も読む。

> Finally, the convention in Go is to use MixedCaps or mixedCaps rather than underscores to write multiword names. 

snake_case よりも camelCase CamelCase みたいね。

## ファイル入出力

### file2list

```
func file2list(filepath string) []string {
	fp, err := os.Open(filepath)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer fp.Close()

	lines := []string{}

	scanner := bufio.NewScanner(fp)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}

	return lines
}

func print_lines(lines []string) {
	for _,line := range lines {
		fmt.Println(line)
	}
}

func main() {
	lines := file2list("intoc.py")
	print_lines(lines)
}
```

## list を実現するには？
slice で頑張る。
array は要素数不変。

[Go言語の基本 — array と slice の違い - Qiita](https://qiita.com/YumaInaura/items/aec7857518102ff5e27c)

```
s := []int{}
s = append(s, 1)
s = append(s, 2, 3, 4)
```

cap内なら既存書き換え、cap超えると新たな配列が生成されるらしい。

# 2019/06/05

## 文法
[他言語プログラマがgolangの基本を押さえる為のまとめ - Qiita](https://qiita.com/tfrcm/items/e2a3d7ce7ab8868e37f7)

この辺読みながら都度慣れた方が良さそうか。
変数定義はややこしいので覚えてしまいたい。

:=    宣言と代入
var   変数
const 定数

宣言は x int のように名前、型の順

## ユニットテスト
go test ./

- 詳細みたいなら -v オプション
- xxxx_test.go 内の TestXXXX 関数が実行される。

```
package main

import (
	"testing"
)

func TestAdd(t *testing.T) {
	actual := 10
	expected := 2 + 8
	if actual != expected {
		t.Errorf("actual %v\nwant %v", actual, expected)
	}
}

func TestSub(t *testing.T) {
	actual := -5
	expected := 2 - 8
	t.Skip("skip sub test.")
	if actual != expected {
		t.Errorf("actual %v\nwant %v", actual, expected)
	}
}
```

[Golangでtestingことはじめ（1）〜testingパッケージを使ったユニットテスト〜 - DeNA Testing Blog](https://swet.dena.com/entry/2018/01/16/211035)

- testing パッケージにはアサーション関数がない

https://github.com/stretchr/testify

testify 使ってみる？

- go get github.com/stretchr/testify
- "github.com/stretchr/testify/assert" を import
- `assert.Equal(t, actual, expected, "2+8=10?")`

簡単！

# 2019/06/04

## コード規約
[Go 言語のコーディングスタイル（コーディング規約） | まくまくHugo/Goノート](https://maku77.github.io/hugo/go/coding-style.html)
[#golang CodeReviewComments 日本語翻訳 - Qiita](https://qiita.com/knsh14/items/8b73b31822c109d4c497)
[Effective Go - The Go Programming Language](https://golang.org/doc/effective_go.html)

- タブ
- go fmt sample.go でフォーマッティング

## go run hello.go と go build hello.go
run はビルドして実行。一時ファイルは残さない。
build は exe をつくる。hello world でも 1.8MB くらいのファイル。

```
package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界")
}
```

## go env

```
set GOARCH=386
set GOBIN=
set GOCACHE=C:\Users\XXXXXXXXXXXX\AppData\Local\go-build
set GOEXE=.exe
set GOHOSTARCH=386
set GOHOSTOS=windows
set GOOS=windows
set GOPATH=C:\Users\XXXXXXXXXXXX\go
set GORACE=
set GOROOT=C:\bin1\Go
set GOTMPDIR=
set GOTOOLDIR=C:\bin1\Go\pkg\tool\windows_386
set GCCGO=gccgo
set GO386=sse2
set CC=gcc
set CXX=g++
set CGO_ENABLED=1
set CGO_CFLAGS=-g -O2
set CGO_CPPFLAGS=
set CGO_CXXFLAGS=-g -O2
set CGO_FFLAGS=-g -O2
set CGO_LDFLAGS=-g -O2
set PKG_CONFIG=pkg-config
set GOGCCFLAGS=-m32 -mthreads -fmessage-length=0
```

## go get
go get github.com/golang/tour/gotour

%gopath% 配下に get される
実行ファイルは %gopath%\bin に配置される

## gopath 変えます
goroot: C:\bin1\Go
→ 要らない。go.exe がたぶん認識できてると思う。

gopath: C:\bin1\gopath
→ やる。
   ユーザー環境変数でいい。

path に %goroot%\bin
→ やる。
   ユーザー環境変数でいい。
