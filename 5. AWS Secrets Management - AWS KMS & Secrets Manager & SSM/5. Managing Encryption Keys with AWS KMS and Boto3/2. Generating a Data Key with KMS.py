"""
 you'll extend the functionality of a Python script for generating a data key in AWS KMS.
 The provided script initiates a boto3 client for KMS, creates an AWS KMS key, and extracts
 the key_id from the KMS key response. Your task is to complete the script by adding functionality
 to generate a data key using the generate_data_key method. Run your updated script and observe the response.
"""

import boto3

# Initialize KMS client
kms = boto3.client('kms')

# Creating an AWS KMS key
kms_key_response = kms.create_key(
    Description='Sample KMS Key for Course',
    KeyUsage='ENCRYPT_DECRYPT',
    Origin='AWS_KMS'
)

# Extract Key Id
key_id = kms_key_response['KeyMetadata']['KeyId']

# TODO: Generate a data key
data_key_response = kms.generate_data_key(
    KeyId=key_id,
    KeySpec='AES_256'
)