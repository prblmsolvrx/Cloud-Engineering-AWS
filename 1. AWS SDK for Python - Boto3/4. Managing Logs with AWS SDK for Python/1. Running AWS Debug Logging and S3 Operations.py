"""
Here, you have a piece of Python code that initializes an S3 resource,
applies AWS debug logging, creates a new bucket, and then lists all the available buckets.
You need to run this script to observe how Python interacts with the local AWS environment
and how the debugging logs offer insights into those interactions.

Important Notes:

The debug logging output can be viewed under the ERRORS tab in your console.
This is because the debug level logs are treated as errors in the coding environment.
Don't be alarmed, these are not actual errors but helpful debug information for developers.
Running scripts can modify the resources in our AWS simulator. To revert to the initial state,
you can use the reset button located in the top right corner. However, keep in mind that
resetting will erase any code changes. To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the boto3 S3 resource
s3 = boto3.resource('s3')

# Apply the AWS debug logging filter
boto3.set_stream_logger('boto3', logging.DEBUG)

# Create a new bucket as the initial setup is empty
s3.create_bucket(Bucket='my-logging-test-bucket')

# List buckets to show logging output
for bucket in s3.buckets.all():
    print(bucket.name)