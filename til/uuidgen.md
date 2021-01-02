# UUID uuidgen
linux:

```
$ uuidgen
```

windows:

- git for windows 同梱の sed 使用
    - uuidgen は同梱されてないので powershell で

```
$ powershell -Command "[Guid]::NewGuid()" | sed -n "4p"
```

