"""
write a Python script demonstrating your mastery of AWS's
Simple Queue Service. Your task is to create a FIFO queue named
EffectiveProcessingFIFOQueue.fifo with custom operational parameters.
The queue you will create should have the following parameters:
- Enable content-based deduplication
- Delay messages delivery by 10 seconds
- Set the maximum message size to 256 KiB
- Retain messages in the queue for 3 days
- The time for polling messages from the queue should be 20 seconds

Important Note: Running scripts can modify the resources in
our AWS simulator. To revert to the initial state, you can
use the reset button located in the top right corner. However,
keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3

# Create a Boto3 resource for SQS
sqs = boto3.resource('sqs')

# TODO: Create an SQS FIFO queue named 'EffectiveProcessingFIFOQueue.fifo' with the prescribed attributes
queue = sqs.create_queue(
    QueueName = 'EffectiveProcessingFIFOQueue.fifo',
    Attributes = {
        'FifoQueue': 'true',  # Indicates that the queue is FIFO
        'ContentBasedDeduplication': 'true',  # Enable content-based deduplication
        'DelaySeconds': '10',  # Delay messages delivery by 10 seconds
        'MaximumMessageSize': str(256 * 1024),  # Set maximum message size to 256 KiB
        'MessageRetentionPeriod': str(3 * 24 * 60 * 60),  # Retain messages for 3 days
        'ReceiveMessageWaitTimeSeconds': '20'  # Set the time for polling messages to 20 seconds
    }
)

print(f"Queue URL: {queue.url}")