"""
write a Python script that involves AWS Simple Notification Service (SNS).
A pre-written script, which, when executed, creates an SNS topic named
'MyTopic' and assigns a display name attribute to it, will be provided.
Additionally, after creating the SNS topic, the script will list all
existing SNS topics to ensure that your new topic has been created successfully.
There is no need for code modification in this task; your role is
simply to execute the script and observe the topic creation process in AWS SNS.
Pay close attention to how the boto3 resource for AWS SNS is initialized,
how a new topic is created, how a display name attribute is assigned to this topic,
and finally, how the script lists all the SNS topics. Be aware that there is a
pre-existing topic named 'MyHeartbeat' in our environment. However,
this topic might take a bit of time to become available.
Depending on when you click the "Run" button, you may or may not see two
topics in the script output.
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

# Set a display name attribute for the SNS topic
topic.set_attributes(
    AttributeName='DisplayName',
    AttributeValue='My Topic Display Name'
)

# List all SNS topics
topics = list(sns.topics.all())
print("List of SNS Topics:", [topic.arn for topic in topics])