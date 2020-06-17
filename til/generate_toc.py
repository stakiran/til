# encoding: utf-8

import glob
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

def get_directory(path):
    return os.path.dirname(path)

def get_filename(path):
    return os.path.basename(path)

def get_basename(path):
    return os.path.splitext(get_filename(path))[0]

def get_extension(path):
    return os.path.splitext(get_filename(path))[1]

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)

lines_header = file2list('template_header.md')
lines_footer = file2list('template_footer.md')

# glob でディレクトリ全探索
searchee_dir = os.path.join(MYDIR)
query = '{}/**/*.md'.format(searchee_dir)
searchee_files = glob.glob(query, recursive=True)

# 目次化したくないファイルは個別に除外
excludes = [
    'til\\readme.md',
    'til\\template_header.md',
    'til\\template_footer.md',
]
targetpaths = []
for filepath in searchee_files:
    should_skip = False
    for excluder in excludes:
        if filepath.endswith(excluder):
            should_skip = True
            break
    if should_skip:
        continue
    targetpaths.append(filepath)

# 目次つくる
lines_toc = []
for filepath in targetpaths:
    cur_fullpath = filepath
    cur_filename = get_filename(cur_fullpath)
    cur_related_path = cur_fullpath.replace(MYDIR, '')[1:]
    cur_related_path = cur_related_path.replace('\\', '/')

    cur_contents_lines = file2list(cur_fullpath)
    cur_firstline = cur_contents_lines[0]
    cur_title_in_section = cur_firstline[2:]

    cur_linecount = len(cur_contents_lines)

    # \xxx\yyy\hoge.md
    #              ^^^ remove
    cur_related_path_without_ext = cur_related_path[:-3]
 
    linkstr = '- [{} {}]({}) ({}L)'.format(
        cur_related_path_without_ext,
        cur_title_in_section,
        cur_related_path,
        cur_linecount
    )
    lines_toc.append(linkstr)
# 空行区切り追加
# Q: なぜ template_footer.md 側で空行を入れない？
#    ->Ans: template 側で空行やらなんやら考慮するの好みじゃないから.
lines_toc.append('')

# つくったのでヘッダーフッターとともに組み立てる
lines_for_output = []
lines_for_output.extend(lines_header)
lines_for_output.extend(lines_toc)
lines_for_output.extend(lines_footer)

# ファイル化
list2file('readme.md', lines_for_output)
