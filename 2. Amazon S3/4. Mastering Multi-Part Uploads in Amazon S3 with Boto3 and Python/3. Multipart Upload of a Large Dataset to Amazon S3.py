import boto3

# Initialize the S3 client
s3_client = boto3.client('s3')

# Create a new bucket for your uploads
bucket_name = 'cosmo-archive-2023'
s3_client.create_bucket(Bucket=bucket_name)

# Path to your dataset
file_path = '/usercode/FILESYSTEM/assets/cosmo-hadoop-course-data-set.zip'
key = 'cosmos-hadoop-course-data-set.zip'

# Initiate a multipart upload session
mpu = s3_client.create_multipart_upload(Bucket=bucket_name, Key=key)
upload_id = mpu['UploadId']

# Define part size
part_size = 1024 * 1024 * 5  # 5 MB
parts = []
part_number = 1

# Upload the dataset in chunks
with open(file_path, 'rb') as f:
    while True:
        data = f.read(part_size)
        if not data:
            break
        part = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=part_number, UploadId=upload_id, Body=data)
        parts.append({'ETag': part['ETag'], 'PartNumber': part_number})
        part_number += 1

# Complete the multipart upload by combining all the uploaded parts
s3_client.complete_multipart_upload(
    Bucket=bucket_name,
    Key=key,
    UploadId=upload_id,
    MultipartUpload={'Parts': parts}
)

print('Multipart upload completed successfully.')
