import boto3


s3 = boto3.client('s3', region_name='us-east-1')

# List all buckets
response = s3.list_buckets()
print("Buckets:")
for r in response['Buckets']:
    print(" -", r['Name'])

# Upload file (private)
local_file = "chelsea_logo.png"  
bucket = "ds2002-dxw2ds"         

with open(local_file, 'rb') as f:
    s3.put_object(
        Body=f,
        Bucket=bucket,
        Key=local_file
    )
print(f"Uploaded {local_file} privately to {bucket}.")

# Upload the same file (as public)
s3.put_object(
    Body=open(local_file, 'rb'),
    Bucket=bucket,
    Key="public_" + local_file,
    ACL='public-read'
)
print(f"Uploaded {local_file} publicly as public_{local_file} to {bucket}.")
