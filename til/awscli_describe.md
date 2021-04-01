# AWSCLI describe 系
- query で欲しい属性だけ並べ直すのが良い

## EC2

```
aws ec2 describe-instances --query "Reservations[*].Instances[*].{instance_id:InstanceId,instance_type:InstanceType,tag_name:Tags[?Key==`Name`]}" --output json
```

## RDS

```
aws rds describe-db-instances --query "DBInstances[*].{db_instance_idenfier:DBInstanceIdentifier,db_instance_class:DBInstanceClass,allocated_storage_size:AllocatedStorage}" --output json
```

## AutoScalingGroup

```
aws autoscaling describe-auto-scaling-groups --query "AutoScalingGroups[*].{asg_name:AutoScalingGroupName,launch_configulation_name:LaunchConfigurationName}" --output json

aws autoscaling describe-launch-configurations --query "LaunchConfigurations[*].{launch_configulation_name:LaunchConfigurationName,instance_type:InstanceType}" --output json
```
