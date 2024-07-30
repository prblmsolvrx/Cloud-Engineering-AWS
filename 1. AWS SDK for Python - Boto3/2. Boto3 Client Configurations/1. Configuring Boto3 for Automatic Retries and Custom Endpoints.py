import boto3
from botocore.config import Config

custom_config = Config(retries={'max_attempts': 3, 'mode': 'standard'})
s3_client = boto3.client('s3', endpoint_url='https://my-test-bucket.com', config=custom_config)

"""
Did you know you can configure a Boto3 client to automatically retry failed requests?
This feature is incredibly helpful when dealing with network issues or service limits.
The provided code creates an Amazon S3 client configured with a custom endpoint and a retry strategy.
It is set to try up to 3 times if a request fails. 
"""