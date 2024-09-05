"""
a Python script to initialize default clients for AWS Secrets Manager,
Parameter Store (SSM), and Key Management System (KMS).
Then, create a custom boto3 session and initialize custom clients
for these three AWS services using the session.
Ensure you are creating the session with 'test'
as both aws_access_key_id and aws_secret_access_key,
and 'us-west-2' as the region_name. In this task, you will
showcase your understanding of creating both default and custom
clients for managing secrets on AWS.
"""

import boto3

# TODO: Create default Secrets Manager client
default_Secrets_Manager = boto3.client('secretsmanager')
# TODO: Create default Parameter Store (SSM) client
default_SSM = boto3.client('ssm')
# TODO: Create default KMS client
kms_default = boto3.client('kms')
# TODO: Create custom session
my_session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)
# TODO: Create Secrets Manager client based on this session
secrets_manager_custom = my_session.client('secretsmanager')
# TODO: Create Parameter Store (SSM) client based on this session
ssm_custom = my_session.client('ssm')
# TODO: Create KMS client based on this session
kms_custom = my_session.client('kms')