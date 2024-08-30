"""
Ensure the SQS resource and SNS client are configured to utilize the provided AWS session, effectively
enabling your script to interact with these AWS services.
Remember, this hands-on practice allows you to apply what you've learned about Boto3 and its ability
to manage AWS services programmatically.
Important Note: As with any operations affecting AWS resources through scripts, be mindful of
the potential changes you are making. During your practices here, you can easily revert any
modifications by using the provided reset functionality. Copying your code before resetting
can help you avoid losing your work.
"""

import boto3

# Pre-configured AWS session - use this to create your SQS resource and SNS client
session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)
print("AWS session has been configured. Ready to proceed with SQS and SNS setup.")

# TODO: Create SQS resource based on the session provided above
sqs_resource_session = session.resource('sqs')
print("sqs_from_session", sqs_resource_session.meta.client.meta.region_name)

# TODO: Create SNS client based on the session provided above
sns_client_session = session.client('sns')
print("sns_from_session", sns_client_session.meta.region_name)
