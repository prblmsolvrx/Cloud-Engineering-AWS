"""
an initial Python script that creates a secret and then updates it twice, your task is to retrieve and print
2 latest version IDs of the secret.
Then, specifically target and print the value of the secret marked with the AWSPREVIOUS staging label.
AWS Secrets Manager uses staging labels to help you manage different versions of a secret.
The AWSCURRENT label always points to the current version of the secret, while AWSPREVIOUS
points to the version before the current one. This feature is particularly useful for rolling
back changes or maintaining an understanding of a secret's history.
"""

import boto3

# Initialize the boto3 Secrets Manager client
sm = boto3.client('secretsmanager')

# Create a new secret
response = sm.create_secret(Name='CosmosSecret', SecretString='secret1')

# Update the secret twice
sm.update_secret(SecretId='CosmosSecret', SecretString='secret2')
sm.update_secret(SecretId='CosmosSecret', SecretString='secret3')

# TO DO: List and print 2 latest version IDs of the secret
# TO DO: Retrieve and print the value of the version of the secret labeled as AWSPREVIOUS

# List and print 2 latest version IDs of the secret
list_response = sm.list_secret_version_ids(SecretId='CosmosSecret')

# Extract and print the two latest version IDs
versions = list_response['Versions']
latest_versions = sorted(versions, key=lambda x: x['CreatedDate'], reverse=True)[:2]
for version in latest_versions:
    print(f"Version ID: {version['VersionId']}")

# Retrieve and print the value of the version labeled as AWSPREVIOUS
previous_version = sm.get_secret_value(SecretId='CosmosSecret', VersionStage='AWSPREVIOUS')
print(f"AWSPREVIOUS Version Value: {previous_version['SecretString']}")