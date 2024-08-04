"""
In this task, you will familiarize yourself with creating AWS sessions
and working with Amazon S3. Using the Python SDK, Boto3, you'll
explore how easy it is to set up an AWS session with specific
credentials and a region. Once this session is established,
it can be used to initialize S3 resource and client.
Your task here is to closely review these interactions
without making any code modifications. Once you feel
comfortable with the structure of the script, run it
to observe the process and understand how Amazon S3
and Boto3 play together.

Important Note: Running scripts can modify the
resources in our AWS simulator. If you need to
revert to the initial state, you can use the
reset button located in the top right corner.
However, keep in mind that resetting will erase
any code changes. To preserve your code during a
reset, consider copying it to your clipboard.
"""

import boto3

# Create an AWS session with explicit credentials and region
session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)

# Create an S3 resource based on the session
s3_resource = session.resource('s3')

# Print S3 resource details
print("S3 resource: ", s3_resource)

# Create an S3 client based on the session
s3_client = session.client('s3')

# Print S3 client details
print("S3 client: ", s3_client)

# Create a default S3 resource with the default session
# The default session uses credentials and settings from environment variables,
# AWS credentials and config file, or IAM role for Amazon EC2 instances
default_s3_resource = boto3.resource('s3')

# Print default S3 resource details
print("Default S3 resource: ", default_s3_resource)

# Create a default S3 client with the default session
default_s3_client = boto3.client('s3')

# Print default S3 client details
print("Default S3 client: ", default_s3_client)