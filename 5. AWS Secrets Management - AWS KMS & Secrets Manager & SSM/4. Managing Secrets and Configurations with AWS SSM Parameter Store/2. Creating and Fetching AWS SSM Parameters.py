"""
modify the provided Python script to retrieve and print the values of the /app_config/api_url
and /app_config/api_key parameters using the get_parameter method. Be sure to utilize the
WithDecryption parameter correctly when fetching these values.
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

# Create an encrypted parameter for application's API key
ssm.put_parameter(
    Name='/app_config/api_key',
    Value='my_encrypted_api_key',
    Type='SecureString',
)

# Retrieve the plain text parameter for the API URL
api_url = ssm.get_parameter(
    Name='/app_config/api_url',
    WithDecryption=False  # No decryption needed for plain text
)

# Retrieve the encrypted parameter for the API key
api_key = ssm.get_parameter(
    Name='/app_config/api_key',
    WithDecryption=True  # Decrypt the SecureString parameter
)

# Print the parameter values
print("API URL:", api_url['Parameter']['Value'])
print("API Key:", api_key['Parameter']['Value'])