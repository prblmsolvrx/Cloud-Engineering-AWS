"""
 a Python script that interacts with AWS Systems Manager (SSM).
 The script is supposed to create a single parameter for an
 application’s database configuration and tag it appropriately.
 Your objective is to complete this script by adding a code to
 tag this parameter with {'Key': 'owner', 'Value': 'Cosmo'}.
"""

import boto3

# Initialize the boto3 SSM client
ssm = boto3.client('ssm')

# Create a parameter for an application's database config
ssm.put_parameter(
    Name='/app_config/database/host',
    Value='db.myapp.com',
    Type='String',
    Overwrite=True  # Overwrite the existing parameter
)

# TODO: Add a line of code to tag the '/app_config/database/host' parameter

# Tag the '/app_config/database/host' parameter
ssm.add_tags_to_resource(
    ResourceType='Parameter',
    ResourceId='/app_config/database/host',
    Tags=[
        {
            'Key': 'owner',
            'Value': 'Cosmo'
        }
    ]
)
