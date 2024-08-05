"""
Your objective is to execute the final steps of the script:

Retrieve All Version IDs: Implement the section of the script
that fetches all version IDs for the object named versioned-course-logo.jpg.
This step is crucial for identifying the available versions of the file.
Download a Specific Version: Based on the version IDs retrieved, modify
the script to download the very first version of versioned-course-logo.jpg
uploaded to the bucket. Note that, due to the reversed chronological order
in which they are listed, the first version uploaded will be the last in the list.
This downloaded file should be saved to the /usercode/FILESYSTEM/downloads
folder, demonstrating your ability to access and restore specific versions
of an object in a version-enabled S3 bucket.
Important Note: Running scripts can alter the file system's state or
modify the resources in our AWS simulator. To revert to the initial
state, you can use the reset button located in the top right corner.
However, remember that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3
import os

# Create S3 resource and client
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# Ensure that /usercode/FILESYSTEM/downloads folder exists
downloads_folder = "/usercode/FILESYSTEM/downloads"
os.makedirs(downloads_folder, exist_ok=True)

# Create S3 bucket called `cosmo-course-logos`
bucket_name = 'cosmo-course-logos'
s3.create_bucket(Bucket=bucket_name)

# Enable versioning for created bucket
s3.BucketVersioning(bucket_name).enable()

# Upload files to the bucket
s3_client.upload_file(Filename='/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg', Bucket=bucket_name, Key='versioned-course-logo.jpg')
s3_client.upload_file(Filename='/usercode/FILESYSTEM/assets/machine-learning-course-logo.jpg', Bucket=bucket_name, Key='versioned-course-logo.jpg')

# Retrieve all version ids for 'versioned-course-logo.jpg'
versions = s3_client.list_object_versions(Bucket=bucket_name, Prefix='versioned-course-logo.jpg')

version_ids = [version['VersionId'] for version in versions.get('Versions', [])]
version_ids.sort(reverse=True)  # Sorting to get the earliest version last

# Print all version IDs
print("Version IDs:", version_ids)

# Download the earliest version of 'versioned-course-logo.jpg' to the '/usercode/FILESYSTEM/downloads/' folder
if version_ids:
    earliest_version_id = version_ids[-1]  # Last item in sorted list is the earliest version
    s3_client.download_file(
        Bucket=bucket_name,
        Key='versioned-course-logo.jpg',
        Filename=os.path.join(downloads_folder, 'earliest-version-course-logo.jpg'),
        ExtraArgs={'VersionId': earliest_version_id}
    )
else:
    print("No versions found for the object.")
