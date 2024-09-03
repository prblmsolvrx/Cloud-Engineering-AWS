"""
 task of extending a provided Python script.
 The initial part of the script creates an
 AWS SNS topic named 'MyTopic'. Your duty is
 to extend this script by adding additional
 functionality that sets the DisplayName attribute
 for the created SNS topic using the assigned TopicArn.
 As you've learned in the lessons, the DisplayName appears
 as the "From" field in notifications sent via email.
 Upon successful execution, the script should print out
 the TopicArn and the successful setting of the DisplayName attribute.
"""

import boto3

# Initialize boto3 SNS resource
sns = boto3.resource('sns')

# Create a new SNS topic 
topic = sns.create_topic(
    Name='MyTopic'
)

# Confirm the SNS topic creation
print("Created SNS topic:", topic.arn)

# TODO: Set a display name attribute for the SNS topic
topic.set_attributes(
     AttributeName='DisplayName',
    AttributeValue='My Topic Display Name'
)