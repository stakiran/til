# Twitter

## エクスポート > データフォーマットメモ
tweet.js

```
  "tweet" : {
    "retweeted" : false,
    "source" : "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
    "entities" : {
      "hashtags" : [ {
        "text" : "oldprofile",
        "indices" : [ "0", "11" ]
      }, {
        "text" : "Tritask",
        "indices" : [ "78", "86" ]
      } ],
      "symbols" : [ ],
      "user_mentions" : [ ],
      "urls" : [ ]
    },
    "display_text_range" : [ "0", "147" ],
    "favorite_count" : "0",
    "id_str" : "1225030257264054274",
    "truncated" : false,
    "retweet_count" : "0",
    "id" : "1225030257264054274",
    "created_at" : "Wed Feb 05 12:15:47 +0000 2020",
    "favorited" : false,
    "full_text" : "#oldprofile\n\n知的生産と自己管理の技術を探求しています。備忘とタスク管理が好き。座右の銘はストレスフリーとベストエフォート。愛用はタスク管理( #Tritask )/プレーンテキスト/ミニマリズム。運動はランニングマン（not ランニング）。地元広島のお好み焼きが恋しい東京暮らし。",
    "lang" : "ja"
  }
```

tweet_media/1036056217368457216-DmDPlpAU8AUb6mB.jpg

- `tweet_media/(expanded_urlのとこ)-(media_urlのとこ).jpg`

```
  "tweet" : {
    ……
    "extended_entities" : {
      "media" : [ {
        "expanded_url" : "https://twitter.com/stakiran2/status/1036056217368457216/photo/1",
        "media_url" : "http://pbs.twimg.com/media/DmDPlpAU8AUb6mB.jpg",
        "id_str" : "1036056159864549381",
        "id" : "1036056159864549381",
        "media_url_https" : "https://pbs.twimg.com/media/DmDPlpAU8AUb6mB.jpg",
        ……
```

## エクスポート > 全般
- 設定 > アカウント > twitter データをダウンロード
- そのうちメールでリンク飛んでくる（即座ではない）
  - https://anywhere.twitter.com/settings/your_twitter_data/data
- 30日経たないと再度不可能

DM データなども含む。以前の github pages に置けた html 形式ではない…… at 2020/02/06 18:23:16

構造

```
.
│  account-creation-ip.js
│  account-suspension.js
│  account-timezone.js
│  account.js
│  ad-engagements.js
│  ad-impressions.js
│  ad-mobile-conversions-attributed.js
│  ad-mobile-conversions-unattributed.js
│  ad-online-conversions-attributed.js
│  ad-online-conversions-unattributed.js
│  ageinfo.js
│  block.js
│  connected-application.js
│  contact.js
│  device-token.js
│  direct-message-group-headers.js
│  direct-message-group.js
│  direct-message-headers.js
│  direct-message.js
│  email-address-change.js
│  follower.js
│  following.js
│  ip-audit.js
│  like.js
│  lists-created.js
│  lists-member.js
│  lists-subscribed.js
│  moment.js
│  mute.js
│  ni-devices.js
│  periscope-account-information.js
│  periscope-ban-information.js
│  periscope-broadcast-metadata.js
│  periscope-comments-made-by-user.js
│  periscope-expired-broadcasts.js
│  periscope-followers.js
│  periscope-profile-description.js
│  personalization.js
│  phone-number.js
│  profile.js
│  protected-history.js
│  README.txt
│  saved-search.js
│  screen-name-change.js
│  tweet.js
│  verified.js
│  
├─direct_message_group_media
├─direct_message_media
│      1189444367146082310-G3HVoVfc.jpg
│      1189444415154094085-9biAkqcy.jpg
│      
├─moments_media
├─moments_tweets_media
├─profile_media
│      831835765201985540-UEYKP2Nc.jpg
│      
└─tweet_media
        1036056217368457216-DmDPlpAU8AUb6mB.jpg
        ……
        1225025199294173184-EQAp7KQVAAAUQCe.png
        
```
