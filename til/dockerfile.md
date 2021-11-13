# Dockerfile

## Python + AWSCLI on AWS
ec2でdocker試すのと、ecsで動かすのと。

- pythonイメージ使って、公式手順でawscliを入れる
    - [Linux での AWS CLI バージョン 2 のインストール、更新、アンインストール - AWS Command Line Interface](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-linux.html)
- コマンド実行は RUN
- 作業ディレクトリつくる
    - cd ではなく WORKDIR
- ファイルコピーは COPY
- AWS 権限は role arn にて
    - ec2インスタンス時とecsコンテナ時で使うソースが違う（切り替え方知りたい。。。）

```
$ cat Dockerfile
FROM python:3.9

RUN apt-get update && apt-get install -y less vim curl unzip sudo

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"RUN unzip awscliv2.zip
RUN sudo ./aws/install

WORKDIR /home
RUN mkdir xworkdir
WORKDIR /home/workdir

COPY script1.py ./
COPY script_entrypoint.sh ./
RUN chmod 775 script_entrypoint.sh

RUN aws configure set default.role_arn arn:aws:iam::(ACCOUNT):role/(ROLE)

#RUN aws configure set default.credential_source EcsContainer
RUN aws configure set default.credential_source Ec2InstanceMetadata

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["./script_entrypoint.sh prm1 prm2"]
```
