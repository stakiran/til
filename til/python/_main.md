# Python snippet template よく使うやつ

## test と main を搭載

```
# -*- coding: utf-8 -*-

import os
import sys

def abort(msg):
    print('Error!: {0}'.format(msg))
    exit(1)

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def file2str(filepath):
    ret = ''
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = f.read()
    return ret

def str2file(filepath, s):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.write(s)

def test():
    pass

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-i', '--input', default=None,
        help='An input filename.')

    parser.add_argument('-o', '--output', default=None,
        help='An output filename.')

    parser.add_argument('--test', default=False, action='store_true',
        help='[DEBUG] Do unittest.')

    args = parser.parse_args()
    return args

def ____main____():
    pass

if __name__ == "__main__":
    args = parse_arguments()

    if args.test:
        test()
        exit(0)

    infilepath  = args.input
    outfilepath = args.output
```

## 小さいやつ

```
# encoding: utf-8

import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)
```
