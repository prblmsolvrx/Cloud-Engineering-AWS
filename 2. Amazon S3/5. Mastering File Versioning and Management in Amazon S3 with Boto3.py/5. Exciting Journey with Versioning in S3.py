"""
Dive into the final task of managing space exploration data using Amazon S3!
Your mission is to craft a script that activates bucket versioning and
sequentially uploads a series of cosmic image files. You are provided
with three unique images intended for upload in a specific order.
Each image will replace the previous one under the same object key,
"course-logo.jpg", showcasing how versioning in S3 maintains each
version of an object, even as it's updated or replaced.
After uploading all images, retrieve and print all versions
of the "course-logo.jpg" to demonstrate the history of changes made to this object.
Important Note: Running scripts can alter the filesystem's 
state or modify the resources in our AWS simulator.
To revert to the initial state, you can use the reset button
located in the top right corner. However, keep in mind that
resetting will erase any code changes. To preserve your
code during a reset, consider copying it to the clipboard.
"""

import boto3

s3 = boto3.resource('s3')

# Create a new bucket specifically for our course logos.
bucket_name = 'educational-course-logos'
bucket = s3.create_bucket(Bucket=bucket_name)

# TODO: Enable versioning on this newly created bucket.
bucket.Versioning().enable()
print(f"Versioning enabled on bucket: {bucket_name}")

# Function to upload a file and print confirmation
def upload_file(file_name, object_name):
    bucket.upload_file(file_name, object_name)
    print(f"Uploaded {file_name} as {object_name}")

# TODO: Upload 'prompt-engineering-course-logo.jpg' from '/usercode/FILESYSTEM/assets/' as 'course-logo.jpg'.
upload_file('/usercode/FILESYSTEM/assets/prompt-engineering-course-logo.jpg', 'course-logo.jpg')    

# TODO: Replace 'course-logo.jpg' by uploading 'machine-learning-course-logo.jpg' from the same directory.
upload_file('/usercode/FILESYSTEM/assets/machine-learning-course-logo.jpg', 'course-logo.jpg')

# TODO: Finally, upload 'data-science-python-course-logo.jpg', replacing the current 'course-logo.jpg'.
upload_file('/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg', 'course-logo.jpg')

# TODO: Print a confirmation after each upload, ensuring the process is clear.

# TODO: Retrieve and print all versions of 'course-logo.jpg', displaying the history of this object.
versions = s3.Bucket(bucket_name).object_versions.filter(Prefix='course-logo.jpg')
print("Versions of 'course-logo.jpg':")
for version in versions:
    print(f"VersionId: {version.id}, LastModified: {version.last_modified}, IsLatest: {version.is_latest}")