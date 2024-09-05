"""
authenticate with AWS using custom credentials. The task presents you with a Python
script that already creates a custom session. Your task is to complete the script
by creating custom clients for AWS Secrets Manager, SSM, and KMS using the already
established custom session. This will help you understand how to create custom clients
using a custom session, which is important for needing custom configurations,
such as when interacting with resources in a different AWS region.
"""

import boto3

# Create custom session
my_session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)

# TODO: Create Secrets Manager client based on this session
secret_manager_default = my_session.client('secretsmanager')
print("Default Secrets Manager client initialized.")

# TODO: Create Parameter Store (SSM) client based on this session
ssm_default = my_session.client('ssm')
print("Default Parameter Store (SSM) client initialized.")

# TODO: Create KMS client based on this session
kms_default = my_session.client('kms')
print("Default KMS client initialized.")