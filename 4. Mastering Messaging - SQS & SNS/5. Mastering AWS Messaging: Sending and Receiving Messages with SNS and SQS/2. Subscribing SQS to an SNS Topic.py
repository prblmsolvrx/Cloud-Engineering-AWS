"""
how to connect Amazon's Simple Queue Service (SQS) and Simple
Notification Service (SNS) to efficiently manage messaging.
Given a Python script which creates an SQS queue and an SNS topic,
your task is to complete the code by subscribing the created SQS queue
to the SNS topic. Your solution code should contain the entire script,
including the creation of the SQS queue, the SNS topic, and the added
subscription.
"""

import boto3

# Initialize Boto3 resource for SNS and SQS
sns_resource = boto3.resource('sns')
sqs_resource = boto3.resource('sqs')

# Create the SQS queue
queue = sqs_resource.create_queue(QueueName='MySQSQueue')

# Get the ARN of the SQS queue
queue_arn = queue.attributes.get('QueueArn')

# Create the SNS topic
topic = sns_resource.create_topic(Name='MySNSTopic')
topic_arn = topic.arn

# TODO: Add code to subscribe the SQS queue to the SNS topic using the topic's `subscribe` method.

subscription = topic.subscribe(
    Protocol='sqs',
    Endpoint=queue_arn,
    ReturnSubscriptionArn=True
)

# Publish a message to the SNS topic using topic object
message = topic.publish(
    Message='Hello from MyDemoTopic!',
)

# Receive message from the SQS queue using queue object
messages = queue.receive_messages(
    WaitTimeSeconds=10,
    MaxNumberOfMessages=10,
)

# Print out the messages
for message in messages:
    print(message.body)