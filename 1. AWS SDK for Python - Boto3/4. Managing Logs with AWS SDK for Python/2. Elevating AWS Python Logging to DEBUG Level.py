"""
Following your progress on the hands-on tasks, you're doing an excellent job!
In this exercise, you're introduced to a Python script that leverages the
Boto3 library for AWS S3 operations. The script sets up a resource for S3,
creates a bucket, and lists all available buckets. Your task is to elevate
the existing logging level from the default WARNING to DEBUG. Here's a hint:
leverage Python's logging module to configure the level to DEBUG.
This alteration will provide more descriptive log outputs for your AWS interactions.

Important Notes:

The debug logging output can be viewed under the ERRORS tab in your console.
This is because the debug level logs are treated as errors in the coding environment.
Don't be alarmed, these are not actual errors but helpful debug information for developers.
Running scripts can modify the resources in our AWS simulator.
To revert to he initial state, you can use the reset button located in the top right corner.
However, keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""
import boto3
import logging

# Basic logging setup with DEBUG level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Initialize a boto3 S3 resource
s3 = boto3.resource('s3')

# Create a new bucket
bucket_name = 'my-debug-logging-bucket'
logger.debug(f'Creating bucket: {bucket_name}')
s3.create_bucket(Bucket=bucket_name)
logger.debug(f'Bucket {bucket_name} created.')

# Iteratively print all bucket names
logger.debug('Listing all buckets:')
for bucket in s3.buckets.all():
    logger.debug(f'Bucket found: {bucket.name}')
