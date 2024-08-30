"""
write a Python script from scratch. This script should create resources
and clients for SQS and SNS. In the first part, these will be default
resources and clients. In the second part, you need to set up an AWS
session with specified region and credentials, and create an SQS
resource and an SNS client based on this session. While setting up
credentials, use 'test' for both aws_access_key_id and aws_secret_access_key,
and 'us-west-2' for region_name.
Important Note: Running scripts can modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset button located in 
the top right corner. However, keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3

# TODO: Create a default AWS SQS resource
default_sqs_resource = boto3.resource('sqs')
# TODO: Create a default AWS SNS client
default_sns_client = boto3.client('sns')
# TODO: Set up an AWS Session with specified region and credentials.
# Use 'test' for AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and 'us-west-2' for the AWS region.
session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)

# TODO: Based on this session, create an SQS resource.
default_sqs_resource = session.resource('sqs')
print(default_sqs_resource)
# TODO: Based on this session, create an SNS client.
default_sqs_client = session.client('sns')
print(default_sqs_client)