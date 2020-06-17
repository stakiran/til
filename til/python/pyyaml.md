# PyYAML
pip install pyyaml した後、

```
import yaml

def file2str(filepath):
    ret = ''
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = f.read()
    return ret

def yamlfile2dict(filepath):
    content = file2str(filepath)
    d = yaml.safe_load(content)
    return d
```
