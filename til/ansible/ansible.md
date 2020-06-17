# Ansible
[ansible playbook コマンド · yteraoka/ansible-tutorial Wiki](https://github.com/yteraoka/ansible-tutorial/wiki/ansible-playbook%20%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)

## crontab は cron モジュール
- name は必須（ドキュメントには state=present 時は要らないとあるが future では required になる）
- state present にしたら冪等性確保できる
    - name を id（もっというと `#Ansible (name)` というコメント）で見ているので被らないようには注意必要？
- `* 5 * * *` ← これ系はデフォが * だと覚えておき、変えたいものだけ指定する

```
- name: Add job to execute reboot every AM 5
  become: true
  cron:
    name: "reboot self every AM 5"
    hour: "{{ restart_hour_at }}"
    job: "/usr/sbin/shutdown -r 0"
    state: present
```

## sed を ansible でやるなら replace
他にも lineinfile モジュールも使えるみたいだがまだ試してない

```
sed -e 's/^apply_updates = no/apply_updates = yes/' -e 's/^update_cmd = default/update_cmd = security/' -i /etc/yum/yum-cron.conf
```

↓

```
- name: edit yum-cron.conf > apply_updates to yes
  become: true
  replace:
    path: "{{ yumcron_conf_path }}"
    regexp: '^apply_updates = no'
    replace: 'apply_updates = yes'

- name: edit yum-cron.conf > update_cmd to security
  become: true
  replace:
    path: "{{ yumcron_conf_path }}"
    regexp: '^update_cmd = default'
    replace: 'update_cmd = security'
```

## become_user はデフォ root だが前タスク指定分が残ったままなので注意
root を使いたいなら、明示的に `become_user: root` などと指定するのが確実。

## copy モジュールでファイルの permission パーミッションが変わらない
操作対象サーバー側の当該ファイルをいったん削除する。


## 変数の存在確認

```
    - name: "NAT インスタンスのIPが与えられているか"
      assert:
        that: dest_nat_instance_ip is defined
```

see: [Conditionals — Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html#the-when-statement)

`not var1` で var1==false

`var1 is defined` と `var1 is undefined` が使える

## set_fact モジュールには name: つけても表示されない
なぜだ見づらいやん

## 環境変数をいじる environement var export set
- environment モジュールなるものは存在しない
    - タスク単位でのみ有効になる特殊構文っぽい
- 恒久設定したいなら .bashrc などに export する
    - ただ shell や command で `echo >>` すると、上手く when で弾いてやらないと毎回追記されることに……

インスタンス生成時（AWS CFn の場合は UserData など）に書いちゃうのが良いのかもしれない？

## ansible_user, ansible_host, ansible_connection, ansible_password ← このへんのリファレンス
see https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html

## ansible playbook 実行時に変数を定義する parameter パラメータを渡す
`-e` オプションで jsonstring 与えれば可能

```
$ ansible-playbook -i ... test.yml -e '{"source_ip":"192.168.1.1","dest_ip":"192.168.1.2"}'
```

playbook からは `{{ source_ip }}` でアクセス

## ansible で簡単にテストコードっぽいことをする
データは `-e` で渡してもらうと楽。

```
$ ansible-playbook -i ... test.yml -e '{"source_ip":"192.168.1.1","dest_ip":"192.168.1.2"}'
```

test.yml > まずはログインしたい先のホスト情報を add host

```
---
- name: "Prepare"
  hosts: myhost1
  gather_facts: no
  tasks:
    - name: "add host でログインしたい先のホスト情報を追加する"
      add_host:
        name: "source"
        ansible_host: "{{ source_ip }}"
        ansible_user: ...
        ansible_password: ...
        ansible_port: 22
        groups:
          - source_node
    - name: "同上"
      add_host:
        name: "dest"
        ansible_host: "{{ dest_ip }}"
        ...
```

test.yml > それから当該ホストを hosts: で指定して、コマンド実行するコードを書いていく

- 詳細は下記参照。assert モジュールが使える
- 冪等性どうこうじゃなくてテストしたいだけなので、command モジュールガンガン使っていい

## assert assertion テストコード簡易サンプル

```
- name: "test ping."
  hosts: source_node
  gather_facts: no
  tasks:
    - set_fact:
        ping_option: "-c 2 -w 2"
        rc_pingok : 0
        rc_pingng : 1
    - name: "Test source to dest"
      command: "ping {{ dest_ip }} {{ ping_option }}" 
      register: result
      ignore_errors: yes
    - name: "設計上 source > dest は導通できない"
      assert:
        that: "{{ result.rc }} == {{ rc_pingng }}"
      ignore_errors: yes
```

ポイント

- playbook 止まらないように ingnore_errors: yes
- set_fact で適宜変数化してわかりやすく
- assert の name は BDD じゃないが日本語でわかりやすく書くべき
- that はリストで並べることもできるが、どのアサートで死んだかわかりづらいので 1 assert 1 that が良い

## 特殊変数 special magic variables
[Special Variables — Ansible Documentation](https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html)

## template や copy やらで扱うファイルパスを相対パス基準にする際に
special variables が使える。

```
role_path     今実行している role のパス
playbook_dir  ansible-playbook 実行時に指定されたディレクトリ
              (明示指定ないならその時のカレントディレクトリ)
```

## 'bool' object has no attribute '__getitem__'
playbook のモジュールから作成させるディレクトリ構造を変えた場合に、 **内部的に整合が取れなくなって（？）発生する** ものと思われる。

- 今回のケース
    - openssh_keypair モジュールによる keypair 作成
    - ./temp に作成していた
    - これを ./temp/user1 に変更
    - このエラーが出た
    - `-vvv` とか見ても keypair はちゃんと作成されている
    - どうも（内部的に）辞書型の情報を取得する際に使う key が、不正な bool 型になってしまっていて、それが表出している感じ？
- ./temp/user1 を手動で削除後、再実行したら通るようになった

## あるホスト上でタスク実行中に、一時的に別ホストで実行する
delegate_to で委譲する。

```
# executing on host1...
# ...


- name: Delegate to another host2
  delegate_to: "{{ host2_name }}"
  delegate_facts: yes
  win_template:
    ...
```

## gather facts などの json を pretty で表示する
フィルタ使うと良い。nice が pretty。yaml もある。

```
- name: hoge
  hosts: hostgroup1
  gather_facts: yes
  tasks:
    - debug: msg="{{ ansible_facts | to_nice_json }}"
```

https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#filters-for-formatting-data

## windows マシンで winrm でタスクを実行するには
これしないと認証設定正しくてもタイムアウトになる。

windows マシン側で以下。以下は指定ユーザーのデスクトップ上に ps1 を配置して実行する例。適宜変えること。

```powershell
Invoke-WebRequest -Uri https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1 -Outfile C:\Users\(USER-NAME)\Desktop\ConfigureRemotingForAnsible.ps1
powershell -ExecutionPolicy Remotesigned C:\Users\(USER-NAME)\Desktop\ConfigureRemotingForAnsible.ps1
winrm set winrm/config/service/auth '@{Basic="true"}'
```

## ansible 変数定義方法
https://qiita.com/answer_d/items/b8a87aff8762527fb319#13-play-vars_prompt

大まかには以下 4 つ

- `ansible-playbook` コマンド実行時に指定するもの
- `hosts: (HostName)` 系のタスク？（名前わからん）で `vars` ディレクティブで定義するもの
- `hosts: (HostName)` 系でない、単発のタスク定義？（名前わからん）中に `vars` ディレクティブで定義するもの
    - tasks/ ディレクトリ配下で書けるもの
- set_fact, block vars, task vars

## ansible_user と ansible_ssh_user の違いは？
- 2.0 以前は ansible_ssh_user
- それ以降は ansible_user で良い
- 今後は ansible_user に統一していくらしい

## グループ host group 参照する
- debug: var=groups['group-name']

## コメントアウト comment out

```
# シャープ

# 複数行
# 同時コメントアウトは
# ないので一つずつね

# というか YAML 文法です
```

## add_host の ansible_host とか ansible_port とかのパラメーター一覧
- https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters

## ansible -v -vv -vvv vvvv varbose debug json pretty
`-v` で標準出力全部出る。

cfg で `stdout_callback = debug` すれば json も pretty になる。

## debug でコマンドラインオプション指定のみ表示させたい

```
  debug:
    var: hostvars[inventory_hostname]
    verbosity: 4
```

verbosity で v の数。1 なら -v や -vv とかで。4 なら -vvvv から表示される。

## when
- リストで繋げると and
    - [Multiple conditions that all need to be true (a logical ‘and’) can also be specified as a list:](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html#the-when-statement)

## 指定タスクのみ実行

### start-at で開始位置指定
$ ansible-playbook site.yml --start-at="test commandline1"

- 指定タスク名 **以降** を実行する
- `--step` つけたら **以降のタスクの各々** について y/n/c を指定できる
- 純粋な指定タスクのみは無理そう

### include
実行したいタスクを specific_tasks.yml に書く。


```
$ cat test_specific_tasks.yml
- name: execute test role
  become: yes
  hosts: vm1
  tasks:
    # - include: roles/test/tasks/main.yml
    - include: roles/test/tasks/specific_tasks.yml

$ ansible-playbook test_specific_tasks.yml
```

### tag
role につけるか、

```
- hosts: ws
  sudo: yes
  roles:
    - role: nginx
      tags: nginx
```

task につけて、

```
tasks:
- yum:
    name:
    - httpd
    - memcached
    state: present
  tags:
  - packages
```

実行時は `ansible-playbook example.yml --tags "configuration,packages"` こんな風に指定。

- `--skip-tag` で除外
- `--list-tasks` で実行タスク名のみ列挙

参考: [Tags — Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html)

## command モジュールと shell モジュールの使い所と使い分け
- 冪等性担保されなくなるので基本的に使うな
- command → セキュアだが環境変数やパイプやらが使えない
- shell → パイプやらも使える

参考: [Ansibleでシェルコマンドを実行させるときのノウハウ - Qiita](https://qiita.com/chroju/items/ec2f7bb87d9ae3603c6a)

## ansible playbook 実行時のカレントディレクトリを知る env

```
- debug: var=ansible_env.PWD

- debug: msg="Current directory is {{ ansible_env.PWD }}!"

```

んで --check で実行する

```
TASK [test : debug] *****************************************************************************
ok: [vm1] => {
    "ansible_env.PWD": "/home/ansible"
}

TASK [test : debug] *****************************************************************************
ok: [vm1] => {
    "msg": "Current directory is /home/ansible!"
}
```

参考: [[Ansible] 環境変数を取得する ansible_env.hoge と lookup("env", "hoge") の違い - てくなべ (tekunabe)](https://tekunabe.hatenablog.jp/entry/2019/03/09/ansible_env)

- > 主な違いは、リモートのものなのか、ローカルのものなのかでした、
-  .env だとリモート、lookip はローカル

## ansible task yaml トライアンドエラーってどうやる？ check
`--check` で実行してみればいい。

文法ミスなら以下のようにエラーが出るのでわかる。(以下は file module の state を `directoryaa` とわざと間違えてみた例)

```
TASK [test : test make directory] ***************************************************************
fatal: [vm1]: FAILED! => {"changed": false, "msg": "value of state must be one of: file, directory, link, hard, touch, absent, got: directoryaa"}
        to retry, use: --limit @/home/ansible/test_ansible/pj1/site.retry
```
        
## ansible コマンドの private key ssh 認証の挙動
一度認証が通ると **その端末ではしばらく認証が通ったままになる** という仕様みたい。

たとえば

- 1: マシン A で `ansible-playbook -i hosts site.yml --private-key=../ansible-key-pair.pem` を通した
- 2: このあと、マシン A では **しばらく --private-key 指定がなくても** 通る
- 3: しばらくしたら通らなくなる

この 2 の部分（認証がキャッシュされてる？）が謎。これのせいで ssh 周りの問題解決に苦戦しがち。

## ansible.cfg は ANSIBLE_CONFIG で設定するのが確実
これが確実っぽい

```
$ export ANSIBLE_CONFIG=/home/ansible/ansible.cfg
$ ansible -i hosts all -m ping
```

~/ansible.cfg に書くだけだと権限次第では？ロードされないことがあるみたい。

- 参考: [ansible-playbook実行時にカレントディレクトリのansible.cfgは権限によっては読まれない。 - Qiita](https://qiita.com/shiro01/items/7d58cf6bde69612d0b48)

## ansible.cfg で private key 指定を略す

```
$ cd
/home/ansible

$ ls
ansible.cfg
hosts
keysecret.pem
...

$ cat ansible.cfg
[defaults]
inventory = $HOME/hosts
private_key_file = $HOME/keysecret.pem

$ cd (yourWorkingDir)

$ ansible-playbook -i hosts site.yml --check
```

inventory 指定してるけど `-i` は省略できなかった([WARNING]: provided hosts list is empty, only localhost is available.)

[ansible.cfgの項目をリスト化してみた - Qiita](https://qiita.com/croissant1028/items/33f06298d7d05bf1e295)

## ●スタートアップ
pj1 という workDir で試す例。

### ディレクトリ構成
```
$ pwd
/home/ansible/test_ansible/pj1

$ tree
.
|-- hosts
|-- roles
|   `-- test
|       |-- README.md
|       |-- defaults
|       |   `-- main.yml
|       |-- files
|       |-- handlers
|       |   `-- main.yml
|       |-- meta
|       |   `-- main.yml
|       |-- tasks
|       |   `-- main.yml
|       |-- templates
|       |-- tests
|       |   |-- inventory
|       |   `-- test.yml
|       `-- vars
|           `-- main.yml
|-- site.retry
`-- site.yml

10 directories, 11 files
```

### hosts

```
[group1]
vm1

[group2]
vm2
```

### site.yml 

```yaml
- name: execute test role
  become: yes
  hosts: vm1
  roles:
    - test
```

### roles/test/tasks/main.yml

```yaml
- name: install unzip for test
  yum: name=unzip state=present
```

## ansible playbok 基本的なコマンドライン

```
$ ansible-playbook -i hosts site.yml --private-key=../ansible-key-pair.pem
$ ansible-playbook -i hosts site.yml --private-key=../ansible-key-pair.pem --check-syntax
$ ansible-playbook -i hosts site.yml --private-key=../ansible-key-pair.pem --check ★dryrun
```

## role ディレクトリのテンプレートをつくる
(workDir)/roles 配下でやる

```
$ cd (workDir)
$ mkdir roles
$ cd roles
$ ansible-galaxy init --offline (ロール名)`
```


## ansible command
`ansible all --list-hosts`

`ansible (specific-groupname) --list-hosts`

`ansible all -m ping`

```
$ cat ansible.cfg
[defaults]
inventory = $HOME/hosts
```

## 秘密鍵 private key を指定する
`--private-key=./ansible-key-pair.pem`

ただし pem ファイルのパーミッションが広すぎるとエラーが出る。600 くらいがよい。

## ●ansible.cfg サーチ順序
- 1: env var `ANSIBLE_CONFIG`
- 2: current directory `./ansible.cfg`
- 3: home directory `~/.ansible.cfg`
- 4: global `/etc/ansible/ansible.cfg`

## ●用語
- control node : ansible 使ってタスク実行する
- managed note : control node で操作されるノードたち
- host inventry: managed node のリスト（定義）
- ad-hoc cmd   : タスクを一度だけ流す仕組み？
- playbook     : 冪等性担保したタスクの記述。レシピ。
- module       : 共通処理をまとめたコード。ユーザー追加とかパッケージインストールとか
- idempotency  : 冪等性。冪等的。

参考: [A system administrator's guide to getting started with Ansible - FAST!](https://www.redhat.com/en/blog/system-administrators-guide-getting-started-ansible-fast?extIdCarryOver=true&sc_cid=701f2000001OH6uAAG)

## ●ディレクトリ構成

```
-production      inventory    プロダクションサーバー向け
-staging         inventory    ステージング環境向け
+group_vars                   特定グループで使う変数を定義？
 -group1.yml
 -……
+host_vars                    特定サーバーで使う変数を定義？
 -hostname1.yml
 -…
+library         (opt)
+module_utils    (opt)
-hem             (opt)
-…
+filter_plugins  (opt)
-site.yml                     master playbook
-webservers.yml               ウェブサーバー層のplaybook
-dbservers.yml                DBサーバー層のplaybook
+role
 +common
  +task
   -main.yml
  +handlers
   -main.yml
  +templates
   -ntp.conf.js
  +files
   -bar.txt
   -foo.sh
  +vars
   -main.yml
  +defaults
   -main.yml
  +meta
   -main.yml
  +library
  +module_utils
  +lookup_plugins
 +webtier
 +monitoring
 +fooapp
```
