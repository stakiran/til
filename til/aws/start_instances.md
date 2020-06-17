# start intances

## instance-ids に指定したインスタンスが存在しないとき
以下が出る。

> An error occurred (InvalidInstanceID.Malformed) when calling the StartInstances operation: Invalid id: "i-01265b7abcdefghij"

その際、存在するインスタンスの指定有無に関わらず **コマンドそのものが実行に失敗する**。

つまり instance-ids に指定する id は全部存在するものでなくてはならない（実行が通らない）。
