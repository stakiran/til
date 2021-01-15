# AWS インスタンスたち

## スポットインスタンス
- AWS が余らせてるインスタンスを安く使う
- > 「この料金まで支払うことが出来る」というサーバの入札価格を決め、時系列に変動するサーバ価格が入札価格より低い場合に、利用することが出来ます。
- 入札価格を下回った場合、**起動中のインスタンスも停止してしまう**
    - ので用途は限定的

[スポットインスタンスを安定して利用するための取り組み - Qiita](https://qiita.com/megadreams14/items/766ce04ca6cb418e95ca)

### スポットフリート？
- 入札条件を複数指定できる感じ

> 予め最高価格と復数のインスタンスタイプとAvailability Zoneを設定しておくことでその中で一番安いスポットインスタンスをn個用意するということを自動で出来るようになる

- わからんのでソース含めて解読すると、
- 以下を指定する
    - 入札価格
    - 何個インスタンスを確保するか
    - launch configulation xN
        - 1-launchconfigulation has 1-subnet(1-AZ) and 1-instancetype
- 入札価格を下回った launch configulation（のインスタンス）のうち、最も安いものが n 個用意される

[Spot Fleetを使ってEC2を1/4の料金で運用する - Qiita](https://qiita.com/f96q/items/28d3c2dd7ad55bf06747)

