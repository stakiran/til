# JsZip

## zip オブジェクトに「別からダウンロードしてきた zip ファイルの中身(blob)」を入れる
- loadAsync で読み込ませる


```js
// blobs は [blob, blob, ……]
// blob は以下参照
const loadAll = async (zip, blobs) => {
  for(const blob of blobs){
    await zip.loadAsync(blob);
  }
  return zip;
}

const promise = loadAll(zip, blobs).then((zip) => {
  return zip.generateAsync({type:'blob'});
}).then((zipContent) => {
  const filename = 'hoge.zip';
  fileSaver(zipContent, realFilename); // file-saver 使ってダウンロードさせる例
})
```

blob としてこれを想定

```js
const config = {
  'responseType' : 'blob',
  'headers' : {
    'Content-Type' : 'application/zip',
  },      
}
axios.get(roleFilePath, config).then((response) => {
  const blob = response.data
  return blob
)
```

## 任意のディレクトリ構造の zip をつくる
- Zip オブジェクトの file() や folder() で追加していく
- ディレクトリ構造を表すデータ構造から Zip をつくる処理をつくると優しい
    - ここでは
    - directory という「ディレクトリなら obj、ファイルなら string を value にする」構造を定義
    - updateZip() で再帰的につくる

```js
updateZip(directory, jszipFolder) {
  Object.keys(directory).forEach((key) => {
    const filenameOrFoldername = key;
    const value = directory[key];

    const isFolder = typeof value == "object";
    if (isFolder) {
      const foldername = filenameOrFoldername;
      const subFolder = jszipFolder.folder(foldername);
      this.updateZip(value, subFolder);
      return; // continue
    }

    const isFile = typeof value == "string";
    if (isFile) {
      const filename = filenameOrFoldername;
      const filecontent = value;
      jszipFolder.file(filename, filecontent);
      return; // continue
    }

    const o = JSON.stringify(directory)
    const k = key
    throw new Error(`Invalid format of directory.\nkey:${k}\n${o}`
    );
  });
}

const directory = {
  "readme.md": "readme.mdの中身",
  folder1: {
    folder2: {
      "hoge.txt" : "hoge.txtの中身"
    }
  }
};

const zip = new JSZip();
updateZip(directory, zip)
```
