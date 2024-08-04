"""
Embark on the ultimate Boto3 and AWS S3 challenge, encapsulating the entire lifecycle of S3 bucket management.
From creation to clean-up, this task will test your proficiency in handling cloud storage with precision.
You'll start by creating a new bucket, then populate it with a series of images that represent various
courses from CodeSignal Learn. After verifying the uploaded contents, you'll remove all objects and
finally delete the bucket itself, showcasing a full spectrum of S3 management skills.
Prepare to execute each step and observe the transformative journey of your S3 bucket from inception to conclusion.
Important Note: Running scripts can alter the filesystem's state or modify the resources
in our AWS simulator. To revert to the initial state, you can use the reset button located in the
top right corner. However, keep in mind that resetting will erase any code changes.
To preserve your code during a reset, consider copying it to the clipboard.
"""

import boto3

# Initialize the boto3 S3 resource
s3 = boto3.resource('s3')

# Create a new bucket
bucket_name = 'full-cycle-management-challenge'

# TODO: Create the bucket using the bucket_name variable
bucket = s3.create_bucket(Bucket=bucket_name)
# Names of the images to be uploaded
images = [
    'prompt-engineering-course-logo.jpg',
    'machine-learning-course-logo.jpg',
    'data-science-python-course-logo.jpg'
]

# TODO: Upload the images to the bucket from '/usercode/FILESYSTEM/assets/'
for image in images:
        file_path = f'/usercode/FILESYSTEM/assets/{image}'
        bucket.upload_file(file_path,image)
        
# TODO: List the contents of the bucket
client = boto3.client('s3')
response = client.list_objects_v2(Bucket=bucket_name)

contents = response.get('Contents',[])
if contents:
    print("Contents of the bucket:")
    for object in contents:
        print(obj['Key'])
    else:
        print("The bucket is empty or the objects could not be listed.")

        
# TODO: Delete all objects from the bucket
if contents:
    for obj in contents:
        bucket.Object(obj['Key']).delete()
        
# TODO: Delete the bucket itself
bucket.delete()
print(f"The bucket '{bucket_name}' and all its objects have been deleted.")
