# docker

## わしゃわしゃ

### build と run と push to AWS ECR
はまる

- push 時の形式は `(ecr-entrypoint)/(repo-name):(image-tag-name)` が強制
    - つまり **ビルドの時点で、この形式名のイメージを作っておく必要** がある
    - 「ローカルでは local1 という名前にして、これを指定 ECR にアップロード」みたいなことはできない
    - 「`(ecr-entrypoint)/(repo-name):(image-tag-name)` という名前でビルドして、 `(ecr-entrypoint)/(repo-name):(image-tag-name)` にアップロード」という書き方しかできない

build

```
$ docker build -t (ecr-entrypoint)/(repo-name):(image-tag-name) .
```

run

```
$ docker run -t -i (ecr-entrypoint)/(repo-name):(image-tag-name) /bin/bash
```

push 

```
$ aws ecr get-login-password --region (region-name) | docker login --username AWS --password-stdin (ecr-entrypoint)

$ docker push (ecr-entrypoint)/(repo-name):(image-tag-name)
```

## ENTRYPOINT と CMD で shellscript を使う

```
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["./script_entrypoint.sh prm1 prm2"]
```

結論

- exec式を使って、引数として「コマンドラインまるごと」を「単一文字列として」与える必要がある。
- なぜ？
    - まず bash の `-c` が「単一文字列」しか受け付けないから
    - dockerfile の shell 形式は CMD を無視するから

## none とは？
- 同じイメージ名で再度生成したときの、古い側のイメージにつく名前
- 消すには `docker image prune`
    - ただし stopped container があると消せないので、先に `docker container prune` する

## build

```
docker build -t app1-front:v1.2.3 -f docker/app1/Dockerfile .
```

- `.`
    - ここを基点として
- `-f`
    - from
    - ここのDockerfileをビルドして
- `-t`
    - to
    - このタグ名として書き出します

## misc
- 環境によってはオプションをイメージ名の前に持ってこないと解釈されないことがある
    - :x: docker run -d 10124:443 localhost/testnginx -p 10123:80 -p 
    - :o: docker run -d -p 10123:80 -p 10124:443 localhost/testnginx
- exec はコンテナに潜る
- run 時の -d はバックグラウンドで動作させるオプション
    - これしないとブロッキング状態になる

```
docker run -d localhost/testnginx
docker run -d -p 10123:80 -p 10124:443 localhost/testnginx

docker run -t -i localhost/testnginx /bin/bash

docker ps

docker stop XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
docker stop XXXXXXXXXXXX

docker exec -it XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX bash

docker logs XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

docker images

docker rmi XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
docker rmi (AWS-AccountID).dkr.ecr.ap-northeast-1.amazonaws.com/(ECR-Repo):(Image-tag-name)
```

