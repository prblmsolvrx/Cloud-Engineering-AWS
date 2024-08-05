"""
Embark on a mission to enhance your cloud storage skills by completing a multipart upload to Amazon S3.
Your challenge is to upload a 43 MB dataset in three parts to the cosmo-archive-2023 bucket.
The dataset is segmented into chunks of 15 MB, 15 MB, and 13 MB. Although the code for uploading
the first chunk is provided, it has not been executed yet. Your objective is to finalize the script
by seamlessly uploading all three chunks, showcasing your adeptness in managing significant datasets
in S3 with efficiency and accuracy. This task is your opportunity to demonstrate proficiency in
ensuring data integrity and accessibility in the cloud.

Important Note: Running scripts can alter the filesystem's state or modify the resources in
our AWS simulator. To revert to the initial state, you can use the reset button located in
the top right corner. However, keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3

# Configure the S3 client
s3_client = boto3.client('s3')

# Create a new bucket and enable versioning
bucket_name = 'cosmo-archive-2023'
s3_client.create_bucket(Bucket=bucket_name)
s3_client.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={'Status': 'Enabled'})

# Path to your large dataset
file_path = '/usercode/FILESYSTEM/assets/cosmo-hadoop-course-data-set.zip'
key = 'cosmos-hadoop-course-data-set.zip'

# Initiate multipart upload
multipart_upload = s3_client.create_multipart_upload(Bucket=bucket_name, Key=key)
upload_id = multipart_upload['UploadId']

"""
# TODO: Upload the second chunk of 15 MB
# TODO: Upload the final chunk of 13 MB

# TODO: Complete the multipart upload by combining all the uploaded parts
"""

# Upload parts
part_size = 1024 * 1024 * 15  # 15 MB
parts = []
part_number = 1
# Upload the first chunk (15 MB) as an example
with open(file_path, 'rb') as f:
    while True:
        data = f.read(part_size)
        if not data:
            break
        part = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=part_number, UploadId=upload_id, Body=data)
        parts.append({'ETag': part['ETag'], 'PartNumber': part_number})
        part_number += 1

# Complete the multipart upload
s3_client.complete_multipart_upload(
    Bucket=bucket_name,
    Key=key,
    UploadId=upload_id,
    MultipartUpload={'Parts': parts}
)

print('Multipart upload completed successfully.')
        