"""
In this task, you are given a script that interacts with an existing Amazon
Simple Queue Service (SQS) queue called 'MyLearningQueue'.
This queue contains motivational messages.
Your task is to complete the script by adding functionality
to receive a message from the queue, print the content of the message,
and then delete it from the queue. Good luck!
"""

import boto3

# Create a boto3 resource for SQS
sqs = boto3.resource('sqs')

# Get the existing queue
queue = sqs.get_queue_by_name(QueueName='MyLearningQueue')

# Receive a message from the queue
messages = queue.receive_messages(MaxNumberOfMessages=1, WaitTimeSeconds=10)

# Check if any messages were received
if messages:
    # Get the first message from the list
    message = messages[0]
    
    # Print the received message body
    print(f"Received message: {message.body}")
    
    # Delete the received message from the queue
    message.delete()
    print("Message deleted from the queue.")
else:
    print("No messages received.")
