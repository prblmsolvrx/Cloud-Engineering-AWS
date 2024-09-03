"""
test your skills in listing SNS topics using the Boto3 resource interface.
A script is provided, which creates 15 SNS topics; however,
the listing part of the script is incomplete. Your task is to
fill in the missing code in order to list all the topics and
print out their ARNs effectively.
"""

import boto3

# Initialize boto3 SNS resource
sns_resource = boto3.resource('sns')

# Create 15 SNS topics
for i in range(15):
    sns_resource.create_topic(
        Name=f'MyTopic{i}'
    )

# TODO: List all SNS topics with their ARNs
topics = list(sns_resource.topics.all())
print("List of SNS Topics:" ,[topic.arn for topic in topics])