# Linux Disk df fdisk mkfs mount etc...

## ディスク情報
df

```
  [ec2-user@ip-10-0-0-1 ~]$ df
  Filesystem     1K-blocks    Used Available Use% Mounted on
  /dev/nvme0n1p2  10473452 1066888   9406564  11% /
  devtmpfs         1887012       0   1887012   0% /dev
  tmpfs            1909536       0   1909536   0% /dev/shm
  tmpfs            1909536    8624   1900912   1% /run
  tmpfs            1909536       0   1909536   0% /sys/fs/cgroup
  tmpfs             381908       0    381908   0% /run/user/1000
  tmpfs             381908       0    381908   0% /run/user/0
```

lsblk

```
  [ec2-user@ip-10-0-0-1 ~]$ lsblk
  NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
  nvme0n1     259:0    0   10G  0 disk 
  ├─nvme0n1p1 259:1    0    1M  0 part 
  └─nvme0n1p2 259:2    0   10G  0 part /
  nvme1n1     259:3    0    2G  0 disk 
  ├─nvme1n1p1 259:4    0    1G  0 part 
  └─nvme1n1p2 259:5    0 1023M  0 part  
```

## パーティション
fdisk

```
  パーティション作成
  fdisk /dev/sba
```

## ファイルシステム
mkfs

```
  ファイルシステム作成
  mkfs -t ext3 /dev/sdb2
```

## マウント
mount

```
  マウント実行
  mount 対象パス マウント先ディレクトリ
  mount /dev/sdb2 /mnt/md1
```

umount

```
  アンマウント実行
  umount /dev/sdb2
```

# fdisk で 2G ディスクからパーティションを 2 つつくる例
- 基本的に p(プライマリ) を使う
- 範囲指定は +1GB など結構自由に指定できる
- p で確認しつつ、ok なら w で書き込むことで完了する
- RHEL7 だと /dev/nvme1n1 ← ディスク名こんな感じのネーミングになる


```
[ec2-user@ip-10-0-0-1 ~]$ sudo fdisk /dev/nvme1n1
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table
Building a new DOS disklabel with disk identifier 0x480ceda2.

Command (m for help): p

Disk /dev/nvme1n1: 2147 MB, 2147483648 bytes, 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x480ceda2

        Device Boot      Start         End      Blocks   Id  System

Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): p
Partition number (1-4, default 1): 
First sector (2048-4194303, default 2048): 
Using default value 2048
Last sector, +sectors or +size{K,M,G} (2048-4194303, default 4194303): +1G
Partition 1 of type Linux and of size 1 GiB is set

Command (m for help): p

Disk /dev/nvme1n1: 2147 MB, 2147483648 bytes, 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x480ceda2

        Device Boot      Start         End      Blocks   Id  System
/dev/nvme1n1p1            2048     2099199     1048576   83  Linux

Command (m for help): n
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): p
Partition number (2-4, default 2): 
First sector (2099200-4194303, default 2099200): 
Using default value 2099200
Last sector, +sectors or +size{K,M,G} (2099200-4194303, default 4194303): 
Using default value 4194303
Partition 2 of type Linux and of size 1023 MiB is set

Command (m for help): p

Disk /dev/nvme1n1: 2147 MB, 2147483648 bytes, 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x480ceda2

        Device Boot      Start         End      Blocks   Id  System
/dev/nvme1n1p1            2048     2099199     1048576   83  Linux
/dev/nvme1n1p2         2099200     4194303     1047552   83  Linux

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
[ec2-user@ip-10-0-0-1 ~]$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
nvme0n1     259:0    0   10G  0 disk 
├─nvme0n1p1 259:1    0    1M  0 part 
└─nvme0n1p2 259:2    0   10G  0 part /
nvme1n1     259:3    0    2G  0 disk 
├─nvme1n1p1 259:4    0    1G  0 part 
└─nvme1n1p2 259:5    0 1023M  0 part 
[ec2-user@ip-10-0-0-1 ~]$ sudo mkfs -t ext4 /dev/nvme1n1p
nvme1n1p1  nvme1n1p2  
[ec2-user@ip-10-0-0-1 ~]$ sudo mkfs -t ext4 /dev/nvme1n1p2
mke2fs 1.42.9 (28-Dec-2013)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
65536 inodes, 261888 blocks
13094 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=268435456
8 block groups
32768 blocks per group, 32768 fragments per group
8192 inodes per group
Superblock backups stored on blocks: 
        32768, 98304, 163840, 229376

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (4096 blocks): done
Writing superblocks and filesystem accounting information: done
```
