# Microsoft Azure AD Active Directory

## テナントIDをゲットする
ディレクトリ名がわかれば取れる。

> https://login.windows.net/YOURDIRECTORYNAME.onmicrosoft.com/.well-known/openid-configuration にアクセスすると、テナントIDを含む多数のURLが表示されます。

[azure — AzureアカウントのテナントIDを取得する方法](https://www.it-swarm-ja.tech/ja/azure/azure%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E3%83%86%E3%83%8A%E3%83%B3%E3%83%88id%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/1049056202/)

他にも azure login からの azure account show など色々あるみたい。
