"""
 a Python script where both Simple Queue Service (SQS)
 and Simple Notification Service (SNS) have been set up
 and the SQS queue has been subscribed to the SNS topic,
 your goal is to complete the remainder. You should publish
 a test message to the SNS topic and then confirm message
 delivery by receiving this message from the subscribed SQS queue.
 Your solution should include both of these operations.
"""

import boto3

# Initialize resources for SNS and SQS
sns_resource = boto3.resource('sns')
sqs_resource = boto3.resource('sqs')

# Create the SQS queue
queue = sqs_resource.create_queue(QueueName='MySQSQueue')

# Get the ARN of the SQS queue
queue_attrs = queue.attributes
queue_arn = queue_attrs['QueueArn']

# Create the SNS topic
topic = sns_resource.create_topic(Name='MySNSTopic')
topic_arn = topic.arn

# Subscribe queue to the topic
subscription = topic.subscribe(Protocol='sqs', Endpoint=queue_arn)

# TODO: Send an SNS notification
message = "hello it's a test message!"
topic.publish(Message=message)

# TODO: Retrieve the message from the queue to verify its arrival. Implement long polling with a duration of 10 seconds.
# Retrieve the message from the queue with long polling (duration of 10 seconds)
messages = queue.receive_messages(
    MaxNumberOfMessages=1,
    WaitTimeSeconds=10
)
