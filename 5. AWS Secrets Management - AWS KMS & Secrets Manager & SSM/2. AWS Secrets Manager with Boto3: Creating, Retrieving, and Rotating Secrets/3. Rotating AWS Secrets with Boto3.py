"""
update the secret Cosmo created by adding the time for the event, then retrieve
the updated secret. Your updated secret should look like this:

{"venue":"Cosmo´s Place","date":"Soon", "time":"19:00"}
"""

import json
import boto3

# Create a client for Secrets Manager
client = boto3.client("secretsmanager")

# Create a secret for Cosmo
response_create = client.create_secret(
    Name="SurprisePartyDetails",
    SecretString='{"venue":"Cosmo´s Place","date":"Soon"}'
)
print("Secret Created: ", response_create['Name'])

# Retrieve the secret
response_get = client.get_secret_value(SecretId="SurprisePartyDetails")
print("Secret Retrieved: ", json.loads(response_get['SecretString']))

# Update the secret to include the time of the event
response_update = client.update_secret(
    SecretId="SurprisePartyDetails",
    SecretString='{"venue":"Cosmo´s Place","date":"Soon", "time":"6:00 PM"}'
)
print("Secret Updated: ", response_update['ARN'])

# Retrieve the updated secret
response_get_updated = client.get_secret_value(SecretId="SurprisePartyDetails")
print("Updated Secret Retrieved: ", json.loads(response_get_updated['SecretString']))
