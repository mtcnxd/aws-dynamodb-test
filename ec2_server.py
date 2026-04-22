import boto3
from config import *

ec2 = boto3.client(
    'ec2', 
    region_name='us-east-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

try:
    response = ec2.start_instances(InstanceIds=[aws_instance_id])

    ec2.stop_instances(InstanceIds=[aws_instance_id])

    print("Instancia iniciada correctamente")

except Exception as e:
    print(e)
