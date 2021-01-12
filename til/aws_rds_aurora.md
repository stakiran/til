# AWS RDS Relational Database Service

## RDS 基礎概念
- フルマネの RDB
    - EC2 で自力で DB 動かすよりも楽
- 使えるエンジン
    - MySQL, PostgreSQL, MariaDB
    - Aurora
    - Oracle, SQL Server


## Aurora 基礎概念
- MySQL 互換
- 3-AZ に 2 つずつの計 6 重

cluster

- contains: master, reader(read replica)s

master と reader

- master が読み書き担当、1台だけ
- それ以外は reader で、読み込み専用かつ master の予備要員

## see
- [AWS再入門 Amazon RDS編 | Developers.IO](https://dev.classmethod.jp/articles/cm-advent-calendar-2015-aws-re-entering-rds/)

