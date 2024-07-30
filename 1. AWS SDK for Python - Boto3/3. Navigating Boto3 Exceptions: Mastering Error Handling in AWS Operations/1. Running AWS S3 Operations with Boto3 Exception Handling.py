import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Create an S3 client
s3_client = boto3.client('s3')

# Try to list objects of non-existent bucket
try:
    response = s3_client.list_objects(Bucket='non-existent-bucket')

# Handle possible errors
except ClientError as e:
    if e.response['Error']['Code'] == 'NoSuchBucket':
        print("The bucket does not exist.")
    elif e.response['Error']['Code'] == 'AccessDenied':
        print("You do not have permissions to access the bucket.")
    else:
        print("Unexpected error:", e.response['Error']['Message'])

# Catch errors within Boto3 itself
except BotoCoreError as e:
    print("Boto3 error:", e)

"""
In this task, your primary objective is to observe a Python script
in action that attempts to list all objects of a non-existent S3 bucket,
which inevitably triggers an exception. This exercise will expose you
to how AWS service exceptions during operations are handled effectively
in real-world scenarios. Your role is to run the script and understand
the error handling process - no code modifications are needed for this task.
"""