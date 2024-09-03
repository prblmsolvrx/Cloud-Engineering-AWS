"""
 existing Python script that interacts with Amazon SQS.
 The current script creates an SQS queue and sends a
 message with two attributes: Author and WeeksOnJob.
 Your task is to add a third attribute, StartingDate,
 representing the job's starting date in a YYYY-MM-DD
 format. After implementing your changes, run the script
 to add the modified message to the queue.
"""

import boto3

# Create an SQS resource
sqs = boto3.resource('sqs')
print("SQS resource created.")

# Create a standard queue
queue = sqs.create_queue(QueueName='test-queue')
print(f"Queue created with URL: {queue.url}")

# Message with custom attributes
response = queue.send_message(
    MessageBody='Hello with attributes!',
    MessageAttributes={
        'Author': {
            'StringValue': 'John Doe',
            'DataType': 'String'
        },
        'WeeksOnJob': {
            'StringValue': '10',
            'DataType': 'Number'
        },
        # TODO: Add a new attribute 'StartingDate' in 'YYYY-MM-DD' format
        'StartingDate': {
            'StringValue': '2001-11-07',
            'DataType': 'String'
        }
    }
)
print(f"Message sent with ID: {response['MessageId']}")