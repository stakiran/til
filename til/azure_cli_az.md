# Azure CLI

## user, role
```
az ad signed-in-user show

az role assignment list --all
```

## blob storage
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

## image

```
$ az vm image list --output table
Offer                         Publisher               Sku                 Urn                                                             UrnAlias             Version
----------------------------  ----------------------  ------------------  --------------------------------------------------------------  -------------------  ---------
CentOS                        OpenLogic               7.5                 OpenLogic:CentOS:7.5:latest                                     CentOS               latest
debian-10                     Debian                  10                  Debian:debian-10:10:latest                                      Debian               latest
flatcar-container-linux-free  kinvolk                 stable              kinvolk:flatcar-container-linux-free:stable:latest              Flatcar              latest
openSUSE-Leap                 SUSE                    42.3                SUSE:openSUSE-Leap:42.3:latest                                  openSUSE-Leap        latest
RHEL                          RedHat                  7-LVM               RedHat:RHEL:7-LVM:latest                                        RHEL                 latest
SLES                          SUSE                    15                  SUSE:SLES:15:latest                                             SLES                 latest
UbuntuServer                  Canonical               18.04-LTS           Canonical:UbuntuServer:18.04-LTS:latest                         UbuntuLTS            latest
WindowsServer                 MicrosoftWindowsServer  2019-Datacenter     MicrosoftWindowsServer:WindowsServer:2019-Datacenter:latest     Win2019Datacenter    latest
WindowsServer                 MicrosoftWindowsServer  2016-Datacenter     MicrosoftWindowsServer:WindowsServer:2016-Datacenter:latest     Win2016Datacenter    latest
WindowsServer                 MicrosoftWindowsServer  2012-R2-Datacenter  MicrosoftWindowsServer:WindowsServer:2012-R2-Datacenter:latest  Win2012R2Datacenter  latest
WindowsServer                 MicrosoftWindowsServer  2012-Datacenter     MicrosoftWindowsServer:WindowsServer:2012-Datacenter:latest     Win2012Datacenter    latest
WindowsServer                 MicrosoftWindowsServer  2008-R2-SP1         MicrosoftWindowsServer:WindowsServer:2008-R2-SP1:latest         Win2008R2SP1         latest

$ az vm image list --offer RHEL --all --output table 
かなり時間かかる。分レベル。
```

## vm

```
$ az vm show -g rg1 -n vm1
```

## vm disk datadisk osdisk

```
az vm show -g RGNAME -n VMNAME --query "storageProfile.dataDisks"

az vm show -g RGNAME -n VMNAME --query "storageProfile"
```

## regions

```
az account list-locations | jq ".[] | {displayname: .displayName, name: .name}"
```
