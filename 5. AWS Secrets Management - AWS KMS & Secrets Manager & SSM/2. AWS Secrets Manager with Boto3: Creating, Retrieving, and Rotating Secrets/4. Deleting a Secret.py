"""
 ensure that the details of the special event remain a secret.
 Your mission is to complete the provided script by adding
 the necessary logic to delete the "PartyDetails" secret from
 the AWS Secrets Manager.
"""

import json
import boto3

# Initialize the Secrets Manager client
client = boto3.client("secretsmanager")

# Create the secret for the party
response_create = client.create_secret(
    Name="PartyDetails",
    SecretString='{"venue":"CodeSignal","date":"Now", "time":"19:00"}'
)
print("Secret Created: ", response_create['Name'])

# TODO: Delete the secret
response_delete =  client.delete_secret(
    SecretId="PartyDetails",
    # Set this to True to immediately delete the secret without a recovery window.
    ForceDeleteWithoutRecovery=True
    # Alternatively, you can specify RecoveryWindowInDays for a soft delete with a recovery period.
    # RecoveryWindowInDays=7
)

print("Secret Deleted: ", response_delete['Name'])
