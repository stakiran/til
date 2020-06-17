# Wireshark 
2017年、v1.10 の話なので古いかも

## フィルタの書き方
ip.src==192.168.137.128 && ip.dst==10.58.81.254 && cflow

not tcp && not icmp

ip.src!=10.58.80.236 && ip.src!=10.128.100.61 && ip.src==10.58.80.0/24

ip.src=10.58.80.0/24

## loopbackをキャプチャするには？
windows では winpcap の制約上無理。

rawcap を使えば可能。

- http://www.netresec.com/?page=RawCap
- 上記から rawcap.exe をダウンロードして cmd 上で実行

```
$ RawCap.exe -f 127.0.0.1 dumpfile.pcap
```

- dumpfile.pcap に記録されてく
- ctrl + c で終了
- wireshark で pcap ファイルを見ればいい

## 背景色について
背景のピンクや緑は view > coloring rules から設定可能 

## チェックサムが有効かどうか調べる
Edit > Preferences >Protocols > 目的のプロトコル(たとえばIPv4)

Validate the IPv4 checksum if possible にチェック。

確認する場合はチェックサム部分を見る。

```
Good: True  <-- これならOK
Bad: False
```

ダメな場合は incorrect で赤色表示になる。チェックサムが働いてない場合は disabled になっている。

## text2pcap
wireshark付属ツール

- linuxだと /usr/sbin/text2pcap みたい
    - rpm -ql wiresharkで探せばわかる

以下のような書式のファイルを与えてやる。

```
0000   45 00 02 08 d2 90 40 00 40 11 bf f3 c0 a8 89 80
0010   0a 3a 51 fe
```

実行例

```
$ text2pcap infile outfile.pcap
```

上記書式は wireshark からコピーして得ればよい。

## cflowをキャプチャできない
cflow とは NetFlow パケットの Wireshark 上でのプロトコル名。

- 宛先ポートを 2055 にしたらok
    - こうしないと、ただの udp パケットとして wireshark 上では見える

## ショートカットキー
ctrl + w   : キャプチャを閉じる

ctrl + r   : キャプチャを再開

## pcapファイルの生成
キャプチャ後に停止し、file > export specific packets から。

## パケット内容のコピー
先頭の「Frame」を選んで Copy すれば、パケット全体をコピーできる。

どこ(Hex? )をコピーするかは Copy のサブメニューから選べる。

以下は例。

```
Hex
0000   45 00 02 08 d2 90 40 00 40 11 bf f3 c0 a8 89 80
0010   0a 3a 51 fe
```

```
Hex Stream
45000208d29040004011bff3c0a889800a3a51fe
```
