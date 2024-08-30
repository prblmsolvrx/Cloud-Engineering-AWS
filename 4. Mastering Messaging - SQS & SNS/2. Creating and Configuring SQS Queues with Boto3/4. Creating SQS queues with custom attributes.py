"""
demonstrate your knowledge of AWS Simple Queue Service by writing a Python script to create
a standard queue named AttrConfigStandardQueue.
The queue should have the following settings:
The visibility timeout of the queue should be set to 20 minutes
The time that the receiver has to wait until receiving the message should be set to 10 seconds
"""

import boto3

# Create an SQS resource
sqs = boto3.resource('sqs')

# TODO: Create a standard SQS queue named 'AttrConfigStandardQueue' 
# TODO: Set the queue attributes 'VisibilityTimeout' to 20 minutes and 'ReceiveMessageWaitTimeSeconds' to 10 seconds

queue = sqs.create_queue(
    QueueName='AttrConfigStandardQueue',
    Attributes={
        'VisibilityTimeout': str(20 * 60),  # 20 minutes in seconds
        'ReceiveMessageWaitTimeSeconds': '10'  # 10 seconds
    }
)

# Print the queue URL
print(f"Queue URL: {queue.url}")