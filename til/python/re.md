# Python re regular expression 正規表現

## 文字列をマスクする

```python
# def masking_char(s):
    masking_char = 'X'
    masked_str = re.sub(r'[a-zA-Z0-9]', 'X', s)
    newstr = masked_str
    return newstr
```
