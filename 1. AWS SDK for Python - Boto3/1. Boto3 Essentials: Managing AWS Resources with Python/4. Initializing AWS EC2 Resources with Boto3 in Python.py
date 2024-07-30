import boto3

# TODO: Use boto3 to initialize an EC2 resource with the default session.
default_session = boto3.Session()
default_ec2_resource = default_session.resource('ec2')

# TODO: Create a custom session targeting the 'us-west-2' region.
custom_session = boto3.Session(region_name='us-west-2')
# TODO: Use the custom session you created to initialize another EC2 resource.
custom_ec2_resource = custom_session.resource('ec2')

"""
Ready to take control? For this task, initialize an EC2 resource in AWS using Boto3.
You will do this twice: first, by leveraging the default session, and second,
by creating a custom session set to the 'us-west-2' region.
This exercise will solidify your understanding of handling AWS resources with Python.
Let’s make it happen!
Important Note: Running scripts can alter the filesystem's state or modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset button located in the top right corner. However,
keep in mind that resetting will erase any code changes. To preserve your code during a reset, consider copying it to the clipboard.
"""