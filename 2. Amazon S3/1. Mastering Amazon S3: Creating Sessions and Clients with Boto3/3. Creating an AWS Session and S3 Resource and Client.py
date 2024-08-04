"""
In this task, you will gain familiarity with establishing an AWS
session and creating S3 resources and clients.
This understanding will help set the foundation
for further AWS-related tasks.

This task entails:

Creating an AWS session with specific, provided credentials.
Utilizing the session to create an S3 resource and client.
To achieve these tasks, fill in the TODO sections in the starting code.

Important Note: Running scripts can alter the filesystem's state
or modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset
button located in the top right corner. However,
keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3

# TODO: Replace with your features
# Step 1: Create an AWS session. Use the following explicit credentials: Access key: "test", Secret access key: "test", and the AWS region: "us-west-2".
session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)

# Step 2: Once the session is created, use this session to create an S3 resource and assign it to the s3_resource variable. 
s3_resource = session.resource('s3')

# Step 3: Similarly, create an S3 client using the session established and assign it to the s3_client variable. Use the principles and functions you've learned so far to accomplish these tasks. Good luck!
s3_client = session.client('s3')
