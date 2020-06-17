# drivers etc hosts 

## パス

```
notepad C:\Windows\System32\drivers\etc\hosts
vi /etc/hosts
```

## 記法
- 区切りはスペースで良い
    - タブも可能
- ホスト名が複数あれば一行に連ねられる

```
10.0.0.1 ip-10-0-0-1 ip-10-0-0-1.ap-northeast-1.compute.internal
```

## 照合順
- hostname
- hosts
- DNS
