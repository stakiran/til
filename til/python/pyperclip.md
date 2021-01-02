# pyperclip

```
pip install pyperclip
```

- copy() と paste() だけだから楽

```py
s = '''# markdoen
- list
- list
- list
'''

pyperclip.copy(s)

s = pyperclip.paste()

print(s)
```

