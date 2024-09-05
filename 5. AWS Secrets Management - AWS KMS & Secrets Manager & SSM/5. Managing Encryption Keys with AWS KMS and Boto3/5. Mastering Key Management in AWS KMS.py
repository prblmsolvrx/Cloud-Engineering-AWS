"""
 write an entire Python script from scratch. The script needs to create an AWS KMS key,
 generate a data key, encrypt some sample data locally, describe the key created,
 list all keys, enable key rotation for the AWS KMS key, and finally, schedule the
 AWS KMS key for deletion. Run the script and observe the flow of the process to
 reinforce your understanding of AWS KMS.
"""

# TODO: Prepare an entire script that does the following:
# Create an AWS KMS key
# Generate a data key
# Encrypt some data
# Describe the key
# List all Keys
# Enable key rotation for the AWS KMS key
# Schedule the AWS KMS key for deletion

import boto3

# Initialize the KMS client
kms = boto3.client('kms')

# 1. Create an AWS KMS key
kms_key_response = kms.create_key(
    Description='Sample KMS Key for Course',
    KeyUsage='ENCRYPT_DECRYPT',
    Origin='AWS_KMS'
)

# Extract the Key ID before using it in any operations
key_id = kms_key_response['KeyMetadata']['KeyId']
print(f"KMS Key created with ID: {key_id}")

# 2. Describe the KMS key
key_description = kms.describe_key(KeyId=key_id)
print("Key Description:", key_description)

# 3. Generate a data key
data_key_response = kms.generate_data_key(
    KeyId=key_id,
    KeySpec='AES_256'
)

# Extract the plaintext and encrypted data key
plaintext_data_key = data_key_response['Plaintext']
encrypted_data_key = data_key_response['CiphertextBlob']

print("Generated Data Key (Plaintext):", plaintext_data_key)
print("Generated Data Key (Encrypted):", encrypted_data_key)

# 4. Encrypt some data using the KMS key
encrypt_response = kms.encrypt(
    KeyId=key_id,
    Plaintext=b'Hello, AWS!'
)
ciphertext = encrypt_response['CiphertextBlob']
print("Encrypted Ciphertext:", ciphertext)

# 5. Decrypt the ciphertext
decrypt_response = kms.decrypt(
    KeyId=key_id,
    CiphertextBlob=ciphertext
)
plaintext = decrypt_response['Plaintext'].decode('utf-8')
print("Decrypted Plaintext:", plaintext)

# 6. List all KMS keys
keys_list = kms.list_keys()
print("List of KMS Keys:")
for key in keys_list['Keys']:
    print(f"Key ID: {key['KeyId']}")

# 7. Enable key rotation for the AWS KMS key
kms.enable_key_rotation(KeyId=key_id)
print("Key rotation enabled for the KMS Key.")

# 8. Check key rotation status
rotation_status = kms.get_key_rotation_status(KeyId=key_id)
is_rotation_enabled = rotation_status['KeyRotationEnabled']
print(f"Key Rotation Enabled: {is_rotation_enabled}")

# 9. Schedule the AWS KMS key for deletion
delete_response = kms.schedule_key_deletion(
    KeyId=key_id,
    PendingWindowInDays=7
)
print(f"Key scheduled for deletion with a waiting period of {delete_response['PendingWindowInDays']} days.")
