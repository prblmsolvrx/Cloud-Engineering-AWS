"""
a Python script, which creates a string parameter /app_config/api_url and initially assigns
it a value. However, this URL has recently changed, and you are tasked with updating the
script to reflect this change. Your specific task is to update the URL to https://api.newapp.com
without removing the original code that sets the initial value. After updating the parameter,
validate your changes by retrieving and printing the updated value.
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

# TODO: Update the '/app_config/api_url' parameter to 'https://api.newapp.com'
ssm.put_parameter(
    Name='/app_config/api_url',
    Value='https://api.newapp.com',
    Type='String',
    Overwrite=True  # Overwrite the existing parameter
)
# TODO: Fetch and print the updated API URL parameter value
response = ssm.get_parameter(Name='/app_config/api_url')
updated_value = response['Parameter']['Value']

print(f"Updated API URL: {updated_value}")
