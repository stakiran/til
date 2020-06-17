# Ansible Tasks レシピ集
試したのをひたすら溜めてく。

## .

```yaml
.
```

## .

```yaml
.
```

## 空ファイル作成 empty file

```yaml
- name: ensure file exists
  copy:
    content: ""
    dest: /etc/nologin
    force: no
    group: sys
    owner: root
    mode: 0555
```

[How to create an empty file with Ansible? - Stack Overflow](https://stackoverflow.com/questions/28347717/how-to-create-an-empty-file-with-ansible)

## debug デバッグメッセージ
- var で直に書くか、msg で `{{xxx}}` 表記するか
- register を使えばモジュール実行結果も見れる

```yaml
- debug: var=ansible_env.PWD

- debug: msg="Current directory is {{ ansible_env.PWD }}!"

- name: test commandline1
  command: set | grep -i ansible
  register: ansible_env_variables

- debug: var=ansible_env_variables
```

## make directory folder
- file モジュールの directory state を使う

```yaml
- name: test make directory
  file: path=./testDir state=directory
```

## unzip
- unzip をインストールした上で、unarchive で zip 指定
- src と dest は両方とも存在してないといけない＆リモート側ファイルを扱うために remote_src を立てる

```yaml
- name: test install unzip with yum
  yum: name=unzip state=present

- name: test unzip with ansible module
  unarchive:
    src: ./src.zip
    dest: ./unzippedDir
    # required for unarchiving on remote file directly.
    remote_src: yes

```

## download and install pip
command モジュール等で get-pip.py 叩くしかないみたい（pip install するモジュールはない）。

```yaml
- block:

  - name: download pip
    get_url:
      url: "https://bootstrap.pypa.io/get-pip.py"
      dest: ./get-pip.py
      force: yes
      sha256sum: "b86f36cc4345ae87bfd4f10ef6b2dbfa7a872fbff70608a1e43944d283fd0eee"

  - name: install pip
    command: "python get-pip.py"
```

## curl get-url
- これで冪等性担保。デフォだと同名存在時にスルーされるけど、これだとハッシュ見てくれる
- ハッシュは sha256sum コマンドで事前にゲットしとく

```yaml
- name: download hoge
  get_url:
    url: "https://……hoge.zip"
    dest: ./hoge.zip
    force: yes
    sha256sum: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```
