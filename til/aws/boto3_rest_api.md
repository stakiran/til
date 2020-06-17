# AWS REST API with boto3

## boto3 の公式ドキュメントが重たいです with firefox
記述部分（#right-column部分）の外をスクロールすると軽い。

## InsecureRequestWarning を消す

### 案1: python の環境変数で

```terminal
$ set PYTHONWARNINGS=ignore:Unverified HTTPS request
$ python script_with_boto3.py
```

### 案2: boto3 バンドルのソースをいじる

```python
import botocore.vendored.requests.packages.urllib3 as urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

from: https://github.com/boto/boto3/issues/699

ポイントは「 "boto3 にバンドルされてる requests" にバンドルされてる urllib3」に対してdisable_warinings が必要ってこと。

## サンプル - describe running instances

```python
# coding: utf-8

from copy import deepcopy
import datetime
import os

import boto3

ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
SECRET_KEY = os.environ['AWS_SECRET_KEY']
USE_SSL    = False

# ref memo
# --------

'''
Region names
https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/using-regions-availability-zones.html

Client class
https://boto3.readthedocs.io/en/latest/reference/core/session.html#boto3.session.Session.client

Instance class
https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#instance
'''

regions = [
    ('ap-northeast-1', 'アジアパシフィック (東京)'),
    ('ap-northeast-2', 'アジアパシフィック (ソウル)'),
    ('ap-southeast-1', 'アジアパシフィック (シンガポール)'),
    ('ap-southeast-2', 'アジアパシフィック (シドニー)'),
    # ('ap-northeast-3', 'アジアパシフィック (大阪: ローカル)'), # subscribe されてないので無理
]

def target_regions_displaystr(regions):
    ret = '対象リージョン: '
    for region in regions:
        _, name = region
        ret = ret + ' / ' + name
    return ret

def get_running_instance_information(region_name):
    ec2 = boto3.resource(
        'ec2',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=region_name,
        verify=USE_SSL
    )

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )

    ret = {
        'total' : 0,
        'instances' : [],
    }
    instance_ret_template = {
        'id'   : '',
        'type' : '',
        'tags' : {},
    }

    # len 関数サポートしてないので数える.
    total_count = 0

    for instance in instances:
        id = instance.id
        type = instance.instance_type
        tags = instance.tags

        instance_ret = deepcopy(instance_ret_template)
        instance_ret['id'] = id
        instance_ret['type'] = type
        instance_ret['tags'] = deepcopy(tags)

        ret['instances'].append(instance_ret)

        total_count += 1

    ret['total'] = total_count

    return ret

def now():
    dt = datetime.datetime.now()

    weekdays = ['月','火','水','木','金','土','日']
    wdstr = weekdays[dt.weekday()]
    datestr = dt.strftime("%Y/%m/%d")
    timestr = dt.strftime("%H:%M:%S") 

    return '{:}({:}) {:}'.format(datestr, wdstr, timestr)

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def simple_printer(ret):
    total_count = ret['total']
    instances = ret['instances']
 
    for i,instance in enumerate(instances):
        idx_for_display = i + 1

        id = instance['id']
        tags = instance['tags']
        type = instance['type']

        print('== {:} =='.format(idx_for_display))
        for tag in tags:
            k, v = tag['Key'], tag['Value']
            print('{:}={:}'.format(k, v))
        print('{:} / {:}'.format(id, type))

    print('')
    print('Total {:} instances.'.format(total_count))


outlines = []
total_count = 0
cur_count = 1

for i,region in enumerate(regions):
    region_name, region_description = region

    print('[{:}/{:}] Getting {:}...'.format(i+1, len(regions), region_description))

    ret = get_running_instance_information(region_name)
    total_count += ret['total']
    instances = ret['instances']

    for instance in instances:
        id = instance['id']
        tags = instance['tags']
        type = instance['type']
        owner = '<<NoOwner>>'
        name = '<<NoName>>'

        for tag in tags:
            k, v = tag['Key'], tag['Value']
            if k=='Owner':
                owner = v
                continue
            if k=='Name':
                name = v
                continue

        #line = '- {:02d} [{:}] {:} {:}「{:}」({:})'.format(
        line = '| {:02d} | {:} | {:} | {:} | {:}({:})'.format(
            cur_count, region_description, type, owner, name, id
        )
        outlines.append(line)

        cur_count += 1

nowstr = '# {:}'.format(now())
outlines.insert(0, nowstr)
outlines.insert(1, target_regions_displaystr(regions))
outlines.insert(2, '')
outlines.insert(3, '| Number | Region | Type | Owner | Note |')
outlines.insert(4, '| ------ | ------ | ---- | ----- | ---- |')

list2file('running_instances.md', outlines)
```

## サンプル - tag editor

```python
# coding: utf-8

from copy import deepcopy
import datetime
import os

import boto3

ACCESS_KEY  = os.environ['AWS_ACCESS_KEY']
SECRET_KEY  = os.environ['AWS_SECRET_KEY']
USE_SSL     = False
REGION_NAME = None

regionname_tokyo = 'ap-northeast-1'
regionname_singa = 'ap-southeast-1'

def get_ec2_client_obj():
    client = boto3.client(
        'ec2',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION_NAME,
        verify=USE_SSL
    )
    return client

def set_tag(target_ids, tag_key, tag_value):
    """ @param target_ids A list of id string. """
    client = get_ec2_client_obj()

    use_dryrun = False
    tags = [
        {
            'Key' : tag_key,
            'Value': tag_value,
        },
    ]

    # 空値をセットする機会はないと思うので
    # タグの delete に充てることにした.
    if tag_value == None:
        tags = [{'Key' : tag_key}]
        response = client.delete_tags(DryRun=use_dryrun, Resources=target_ids, Tags=tags)
        return response

    response = client.create_tags(DryRun=use_dryrun, Resources=target_ids, Tags=tags)
    return response

def describe_tag(target_id):
    """ @param target_id A string. """
    client = get_ec2_client_obj()

    use_dryrun = False
    filter = [
        {
            'Name'  : 'resource-id',
            'Values' : [target_id],
        },
    ]

    result = client.describe_tags(DryRun=use_dryrun, Filters=filter)
    tags = result['Tags']
    return tags

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def printable_tags(tags_of_describe_tag):
    s = ''
    for i,tag in enumerate(tags_of_describe_tag):
        k, v = tag['Key'], tag['Value']
        #resource_id, resource_type = tag['ResourceId'], tag['ResourceType']
        printable_kv = '{:}={:}'.format(k, v)
        if i==0:
            s = printable_kv
            continue
        s = '{:},{:}'.format(s, printable_kv)
    return s

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='',
    )
    parser.add_argument('-i', '--input', default=None, required=True,
        help='A filepath which contains resource id with 1-id 1-line.')
    parser.add_argument('--tokyo', default=False, action='store_true')
    parser.add_argument('--singa', default=False, action='store_true')

    parser.add_argument('-l', '--list', default=False, action='store_true',
        help='If given, not settings given tag but showing current tags.')

    parser.add_argument('-s', '--set', default=False, action='store_true',
        help='If given, setting given key-value to given resources. Need -k option.')

    parser.add_argument('-k', '--key', default=None,
        help='A key you want to set.')
    parser.add_argument('-v', '--value', default=None,
        help='A value you want to set. If ommited, not setting but delete this tag.')

    parsed_args = parser.parse_args()
    return parsed_args

args = parse_arguments()
if args.tokyo:
    REGION_NAME = regionname_tokyo
if args.singa:
    REGION_NAME = regionname_singa

target_ids = file2list(args.input)

if args.list:
    total_count = len(target_ids)
    print('Total {:} resources.'.format(total_count))
    for i,target_id in enumerate(target_ids):
        print('{:}/{:} {:}...'.format(i+1, total_count, target_id), end='')
        tags = describe_tag(target_id)
        print(' {:}'.format(printable_tags(tags)))
    exit(0)

if args.key == None:
    raise RuntimeError('No tag key given.')
response = set_tag(target_ids, args.key, args.value)
print(response)
```
