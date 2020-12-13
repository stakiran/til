# TSLint

## Q: VSCode で tslint がないせいでデバッグ実行できない（ブロッキング）するんだが……
VSCode を再起動してください。

参考:  https://github.com/tritask/tritask-vscode/issues/11

## TSLint から ESLint に移行する
TSLint 消して、ESLint 入れればいいだけ。

参考:

- [typescript-eslint/README.md at master · typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/blob/master/docs/getting-started/linting/README.md)
    - 手順が一番詳しい
- [脱TSLintして、ESLint TypeScript Plugin に移行する - Qiita https://qiita.com/suzuki_sh/items/fe9b60c4f9e1dbc5d903]
    - ESLint 使うかの背景に詳しい
        - TSLint は活動活発じゃなかった
        - ESLint という流行ってるモンがあるんだから、乗っかればええやん
        - ってことで typescript-eslint としてやっていくことに
- [Migrate from TSLint to ESLint | Visual Studio Code Extension API https://code.visualstudio.com/api/advanced-topics/tslint-eslint-migration]
