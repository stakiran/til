# git config
断りがない場合は windows 前提かも。

## git credential cache 時間伸ばすのとクリア
- デフォは 15min

伸ばす

```
git config --global credential.helper "cache --timeout 3600"
```

他人の認証をクリアする

```
$ ps
$ (git-credential-) のプロセス pid
$ kill
```

## gitconfig location
%userprofile%\.gitconfig

## http proxy 周り
- http.proxy のみで **https.proxyは不要**
- postBuffer はでかい repo 扱ってて動作しない場合(細かい設定背景忘れた)
- `[http "..."]` でドメイン個別に異なる設定が使える

```
[http]
	proxy = http://(IP):(PORT)
	postBuffer = 33554432
[http "https://(Domain-1)"]
	sslCAInfo=D:/data/crt/xxxx.cer
[http "https://(Domain-2)"]
	proxy = http://(IP):(PORT)
	sslCAInfo=D:/data/crt/xxxx.pem
```

## credential 
- ドメイン個別可能
- Windows なら wincred が楽だと思う

```
[credential]
	helper = wincred
[credential "https://(Domain-For-AWS)"]
	helper = !aws codecommit credential-helper $@
	UseHttpPath = true
```

## エイリアス
サンプルとして。

```
[alias]
	b = branch
	c = commit
	co = checkout
	s = status
	ss = status --short
	d = diff
	pl = pull
	po = push origin
	pom = push origin master
	ls = log --pretty=oneline --abbrev-commit
	ll = log --date=short --pretty=format:'%Cgreen%h %ad(%cr) %Creset%s'
	lt = log --date=short --pretty=format:'%Cgreen%h %ad%Creset'
	lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
```
