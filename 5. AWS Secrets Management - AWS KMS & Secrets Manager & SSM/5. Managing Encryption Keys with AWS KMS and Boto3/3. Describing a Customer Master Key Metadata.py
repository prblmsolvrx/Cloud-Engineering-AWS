"""
enhance an existing Python script by incorporating a feature that fetches metadata of an AWS KMS Key.
The provided script creates a KMS key, generates a data key, and stores the key_id. Now, you are
required to add functionality to describe the created KMS key using the describe_key operation
and print its KeyState. Carefully observe how the data flows and the output to strengthen your
grasp on AWS KMS operations.
Hint: The KeyState is nested inside KeyMetadata in the response from the describe_key operation.
"""

import boto3

# Initialize KMS client
kms = boto3.client('kms')

# Creating a KMS key
cmk_response = kms.create_key(
    Description='Sample KMS Key for Course',
    KeyUsage='ENCRYPT_DECRYPT',
    Origin='AWS_KMS'
)

# Extract Key Id
key_id = cmk_response['KeyMetadata']['KeyId']

# Generate data key
data_key_response = kms.generate_data_key(
    KeyId=key_id,
    KeySpec='AES_256'
)

# TODO: Use describe_key to fetch metadata, extract 'KeyState' from 'KeyMetadata', and print it
key_description = kms.describe_key(KeyId=key_id)
key_id = key_description['KeyMetadata']['KeyState']

print(key_id)