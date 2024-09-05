"""
implement a script from scratch that interacts with the AWS Systems Manager Parameter Store.
This exercise will require you to apply all the concepts you've learned thus far to create,
read, update, tag, and delete parameters, as well as work with parameter hierarchies.
Go ahead, emit your knowledge vibe, and write your script!
"""

import boto3

# TODO: Initialize a boto3 SSM client
ssm_client = boto3.client('ssm')

# TODO: Create parameters for application's API URL and API key
def create_parameters():
    # Create API URL parameter
    ssm_client.put_parameter(
        Name='/app_config/api_url',
        Value='https://api.example.com',
        Type='String',
        Overwrite=True
    )
    
    # Create API Key parameter
    ssm_client.put_parameter(
        Name='/app_config/api_key',
        Value='your-api-key',
        Type='SecureString',
        Overwrite=True
    )
    
# TODO: Update the API URL parameter
def update_api_url(new_url):
    ssm_client.put_parameter(
        Name='/app_config/api_url',
        Value=new_url,
        Type='String',
        Overwrite=True
    )
    
# TODO: Read and print the API URL parameter
def get_api_url():
    response = ssm_client.get_parameter(Name='/app_config/api_url')
    print(f"API URL: {response['Parameter']['Value']}")

# TODO: Tag the API key parameter
def tag_api_key():
    ssm_client.add_tags_to_resource(
        ResourceType='Parameter',
        ResourceId='/app_config/api_key',
        Tags=[
            {'Key': 'Environment', 'Value': 'Production'},
            {'Key': 'Project', 'Value': 'MyApp'}
        ]
    )

# TODO: Create a parameter hierarchy for application's database config
def create_database_parameters():
    # Database host parameter
    ssm_client.put_parameter(
        Name='/app_config/database/host',
        Value='db.example.com',
        Type='String',
        Overwrite=True
    )
    
    # Database port parameter
    ssm_client.put_parameter(
        Name='/app_config/database/port',
        Value='5432',
        Type='String',
        Overwrite=True
    )
    
    # Database name parameter
    ssm_client.put_parameter(
        Name='/app_config/database/name',
        Value='mydatabase',
        Type='String',
        Overwrite=True
    )
    
# TODO: List all parameters in '/app_config/database' hierarchy
def list_database_parameters():
    response = ssm_client.get_parameters_by_path(
        Path='/app_config/database',
        Recursive=True
    )
    for param in response['Parameters']:
        print(f"Parameter: {param['Name']}, Value: {param['Value']}")
        
# TODO: Delete the API URL parameter and the parameters in the database hierarchy
def delete_parameters():
    # Delete API URL parameter
    ssm_client.delete_parameter(Name='/app_config/api_url')
    
    # Delete parameters in the database hierarchy
    response = ssm_client.get_parameters_by_path(
        Path='/app_config/database',
        Recursive=True
    )
    for param in response['Parameters']:
        ssm_client.delete_parameter(Name=param['Name'])