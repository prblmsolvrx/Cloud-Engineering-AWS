"""
a Python script is provided that creates several parameters using the AWS SSM Parameter Store.
Your task is to extend this script by adding a few lines of code that will remove these parameters.
Specifically, you are required to delete the /app_config/api_url parameter individually and the
parameters under the /app_config/database/ hierarchy in a batch. This task will give you a broader
understanding of managing parameters using the AWS SSM Parameter Store.
"""

import boto3

# Initialize the boto3 SSM client
ssm = boto3.client('ssm')

# Create a plain text parameter for application's API URL
ssm.put_parameter(
    Name='/app_config/api_url',
    Value='https://api.myapp.com',
    Type='String',
)

# Create a parameter hierarchy for application's database config
ssm.put_parameter(
    Name='/app_config/database/host',
    Value='db.myapp.com',
    Type='String',
)

ssm.put_parameter(
    Name='/app_config/database/user',
    Value='mydbuser',
    Type='String',
)

ssm.put_parameter(
    Name='/app_config/database/password',
    Value='mydbpassword',
    Type='SecureString',
)

# TODO: Delete '/app_config/api_url' parameter individually 
# TODO: Delete parameters in a '/app_config/database' hierarchy in a batch

# Delete '/app_config/api_url' parameter
ssm.delete_parameter(
    Name='/app_config/api_url'
)
# Delete parameters in the '/app_config/database' hierarchy in a batch
ssm.delete_parameters(
    Names=[
        '/app_config/database/host',
        '/app_config/database/user',
        '/app_config/database/password'
    ]
)
