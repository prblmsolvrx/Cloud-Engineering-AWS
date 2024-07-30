"""
Welcome back! In this task, we will take your understanding of boto3 and AWS a notch higher.
You are given a Python script that attempts to retrieve the list of objects in a
non-existent AWS S3 bucket — a situation that inherently throws an exception.

Your task is to enhance this script by incorporating an exception handling mechanism
to gracefully handle this ClientError exception that arises due to the service's response.

In the ClientError exception, you should discern between various status codes:

'AccessDenied': In this scenario, print this message: 'You do not have permissions
to access the requested resource.'
'NoSuchBucket': Here, print this message: 'The requested resource does not exist.'
For other status codes, just print this generic message:'Unexpected error occurred
with error code: {error_code}'. You can check the status code with e.response['Error']['Code'].
"""

import boto3
from botocore.exceptions import ClientError

# Create an S3 client
s3_client = boto3.client('s3')

# Attempt to list objects of a non-existing bucket which will likely throw an exception
try:
    response = s3_client.list_objects(Bucket='nonexistent_bucket')
    print("Objects in bucket:", response.get('Contents', []))
# TODO: Implement error handling for service level issues.

except ClientError as e:
    error_code = e.response['Error']['Code']
    error_message = e.response['Error']['Message']
    
    # Handle specific error codes
    if error_code == 'NoSuchBucket':
        print(f"Error: The bucket does not exist. {error_message}")
    elif error_code == 'AccessDenied':
        print(f"Error: Access denied. {error_message}")
    else:
        print(f"An unexpected error occurred: {error_message}")
