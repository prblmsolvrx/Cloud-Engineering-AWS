"""
Impressive work! Let's raise the bar again. You're provided with a Python script that tries to list objects in a S3 bucket.
The script adeptly handles the ClientError exception originating from service's response. This time, your task is to further
enhance this script by incorporating handling for the BotoCoreError, a type of exception
that symbolizes errors within Boto3 itself. In case of a BotoCoreError, print this message: 'Unexpected Boto3 error: {error_message}'.
"""

import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Create an S3 client
s3_client = boto3.client('s3')

# Attempt to list objects of a bucket
try:
    response = s3_client.list_objects(Bucket='cosmo-images-archive-2023')

# ClientError is caught when issues occur at the service level
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'NoSuchBucket':
        print("The requested resource does not exist.")
    elif error_code == 'AccessDenied':
        print("You do not have permissions to access the requested resource.")
    else:
        print(f"Unexpected error occurred with error code: {error_code}")
        
# TODO: Handle possible Boto3 internal errors.
# Handle internal errors
except BotoCoreError as e:
    print(f"An internal Boto3 error occurred: {e}")

# Handle any other exceptions
except Exception as e:
    print(f"An unexpected error occurred: {e}")
