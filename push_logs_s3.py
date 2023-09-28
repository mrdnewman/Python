import boto3
import os
import glob

# Initialize the S3 client
s3 = boto3.client('s3')

# Specify the local directory where your log files are located
log_directory = '/path/to/log/files/'

# Specify the S3 bucket name and prefix (folder) where you want to store the logs
bucket_name = 'your-s3-bucket-name'
s3_prefix = 'logs/'

# Specify the file extensions of the logs you want to upload
log_extensions = ['.log', '.txt']

# Get a list of log files matching the specified extensions in the local directory
log_files = [f for f in glob.glob(os.path.join(log_directory, '*')) if os.path.splitext(f)[1] in log_extensions]

# Iterate through the log files and upload them to S3
for log_file in log_files:
    # Extract the file name without the path
    log_filename = os.path.basename(log_file)
    
    # Construct the S3 object key (path in the bucket)
    s3_object_key = s3_prefix + log_filename
    
    # Upload the log file to S3
    s3.upload_file(log_file, bucket_name, s3_object_key)

print("Log files uploaded to S3 successfully.")
