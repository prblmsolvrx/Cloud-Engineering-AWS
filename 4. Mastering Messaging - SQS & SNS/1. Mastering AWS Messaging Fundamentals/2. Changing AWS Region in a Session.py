"""
 modify an executing Python script. The script creates a specific AWS session with a
 custom access key, secret key, and region. However, the region is set to us-west-1.
 Your task is to change the provisioned region from us-west-1 to us-east-1.
 Run the modified script and observe how altering the session's region properties
 influences AWS resource and client creation.
Important Note: Running scripts can modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset button located
in the top right corner. However, keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3

# TODO: Change the AWS region from 'us-west-1' to 'us-east-1'
# Create AWS session with specified region and credentials
session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

print("Current AWS Session region:", session.region_name)

# Create SQS resource based on this session
sqs_from_session = session.resource('sqs')
print("Current SQS resource region:", sqs_from_session.meta.client.meta.region_name)

# Create SNS client based on this session
sns_from_session = session.client('sns')
print("Current SNS client region:", sns_from_session.meta.region_name)