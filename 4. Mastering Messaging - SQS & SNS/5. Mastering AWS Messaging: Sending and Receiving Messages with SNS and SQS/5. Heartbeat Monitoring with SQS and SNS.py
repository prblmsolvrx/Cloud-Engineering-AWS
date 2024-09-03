"""
an SNS topic named MyHeartbeat with the
ARN arn:aws:sns:us-east-1:000000000000:MyHeartbeat
has already been set up. The MyHeartbeat topic receives
an event every 5 seconds from a background job. Your task
is to leverage your learnt knowledge on Amazon Simple Queue
Service (SQS) and Simple Notification Service (SNS) to complete the following:
Create an SQS queue named MyHeartbeatQueue.
Subscribe the created SQS queue to the MyHeartbeat SNS topic using its ARN.
This SQS queue will capture and store the heartbeat events.
Poll for messages from the newly created SQS queue for 10 seconds and print
out all the messages.
This task simulates a real-world scenario where background jobs or services
constantly send heartbeat messages to ensure effective monitoring and maintain
the health of your system. The goal here is not just to get the task done
but also to get a feel of how this would be used in a professional setting.
"""

import boto3

# Initialize boto3 resource for SNS and SQS
sns = boto3.resource('sns')
sqs = boto3.resource('sqs')

# Create an SQS queue named 'MyHeartbeatQueue'
queue = sqs.create_queue(
    QueueName='MyHeartbeatQueue',
    Attributes={
        'VisibilityTimeout': '30',  # Adjust as necessary
        'FifoQueue': 'false',  # Use 'true' if creating a FIFO queue
    }
)

# Get the 'MyHeartbeat' SNS topic using its ARN
topic_arn = 'arn:aws:sns:us-east-1:000000000000:MyHeartbeat'
topic = sns.Topic(topic_arn)

# Subscribe the created SQS queue to the 'MyHeartbeat' SNS topic
subscription = topic.subscribe(
    Protocol='sqs',
    Endpoint=queue.attributes['QueueArn']
)

# Poll for messages with 'WaitTimeSeconds' of 10, print their bodies, and delete after processing
while True:
    messages = queue.receive_messages(
        WaitTimeSeconds=10,  # Long polling
        MaxNumberOfMessages=10  # Adjust to receive up to 10 messages at a time
    )

    for message in messages:
        # Print the message body
        print(message.body)

        # Delete the message after processing
        message.delete()
