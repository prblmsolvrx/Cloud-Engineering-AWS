"""
how Simple Notification Service (SNS) broadcasts messages to multiple
Simple Queue Service (SQS) queues. Given a Python script that sets
up SNS and SQS, creates an SQS queue, and subscribes it to an SNS topic,
your task is to enhance the script by adding a second SQS queue, subscribing
it to the same SNS topic, and confirming that the SNS message is delivered to both queues.
This setup will enable you to observe how publishing one message to an
SNS topic results in it being deployed to all subscribed SQS queues.
Utilizing long polling for message reading will also demonstrate more
efficient message retrieval from the queues.
"""

import boto3

# Initialize Boto3 resource for SNS and SQS
sns = boto3.resource('sns')
sqs = boto3.resource('sqs')

# Create the first SQS queue
queue_1 = sqs.create_queue(QueueName='MySQSQueue')

# Get the ARN of the SQS queue
queue_arn_1 = queue_1.attributes.get('QueueArn')

# Create the SNS topic
topic = sns.create_topic(Name='MySNSTopic')
topic_arn = topic.arn

# Subscribe the first queue to the topic
topic.subscribe(Protocol='sqs', Endpoint=queue_arn_1)

# Create the second queue
# Subscribe the second queue to the topic
# Create the second SQS queue
queue_2 = sqs.create_queue(QueueName='MySQSQueue2')
# Get the ARN of the second SQS queue
queue_arn_2 = queue_2.attributes.get('QueueArn')
# Subscribe the second queue to the topic
topic.subscribe(Protocol='sqs', Endpoint=queue_arn_2)

# Send an SNS notification
topic.publish(Message='Hello World!')

# Read the message from the first queue with long polling for 10s
messages = queue_1.receive_messages(WaitTimeSeconds=10)

for message in messages:
    print(message.body)

# TODO: Read the message from the second queue with long polling for 10s
messages_2 = queue_2.receive_messages(WaitTimeSeconds=10)

print("Messages from Queue 2:")
for message in messages_2:
    print(message.body)
    message.delete()