"""
task is designed to reinforce your understanding of reading and deleting messages from an AWS SQS FIFO (First-In-First-Out) queue.
You'll be implementing Python script which reads and deletes messages from the SQS FIFO queue.
Initially, a FIFO queue named 'student_queue.fifo' is created and 2 messages are sent to this queue. Your task is to:
Receive both messages from the queue in a single call using long polling. Print their contents.
Delete both messages from the queue.
The messages should be processed in the order they were added (First-In-First-Out).
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

queue.send_message(
    MessageBody='First Message',
    MessageGroupId='CodeSignal2021'
)

queue.send_message(
    MessageBody='Second Message',
    MessageGroupId='CodeSignal2021'
)

# TODO: Receive both the messages from the queue in a single call using long polling. Print their contents.
# TODO: Delete both messages from the queue.
messages = queue.receive_messages(
    MaxNumberOfMessages=2,  # Maximum number of messages to retrieve
    WaitTimeSeconds=10  # Long polling duration (up to 20 seconds)
) 

for message in messages:
    print(f'Received message: {message.body}')
# Delete the message from the queue
    message.delete()