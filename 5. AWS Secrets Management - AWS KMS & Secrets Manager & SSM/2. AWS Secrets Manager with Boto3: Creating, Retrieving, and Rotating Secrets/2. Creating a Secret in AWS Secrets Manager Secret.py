"""
A secret meeting is scheduled at CodeSignal Learn to discuss our learning
impact strategy. To share the details of the event smartly and securely,
we have decided to use AWS Secrets Manager. Your task is to write a script
that creates a new secret named "StrategyMeeting" in AWS Secrets Manager.
This secret should contain a venue and date attribute, having the values
"CodeSignal Office" and "Tomorrow" respectively.
"""
import boto3

# Initialize the Secrets Manager client
client = boto3.client("secretsmanager")

# TODO: Create the secret for the meeting
response_create = client.create_secret(
    Name="StrategyMeeting",
    SecretString='{"venue" : "CodeSignal Office", "date" : "Tomorrow"}'
)