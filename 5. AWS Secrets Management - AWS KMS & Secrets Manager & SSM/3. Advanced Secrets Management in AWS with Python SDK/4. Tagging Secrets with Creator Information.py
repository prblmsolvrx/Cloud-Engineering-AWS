"""
add to the python script and make it tag the secret, indicating that Cosmo is the creator.
By tagging secrets, you can classify and manage them more efficiently,
depending on your organizational needs.
"""

import boto3

# Initialize the boto3 Secrets Manager client
sm = boto3.client('secretsmanager')

# Create a new secret 
response = sm.create_secret(Name='CosmosSecret', SecretString='mysecret')

# TO DO: Tag the secret with Cosmo as the creator
sm.tag_resource(
    SecretId=response['ARN'],  # Use the ARN or the name of the secret
    Tags=[
        {
            'Key': 'Creator',
            'Value': 'Cosmo'
        }
    ]
)

print("Secret created and tagged successfully.")