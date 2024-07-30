import boto3

# TODO: Create an S3 client with a custom configuration with endpoint_url set to http://localhost:4566
client = boto3.client('s3',endpoint_url='http://localhost:4566')

"""
Your task is to configure a Boto3 client for S3 with a custom configuration,
specifically setting the endpoint_url to http://localhost:4566.
This setup is common when working with local cloud simulators that mimic
AWS services, allowing you to develop and test without impacting real AWS resources.
"""