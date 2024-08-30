"""
The script creates an Amazon SQS queue with pre-set attributes.
Your goal is to understand the original queue configuration and
adjust some attributes according to new technical requirements.

Consider the following:
The processing time for messages usually takes 60 minutes, so messages
should become invisible for that duration (VisibilityTimeout).
Messages should remain in the queue for 3 days (MessageRetentionPeriod).
There's a new requirement to have a delivery delay of 30 seconds (DelaySeconds).

"""

import boto3

sqs = boto3.resource('sqs')

# Queue with attributes
queue = sqs.create_queue(
    QueueName='AttributeConfigQueue',
    Attributes={
        'VisibilityTimeout': '3600',
        'DelaySeconds': '30',
        'MessageRetentionPeriod': '259200',
        'ReceiveMessageWaitTimeSeconds': '10'
    }
)

print(f"Queue configured with initial settings. ARN: {queue.attributes.get('QueueArn')}")