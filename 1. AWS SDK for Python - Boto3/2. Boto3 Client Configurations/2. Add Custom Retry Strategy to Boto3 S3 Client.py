import boto3
from botocore.config import Config

# TO DO: Setup a boto3 S3 client with a custom retry strategy: set 'max_attempts' to 5 and 'mode' to 'standard'
config_with_retry = Config(
    retries={
        'max_attempts' : 5,
        'mode': 'standard'
    }
)
s3 = boto3.client('s3',config = config_with_retry)

# Retrieve the list of S3 buckets
response = s3.list_buckets()
print(response['Buckets'])