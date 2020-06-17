# format link

## 動作しないバグを直す
[Firefox の Format Link の直し方 - Qiita](https://qiita.com/scivola/items/c08e5b46be491470d9b7)

```
[1] ロケーションバーに about:debugging#/runtime/this-firefox と打つ
[2] Format Link の「調査」をクリック（コンソールが出る）
[3] コンソール上で await browser.storage.sync.set(DEFAULT_OPTIONS); と打つ
```
