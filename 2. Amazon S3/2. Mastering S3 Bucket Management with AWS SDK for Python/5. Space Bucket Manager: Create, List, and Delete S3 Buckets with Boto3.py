"""
Great job making it this far, Space Explorer! 
You've learned a lot about managing S3 buckets
with Boto3. For your final mission, let's apply
all that knowledge. You're tasked with creating
two S3 buckets: 'intergalactic-archive-us'
in the default us-east-1 region and 'intergalactic-archive-eu'
in the eu-central-1 region. Then, list all your buckets
to see your entire galactic collection. Conclude your mission
by safely removing the 'intergalactic-archive-eu' bucket.
Important Note: Running scripts can alter the filesystem's
state or modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset
button located in the top right corner. However,
keep in mind that resetting will erase any code changes.
To preserve your code during a reset,
consider copying it to the clipboard.
"""

import boto3

# TODO: Initialize the S3 resource variable using boto3
S3_resource = boto3.resource('s3')
# TODO: Create a bucket named 'intergalactic-archive-us' in the default region
new_bucket = S3_resource.create_bucket(Bucket="intergalactic-archive-us")
# TODO: Create another bucket named 'intergalactic-archive-eu' in the eu-central-1 region
new_bucket = S3_resource.create_bucket(
    Bucket="intergalactic-archive-eu",
    CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'}
)


# TODO: Print all bucket names available in your AWS account after the creation
buckets = S3_resource.buckets.all()
for bucket in buckets:
    print(bucket.name)
    
# TODO: Delete the 'intergalactic-archive-eu' bucket.
buckets_to_delete = S3_resource.Bucket('intergalactic-archive-eu')
buckets_to_delete.delete()
# TODO: Print all remaining buckets after the deletion
buckets = S3_resource.buckets.all()
for bucket in buckets:
    print(bucket.name)
    
