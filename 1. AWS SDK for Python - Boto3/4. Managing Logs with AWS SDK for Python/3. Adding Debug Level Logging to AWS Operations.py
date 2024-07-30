"""
As you progress with Boto3, understanding and implementing logging is crucial
for diagnosing and troubleshooting AWS service interactions.
This exercise focuses on configuring logging for a Boto3 S3 client operation.
Your task is to set up logging to capture and display detailed
DEBUG information specifically for S3 interactions.

Hint: Leverage Python's logging module for configuration and employ
boto3.set_stream_logger() to fine-tune logging for the S3 service
at the DEBUG level.

Important Notes:

The debug logging output can be viewed under the ERRORS tab in your console.
This is because the debug level logs are treated as errors in the coding environment.
Don't be alarmed, these are not actual errors but helpful debug information for developers.
Running scripts can modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset button located
in the top right corner. However, keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3
import logging

# TODO: Set up logging to capture DEBUG information for S3 client interactions
# Configure logging using Python’s logging module
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# TODO: Set boto3 to log DEBUG information for the botocore module
# This captures detailed logs for S3 operations
boto3.set_stream_logger('botocore', level=logging.DEBUG)

# Initialize a boto3 S3 client
s3 = boto3.client('s3')

# TODO: Attempt an S3 operation to generate and capture detailed logs
try:
    response = s3.list_buckets()
    logger.debug(f'Buckets listed successfully: {response}')
except Exception as e:
    # Use logging to report errors
    logger.error("An error occurred:", exc_info=e)
