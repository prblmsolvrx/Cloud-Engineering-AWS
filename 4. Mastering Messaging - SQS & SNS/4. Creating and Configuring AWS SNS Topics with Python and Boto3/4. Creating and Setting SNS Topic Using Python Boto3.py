"""
you'll combine what you've learned about AWS Simple Notification Services (SNS)
and write a Python script from scratch. Your script will create an SNS topic named
'MyTopic', retrieve its Amazon Resource Name (ARN), and then set a Display
Name attribute for this created topic. The Display Name is an attribute that
appears in the "From" field for notifications sent via email. Please remember
to print out the Topic ARN and a success message after setting the
Display Name attribute.
"""

# TODO: You need to write a script that satisfies the following:
# 1. Initializes a boto3 resource for AWS SNS
# 2. Creates a new SNS topic named 'MyTopic' and retrieves its ARN
# 3. Prints the ARN of the created topic
# 4. Sets a DisplayName attribute for the created topic using its ARN
# 5. Prints a success message after setting the DisplayName attribute

import boto3
sns = boto3.resource('sns')

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

print("Success")