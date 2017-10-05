import boto3
from pprint import pprint

s3 = boto3.resource('s3')
pprint(s3.buckets.all())

# error
# pprint(s3.buckets.all()[0])

print('S3 Buckets')
for bucket in s3.buckets.all():
    pprint(bucket)

ec2 = boto3.resource('ec2')

print('\nEC2 Instances:')
for ins in ec2.instances.all():
    pprint(ins)

print('\nEC2 Instances (id, state)')
for ins in ec2.instances.all():
    print(ins.id, ins.state)

