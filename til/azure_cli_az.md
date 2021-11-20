# Azure CLI

## user, role
```
az ad signed-in-user show

az role assignment list --all
```

## storage
事前に connection string 入れておく

```
set AZURE_STORAGE_CONNECTION_STRING=……
```

```
$ az storage blob directory download -c container1 -d . -s *
```

コンテナ container1 にあるファイルを全部カレントディレクトリにダウンロード

```
$  az storage blob directory upload -c container1 -d container_folder1 -s file1.txt
```

コンテナ container1 の /container_folder1/ に、ローカルの file1.txt をアップロード
