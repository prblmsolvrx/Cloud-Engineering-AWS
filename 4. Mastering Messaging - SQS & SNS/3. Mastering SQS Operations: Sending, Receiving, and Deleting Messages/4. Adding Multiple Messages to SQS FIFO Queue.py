"""
you'll interact with an AWS SQS FIFO (First-In-First-Out) queue.
A FIFO queue named 'student_queue.fifo' is created initially.
You're tasked to send two messages to this queue, with each message
having the same MessageGroupId of 'CodeSignal2021'.
The content of these messages doesn't matter.
This task aims to help you learn how to properly send messages
to an SQS FIFO queue using Python (boto3).

"""

import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(
    QueueName='student_queue.fifo',
    Attributes={
        'FifoQueue': 'true',
        'ContentBasedDeduplication': 'true'
    }
)

# TODO: Send 2 messages to the queue with the same MessageGroupId of 'CodeSignal2021'.
queue.send_message(
    MessageBody='First message to the FIFO queue',
    MessageGroupId='CodeSignal2021',
    MessageDeduplicationId='first-message'
)

queue.send_message(
    MessageBody='Second message to the FIFO queue',
    MessageGroupId='CodeSignal2021',
    MessageDeduplicationId='second-message'
)

print("Messages sent successfully!")