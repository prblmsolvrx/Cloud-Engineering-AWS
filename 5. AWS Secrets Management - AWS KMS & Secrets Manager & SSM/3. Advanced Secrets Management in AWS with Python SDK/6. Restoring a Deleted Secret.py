"""
can accidentally delete secrets he still needs. Luckily, deleted secrets are not immediately
removed and can be restored within a certain time period. Faced with such a situation, your
task is to help Cosmo out by completing a Python script that restores a secret that was just deleted.
"""

import boto3
import time

# Initialize the boto3 Secrets Manager client
sm = boto3.client('secretsmanager')

# Create a new secret
response = sm.create_secret(Name='CosmosSecret', SecretString='mysecret')

# Delete the secret
sm.delete_secret(SecretId='CosmosSecret', RecoveryWindowInDays=7)

# TO DO: Restore the deleted secret
time.sleep(5)
response = sm.restore_secret(SecretId='CosmosSecret')
print(f"Secret restored: {response}")