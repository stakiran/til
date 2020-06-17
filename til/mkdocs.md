# MkDocs

## サンプル2
- 絵文字やタスクリストは pymdown を使う
  - materialテーマにはすでに入っている
- .git の除外は plugin の exclude で、glob で
- ビルド時に認識されない場合は、nav で index に当たるファイルを指定

```yaml
site_name: GitLab Wiki コンテンツを MkDocs 化するサンプル
use_directory_urls: false
docs_dir: selfla-saas-2020-1q-comparison-with-lean.wiki
site_dir: output_html_leanwiki
nav:
    - 'home.md'
theme:
    name: 'material'
    language: 'ja'
markdown_extensions:
    - toc:
        permalink: True
    - mdx_truly_sane_lists:
        nested_indent: 4
    - pymdownx.emoji:
        emoji_generator: !!python/name:pymdownx.emoji.to_svg
    - pymdownx.tasklist:
        custom_checkbox: true
extra:
    search:
        language: 'jp'
plugins:
    - exclude:
        # Exclude .git folder etc.
        glob:
            - '**/.*/*'
```

## サンプル1
- docs_dir と site_dir
  - ソースとビルド先を指定
  - yml ファイルより上のディレクトリ(../docsとか)は指定不可
    - **ymlファイルと同じ階層にある md を ./ とかで指定するのも不可能**
- use_directory_urls: false
  - index.html までリンクさせるのに必要(これしないとローカルで生成サイト開いた時にリンク先ページを開けない)
- mdx_truly_sane_lists でインデント2スペースリスト(これしないと4スペースしか認識されない)
  - pip install mdx_truly_sane_lists
- material テーマは日本語検索に対応している

```
site_name: マイサイト
use_directory_urls: false
docs_dir: wiki
site_dir: wiki_public
theme:
  name: 'material'
  language: 'ja'
markdown_extensions:
    - toc:
        permalink: True
    - mdx_truly_sane_lists:
        nested_indent: 2
extra:
  search:
    language: 'jp'
```

## css
src 配下に css ファイルを置く。

extra_css で **docs_dir 基点で指定** する。

```
extra_css:
    - css/extra.css
```

ビルド時は src 配下がコピーされる感じ。


## 生成したサイトで index.html が開かれない
ローカルで生成サイトを開くとそうなる。

これは [OS側の仕様](https://support.mozilla.org/ja/questions/1176131)。`website/dir1` にアクセスした時に `website/dir1/index.html` が返されるのは、ウェブサーバー側がそうしてるからにすぎない。 index.html まで開かせたいなら `mkdocs serve` でローカルサーバーを立ち上げてから読むしかなさそう。
→ use_directory_urls: false 使えば ok

## material テーマ
https://github.com/squidfunk/mkdocs-material

pip install mkdocs-material

