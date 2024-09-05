"""
update this password using AWS Secret Manager.
Initially, you are given a script that creates a secret with a basic password.
You need to modify the script to update the password with an auto-generated one.
"""

import boto3

# Initialize the boto3 Secrets Manager client
sm = boto3.client('secretsmanager')

# Create a new secret with a simple password
response = sm.create_secret(Name='CosmoSecret', SecretString='simplePassword')

# TODO: Generate a new highly secure password
highly_secure_password = sm.get_random_password(PasswordLength=16)['RandomPassword']
# TODO: Update the secret with the new password
update_secret_v1 = sm.update_secret(SecretId='CosmoSecret', SecretString=highly_secure_password)