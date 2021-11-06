# docker

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

