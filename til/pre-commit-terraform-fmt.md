# pre-commit
- https://pre-commit.com for more information
- https://pre-commit.com/hooks.html for more hooks

## pre-commit 基本

```
$ pip install pre-commit

$ pre-commit sample-config > .pre-commit-config.yaml

$ pre-commit install
$ pre-commit uninstall
が、基本的には yaml 書き換えて install する、の流れで良いっぽい
```

```
どう働く？(fmtを例に)
 commit時に自動で走る
 case1 もしfmtの結果とズレてる場合は、failedにしてcommitを取り下げる
  このとき裏では自動でfmtしてくれている
 case2 ズレてない場合はpassedとなって、commitを取り下げない
 case3 nothing to commitのときはskippedで何もしない
```

## terraform fmt だけ行いたい
- ❌ https://github.com/antonbabenko/pre-commit-terraform
    - 最初これ使おうとした
    - けど terraform.exe がたぶん直に PATH 通ってないとだめそう
        - 自分は alauncher でバッチファイル経由で通してるので
- ので local

```
repos:
  - repo: local
    hooks:
      - id: terraform-fmt
        name: terraform-fmt
        entry: terraform 
        args: ['fmt', '-recursive']
        language: system
        pass_filenames: false
```

- entry が本体で、args に引数
- language は `system`
    - entry に指定されたコマンドをシステムから探す、的な意味になる
    - 要するにこれ指定しないとたぶん PATH を見てくれない
- pass_filenames は true だと動かんので false に
    - `Only .tf and .tfvars files can be processed with terraform fmt` で怒られるので

## hooks.language
https://github.com/pre-commit/pre-commit/blob/e1ce4c0bf32f905a93dd22f0bd9be26c2561ab6a/pre_commit/languages/all.py

```
conda
coursier
dart
docker
docker_image
dotnet
fail
golang
lua
node
perl
pygrep
python
r
ruby
rust
script
swift
system
```
