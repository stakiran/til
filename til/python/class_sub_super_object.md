# Python でスーパークラスやらサブクラスやら

- スーパークラス
    - 実装してほしい部分は NotImplementedError などで知らせてやる
- サブクラス
    - class 時にスーパーを指定
    - ctor から super().__init__() で super ctor を呼び出し

```
class Formatter():
    def __init__(self, lines, outpath):
        self._lines = lines
        self._outpath = outpath

    def build(self):
        self._construct_header()
        self._construct_lines()

    def output_to_file(self):
        raise NotImplementedError()

    def _construct_header(self):
        raise NotImplementedError

    def _construct_lines(self):
        raise NotImplementedError

class CsvFormatter(Formatter):
    def __init__(self, lines, outpath):
        super().__init__(lines, outpath)

    def output_to_file(self):
        ...

    def _construct_header(self):
        ...
