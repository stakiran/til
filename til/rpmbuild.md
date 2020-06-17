# rpmbuild

## define 内にコマンドを書く
%define revision %(echo $SVN_REVISION)

## RPM とか SOURCE とかのディレクトリはどうやって指定する？
_topdir のこと。

```
#!/bin/sh
./clean.sh
rpmbuild --define="%_topdir `pwd`/../../RPMTEMP" hoge.spec -bb --target x86_64
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                   ここで指定

${RPM_BUILD_ROOT} は、 /opt/hoge など実際に配置する階層でファイルを配置するところ。
+ _topdir
 + RPM
 + SOURCE
 + RPMBUILDROOT <- こんな感じで作られる
  + opt
   + hoge
    ...
```

## オプション

```
-bp で %prep だけ。
-bc で %prep と %build。
-bi で %prep と %build と %install
-bb で biとバイナリパッケージビルド（rpmつくる）。%clean も実行される。
```

## %prop とか %install とか

```
%prep    ソースをビルドする前に実施する準備事項
%build   ソースのビルド手順
%install ソースからのインストール手順
%check   ビルドされたバイナリが正常に動作するか検証する手順
%clean   パッケージ作成後の後始末
%pre     RPMパッケージをインストールするときパッケージの展開前に行うことを書く
%post    RPMパッケージをインストールするときパッケージの展開後に行うことを書く
%preun   RPMパッケージをアンインストールするとき展開ファイルの削除前に行うことを書く
%postun  RPMパッケージをアンインストールするとき各ファイルを削除した後に行うことを書く
```

from https://vinelinux.org/docs/vine6/making-rpm/make-spec.html#mr-script

## 最低限試した際のコマンドライン

```
$ /path/to/install/a.out
Hello World!

$ pwd
/path/to/rpmbuild

$ cat plain.spec
Name: rpmbuild_try
Summary: try for studying rpmbuild.
Version: 1.0.0
Release: rel1
License: NYSL
Group: Applications/System
URL: http:/www.google.co.jp/
Vendor: vendor1

%description
rpmbuild try!

%prep
touch spec_prep.txt

%build
touch spec_build.txt

%install
touch spec_install.txt
install -m 755 "/path/to/install/a.out" "$RPM_BUILD_ROOT/rpmbuildtry"

%clean
touch spec_clean.txt

%pre
touch spec_pre.txt

%post
touch spec_post.txt

%preun
touch spec_preun.txt

%postun
touch spec_postun.txt

%files

%changelog
* Sun May 14 2017 Hoge Fuga <mailaddress@mailaddress.com> - 0.1.4-0
- comment1
- comment2

$ rm -rf /path/to/rpmbuild/root/
★rpmbuildの作業ディレクトリを消している

$ rpmbuild --define="__check_files %{nil}" --define="%_topdir /path/to/rpmbuild/root" plain.spec -bb --target x86_64
...
実行中(%prep): /bin/sh -e /var/tmp/rpm-tmp.XZAAXC
...
実行中(%build): /bin/sh -e /var/tmp/rpm-tmp.9zGzTX
...
実行中(%install): /bin/sh -e /var/tmp/rpm-tmp.W2H9Pi
...
Processing files: rpmbuild_try-1.0.0-rel1.x86_64
書き込み完了: /path/to/rpmbuild/root/RPMS/x86_64/rpmbuild_try-1.0.0-rel1.x86_64.rpm
実行中(%clean): /bin/sh -e /var/tmp/rpm-tmp.dUYYjZ
...

$ ls -R
.:
plain.spec  root

./root:
BUILD  BUILDROOT  RPMS  SOURCES  SPECS  SRPMS

./root/BUILD:
spec_build.txt  spec_clean.txt  spec_install.txt  spec_prep.txt

./root/BUILDROOT:
rpmbuild_try-1.0.0-rel1.x86_64

./root/BUILDROOT/rpmbuild_try-1.0.0-rel1.x86_64:
rpmbuildtry

./root/RPMS:
x86_64

./root/RPMS/x86_64:
rpmbuild_try-1.0.0-rel1.x86_64.rpm

./root/SOURCES:

./root/SPECS:

./root/SRPMS:

$ rpm -ivh ./root/RPMS/x86_64/rpmbuild_try-1.0.0-rel1.x86_64.rpm
準備中...                ########################################### [100%]
   1:rpmbuild_try           ########################################### [100%]


$ rpm -ivh ./root/RPMS/x86_64/rpmbuild_try-1.0.0-rel1.x86_64.rpm
準備中...                ########################################### [100%]
        パッケージ rpmbuild_try-1.0.0-rel1.x86_64 は既にインストールされています。

$ rpm -qa | grep rpmbuild_try
rpmbuild_try-1.0.0-rel1.x86_64

$ rpm -e rpmbuild_try

$ rpm -qa | grep rpmbuild_try
```
