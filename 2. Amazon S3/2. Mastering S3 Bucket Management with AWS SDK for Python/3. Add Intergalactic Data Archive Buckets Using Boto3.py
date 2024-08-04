"""
Well done on your journey through the cosmos of S3 buckets with Boto3! Now,
let's test your skills further. Create a new bucket specifically
for storing archive data from European space missions
in the eu-central-1 region called cosmo-uploads-archive-europe-2023.
Then, create another bucket cosmo-uploads-archive-us-2023 for
US space mission archives in the default us-east-1 region. Good luck!
Important Note: Running scripts can alter the filesystem's state or
modify the resources in our AWS simulator. To revert to the initial state,
you can use the reset button located in the top right corner. However,
keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3

# Using boto3 to interact with simulated AWS via LocalStack
s3_resource = boto3.resource('s3')

# TODO: Create a new bucket suitable for storing archive data from European space missions in the eu-central-1 region.
new_bucket_1 = s3_resource.create_bucket(
    Bucket = 'cosmo-uploads-archive-europe-2023',
        CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'}
    )
# TODO: Make another bucket in the default us-east-1 region to store archive data from US space missions. No need to specify the region for the default.
new_bucket_2 = s3_resource.create_bucket(Bucket = 'cosmo-uploads-archive-us-2023')
# List all the buckets and print their names
for bucket in s3_resource.buckets.all():
    print(bucket.name) 

"""
Expected output:

cosmo-uploads-archive-europe-2023
cosmo-uploads-archive-us-2023
"""