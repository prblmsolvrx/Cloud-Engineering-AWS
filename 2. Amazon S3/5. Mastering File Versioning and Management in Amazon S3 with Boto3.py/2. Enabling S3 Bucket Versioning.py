import boto3

# Initialize S3 resource
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

bucket_name = 'archive-bucket'

# TODO: Create a new bucket and enable the versioning for it
bucket = s3_resource.create_bucket(Bucket=bucket_name)

# Enable versioning for the bucket
versioning = s3_client.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

print(f"Bucket {bucket_name} created and versioning enabled.")
