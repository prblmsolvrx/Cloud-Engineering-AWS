"""
a Python script that initializes a DynamoDB table named Movies and populates
it with several movie records. Each record includes a year and title attribute,
with year serving as the primary key. Your task is to extend the script by writing two Query operations:

Retrieve all movies released in the year 2018.
Retrieve all movies from 2017 that have the title starting with "The".
This exercise aims to enhance your ability to construct and execute Query operations,
a crucial skill for efficiently retrieving specific data sets from DynamoDB.

Important Note: Running scripts can modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset button located in the
top right corner. However, keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3
from boto3.dynamodb.conditions import Key, Attr

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table
table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {'AttributeName': 'year', 'KeyType': 'HASH'},  # Partition key
        {'AttributeName': 'title', 'KeyType': 'RANGE'}  # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'year', 'AttributeType': 'N'},
        {'AttributeName': 'title', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
)

# Wait for the table to be created with custom configuration
dynamodb.meta.client.get_waiter('table_exists').wait(
    TableName='Movies',
    WaiterConfig={'Delay': 2,'MaxAttempts': 10}
)

# Populate table with data
table.put_item(Item={'year': 2016, 'title': 'The Big New Movie'})
table.put_item(Item={'year': 2017, 'title': 'The Bigger, Newer Movie'})
table.put_item(Item={'year': 2017, 'title': 'Yet Another Movie'})
table.put_item(Item={'year': 2017, 'title': 'One More Movie'})
table.put_item(Item={'year': 2015, 'title': 'An Old Movie'})
table.put_item(Item={'year': 2018, 'title': 'Another New Movie'})

# TODO: Write a query to retrieve all movies released in 2018 and print them
response_scan1 = table.query(
    KeyConditionExpression = Key('year').eq(2018)
)
print(response_scan1)

# TODO: Write a query to retrieve all movies from 2017 with titles starting with "The" and print them

response_scan2 = table.query(
    KeyConditionExpression = Key('year').eq(2017) & Key('title').begins_with('The')
)
print(response_scan2)