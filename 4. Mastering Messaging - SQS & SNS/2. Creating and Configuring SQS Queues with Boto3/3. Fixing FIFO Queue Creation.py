"""
existing Python script is designed to create a FIFO (First In, First Out)
queue in Amazon's Simple Queue Service (SQS) but seemingly contains some
errors preventing the queue from being created correctly. Your goal in
this task is to sift through this script, identify the bug or bugs causing
the problem, and fix them. After correcting the errors, run your updated
script to verify the successful creation of the FIFO queue.
"""

import boto3

sqs = boto3.resource('sqs')

fifo_queue_name = 'FIFOQueue.fifo'

# Creating the FIFO queue
queue = sqs.create_queue(
    QueueName=fifo_queue_name,
    Attributes={
        'FifoQueue': 'true',
        'VisibilityTimeout': '45',
        'DelaySeconds': '5',
        'MaximumMessageSize': '262144',  # in bytes
        'MessageRetentionPeriod': '86400',  # in seconds
        'ContentBasedDeduplication': 'true',
        'ReceiveMessageWaitTimeSeconds': '20'
    }
)

print("FIFO Queue URL:", queue.url)