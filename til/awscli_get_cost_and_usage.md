# AWSCLI get-cost-and-usage
- 以下は第一キーが region、第二キーが service タグの場合
    - リージョンごと Service タグごとの値が取れる
- filter は jsonstring でエグいので、別の手段で生成させるのが賢い
- metrics は正直よくわからん
    - ブレンドと非ブレンドの違いとか
    - どっちでも値同じだったりするし

```
aws ce get-cost-and-usage --time-period Start=2021-03-01,End=2021-04-01 --granularity MONTHLY --metrics "BlendedCost" --group-by Type=DIMENSION,Key=REGION Type=DIMENSION,Key=SERVICE --filter "{\"Tags\":{\"Key\":\"Service\",\"Values\":[\"your-service-tag\"]}}"
```

## filter でワイルドカード的なこと
- できない
    - コストグループっての使えばできるらしい（？）が試してない
- なので OR で愚直に全部並べていくしかない
    - 例: your-servicetag-1 と your-servicetag-2 の両方を引っ張りたい場合
    - `--filter "{\"Or\":[{\"Tags\":{\"Key\":\"Service\",\"Values\":[\"your-servicetag-1\"]}},{\"Tags\":{\"Key\":\"Service\",\"Values\":[\"your-servicetag-2\"]}}]}"`

## Service タグ？
- コスト系のフィルタリングで使えるタグは Service タグのみ
    - 任意のタグ（たとえば Name タグ）が使えるわけではない
- タグがついてない場合は No Tag 扱い
    - `--filter "{\"Tags\":{\"Key\":\"\",\"Values\":[]}}"`
