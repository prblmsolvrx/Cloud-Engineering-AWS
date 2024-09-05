"""
script demonstrates creating versions of a secret, updating the secret with both
manually specified and randomly generated passwords, listing the secret versions,
retrieving a secret's value by different version stages, managing secret tags,
and restoring a deleted secret. The purpose of this task is to expose you to how
these operations work within a real script. There's no need for you to write any
code—your task is simply to run the script, observe its execution and understand
what each part of the code is doing.
"""

import boto3

# Initialize the Secrets Manager client
client = boto3.client('secretsmanager')

# Create a new secret version 1
client.create_secret(Name='MyPassword', SecretString='simple password 1')

# Update the secret to version 2
client.update_secret(SecretId='MyPassword', SecretString='simple password 2')

# Generate a strong random password for version 3
strong_password = client.get_random_password(PasswordLength=16)['RandomPassword']

# Update the secret to version 3 and use the generated password
updated_secret_v3 = client.update_secret(SecretId='MyPassword', SecretString=strong_password)

# List Secret versions
versions_response = client.list_secret_version_ids(SecretId='MyPassword')
print('Versions of Secret:', versions_response['Versions']) # Note that only the 2 last versions are returned!

# Retrieve the previous value of the secret using the AWSPREVIOUS staging label
previous_secret_value = client.get_secret_value(SecretId='MyPassword', VersionStage='AWSPREVIOUS')['SecretString']
print('\nPrevious Secret Value (version 2):', previous_secret_value)

# Delete the secret
client.delete_secret(
    SecretId='MyPassword',
    ForceDeleteWithoutRecovery=False,
    RecoveryWindowInDays=7
)

# Restore the secret
response_restore = client.restore_secret(SecretId='MyPassword')
print('\nRestored Secret:', response_restore)

# Tag the secret
response_tag = client.tag_resource(
    SecretId='MyPassword',
    Tags=[{'Key': 'Environment', 'Value': 'Test'}]
)
print('\nTagged Secret:', response_tag)

# Remove tag from the secret
response_untag = client.untag_resource(
    SecretId='MyPassword',
    TagKeys=['Environment']
)
print('\nUntagged Secret:', response_untag)

"""
output :-
Versions of Secret: [{'VersionId': '2f68882c-169a-40f0-a9dd-6b1976f7ccb8', 'VersionStages': ['AWSPREVIOUS'], 'CreatedDate': datetime.datetime(2024, 9, 5, 11, 19, 49, tzinfo=tzlocal())}, {'VersionId': '73cb300a-ef47-4d3c-a8bd-7dac5d94bafb', 'VersionStages': ['AWSCURRENT'], 'CreatedDate': datetime.datetime(2024, 9, 5, 11, 19, 49, tzinfo=tzlocal())}]
Previous Secret Value (version 2): simple password 2
Restored Secret: {'ARN': 'arn:aws:secretsmanager:us-east-1:000000000000:secret:MyPassword-RYJruK', 'Name': 'MyPassword', 'ResponseMetadata': {'RequestId': 'aa763e00-456e-4e44-b670-5f8b224bc8d4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'content-length': '103', 'x-amzn-requestid': 'aa763e00-456e-4e44-b670-5f8b224bc8d4', 'connection': 'close', 'date': 'Thu, 05 Sep 2024 11:19:49 GMT', 'server': 'hypercorn-h11'}, 'RetryAttempts': 0}}
Tagged Secret: {'ResponseMetadata': {'RequestId': '07a68785-32f8-4d87-8116-31ae8692d2ac', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'content-length': '2', 'x-amzn-requestid': '07a68785-32f8-4d87-8116-31ae8692d2ac', 'connection': 'close', 'date': 'Thu, 05 Sep 2024 11:19:49 GMT', 'server': 'hypercorn-h11'}, 'RetryAttempts': 0}}
Untagged Secret: {'ResponseMetadata': {'RequestId': '2f5a0242-ca83-42b0-ad88-04a9e4d53b58', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'content-length': '2', 'x-amzn-requestid': '2f5a0242-ca83-42b0-ad88-04a9e4d53b58', 'connection': 'close', 'date': 'Thu, 05 Sep 2024 11:19:49 GMT', 'server': 'hypercorn-h11'}, 'RetryAttempts': 0}}
"""