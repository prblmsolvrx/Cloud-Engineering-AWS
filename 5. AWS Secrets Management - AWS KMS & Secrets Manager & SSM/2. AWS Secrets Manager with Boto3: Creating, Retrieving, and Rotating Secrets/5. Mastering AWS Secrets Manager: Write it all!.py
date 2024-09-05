"""
write a complete Python script that creates, retrieves, updates (rotates),
retrieves the updated secret, and finally retrieves the previous version of
the secret. The goal of this task is to provide hands-on experience with
the concepts you've learned so far in this lesson.
"""

import boto3

# Initialize a boto3 client for Secrets Manager
client = boto3.client("secretsmanager")

# Create a secret named TestSecret with a username and password
response_create = client.create_secret(
    Name="TestSecret",
    SecretString='{"username": "test", "password": "password"}'
)
print("Secret Created: ", response_create['Name'])

# Retrieve the created secret using its SecretId
response_get = client.get_secret_value(SecretId="TestSecret")
print("Secret Retrieved: ", response_get['SecretString'])

# Rotate the secret by updating it with new password
response_rotate = client.update_secret(
    SecretId="TestSecret",
    SecretString='{"username": "test", "password": "newpassword"}'
)
print("Secret Rotated/Updated")

# Retrieve the updated/rotated secret again
response_get_updated = client.get_secret_value(SecretId="TestSecret")
print("Updated Secret Retrieved: ", response_get_updated['SecretString'])

# Describe the secret and print its versions
response_version = client.describe_secret(SecretId="TestSecret")
if 'VersionIdsToStages' in response_version:
    print("Version IDs and Stages: ", response_version['VersionIdsToStages'])

# Retrieve the previous version of the secret using the AWSPREVIOUS stage
for version_id, stages in response_version['VersionIdsToStages'].items():
    if 'AWSPREVIOUS' in stages:
        response_get_previous = client.get_secret_value(
            SecretId="TestSecret", VersionId=version_id
        )
        print("Previous Version Retrieved: ", response_get_previous['SecretString'])
