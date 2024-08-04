"""
Explore AWS S3 and Boto3 by engaging
with a practical task that involves
managing course logos for CodeSignal
Learn. Your objective is to complete
a script that not only populates the
'codesignal-learn-course-logos' bucket
with specific course logos but also lists
all objects within it after the upload.
The provided script already includes
steps for creating the bucket and uploading
logos. Your key task is to add the final
piece: the logic to list all the objects
in the bucket, demonstrating your ability
to navigate and manage cloud resources effectively.
Important Note: Running scripts can alter
the filesystem's state or modify the resources
in our AWS simulator. To revert to the initial
state, you can use the reset button located
in the top right corner. However, keep in mind
that resetting will erase any code changes.
To preserve your code during a reset, consider
copying it to the clipboard.
"""

import boto3

# Initialize the boto3 S3 resource
s3 = boto3.resource('s3')

# Create the bucket as the initial setup is empty
bucket_name = 'codesignal-learn-course-logos'
s3.create_bucket(Bucket=bucket_name)

# Upload course logos to the S3 bucket from the filesystem
s3.Bucket(bucket_name).upload_file('/usercode/FILESYSTEM/assets/prompt-engineering-course-logo.jpg', 'prompt-engineering-course-logo.jpg')
s3.Bucket(bucket_name).upload_file('/usercode/FILESYSTEM/assets/machine-learning-course-logo.jpg', 'machine-learning-course-logo.jpg')
s3.Bucket(bucket_name).upload_file('/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg', 'data-science-python-course-logo.jpg')

# TODO: List all objects in the bucket
client = boto3.client('s3')
response = client.list_objects_v2(Bucket=bucket_name)

# Print out the object names
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
    else:
        print("The bucket is empty or the objects could not be listed.")