# Terraform で常に changes が出る件 about ecs_task_definition
- https://stackoverflow.com/questions/67064074/terraform-keeps-forcing-new-resource-force-replacement-for-container-definition
    - aws provider のバグ
    - 「terraform planに表示されているデフォルト値をすべてnullまたは空の設定セットで埋める必要があります」

## 過去遭遇したもの
- 同じ名前の環境変数を 2 つ定義していた
- aws_ecs_task_definition.volume.efs_volume_configuration.root_directory の値を `""` にしていた
    - 内部的には `"/"` に変換されるっぽいので、常に `"/" → ""` の change が発生したとみなされてしまう

