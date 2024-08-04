"""
Embark on a mission to tidy up our cosmic storage! In this task,
you're provided with code that creates three S3 buckets destined
for different sectors of our interstellar operations. However,
to streamline our data storage, we need to decommission one
of the buckets. Your task is to identify and delete the
interstellar-operations-archive bucket. This will help us
optimize our galactic data management strategy and ensure
efficient use of resources.

Important Note: Running scripts can alter the
filesystem's state or modify the resources in
our AWS simulator. To revert to the initial state,
you can use the reset button located in the top
right corner. However, keep in mind that resetting
will erase any code changes. To preserve your code
during a reset, consider copying it to the clipboard.
"""

import boto3

# Initialize S3 resource
s3_resource = boto3.resource('s3')

# Create three buckets for various interstellar operations
s3_resource.create_bucket(Bucket='interstellar-research-data')
s3_resource.create_bucket(Bucket='interstellar-operations-archive')
s3_resource.create_bucket(Bucket='interstellar-navigation-logs')

# TODO: Delete the 'interstellar-operations-archive' bucket to optimize our storage.
bucket_to_delete = s3_resource.Bucket('interstellar-operations-archive')

# Delete all objects within the bucket before deleting the bucket itself
bucket_to_delete.objects.all().delete()

# Delete the bucket
bucket_to_delete.delete()

print("Remaining buckets after deletion:")
for bucket in s3_resource.buckets.all():
    # This will print the names of the remaining buckets
    print(bucket.name)