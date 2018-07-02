import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2', region_name='ap-northeast-1')
    response = client.stop_instances(
        InstanceIds=[
            # Host A
            'i-XXXXXXXXX',
            # Host B
            'i-XXXXXXXXX',
            # Host C
            'i-XXXXXXXXX',
        ]
    )
    print(response)

