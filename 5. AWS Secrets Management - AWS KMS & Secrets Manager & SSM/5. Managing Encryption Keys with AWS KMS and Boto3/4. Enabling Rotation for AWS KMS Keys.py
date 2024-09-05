"""
 assert your understanding of enabling key rotation using AWS KMS with Python Boto3.
 The starter script creates a KMS key and provides a key ID that you can interact with,
 but it does not enable key rotation. Your task is to expand the interface and add
 a command line to enable key rotation on the provided key, then verify that rotation
 has been enabled by describing the key and printing the KeyRotationEnabled attribute.
 Run the script and view the result of your added feature.
"""

import boto3

# Initialize KMS client
kms = boto3.client('kms')

# Creating a KMS key
kms_response = kms.create_key(
    Description='Sample KMS key for Course',
    KeyUsage='ENCRYPT_DECRYPT',
    Origin='AWS_KMS'
)

# Extract Key Id
key_id = kms_response['KeyMetadata']['KeyId']

# TODO: Enable key rotation for the created KMS key
kms.enable_key_rotation(KeyId=key_id)
# TODO: Verify the key rotation by describing the key and printing the 'KeyRotationEnabled' attribute
rotation_status = kms.get_key_rotation_status(KeyId=key_id)
is_rotation_enabled = rotation_status['KeyRotationEnabled']
print(f"Key Rotation Enabled: {is_rotation_enabled}")
