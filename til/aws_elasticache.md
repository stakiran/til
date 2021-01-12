# AWS ElastiCache

## 基礎概念
- AWSのインメモリキャッシュサービス
- フルマネ
- エンジンは Redis と memcached が選べる

構造

- cluster
    - shard
        - 1-primary-node
        - N-read-replica-node

[RedisとElastiCacheを分かりやすくまとめてみた - Qiita](https://qiita.com/gold-kou/items/966d9a0332f4e110c4f8#elasticache)
