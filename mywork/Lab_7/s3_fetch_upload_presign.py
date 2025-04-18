import boto3
import requests
import argparse

parser = argparse.ArgumentParser(description="Fetch a file, upload to S3, and generate a presigned URL.")
parser.add_argument("--url", required=True, help="The URL of the file to fetch")
parser.add_argument("--bucket", required=True, help="The name of the S3 bucket")
parser.add_argument("--key", required=True, help="The object name to use in S3")
parser.add_argument("--expires", type=int, default=604800, help="Expiration time in seconds (default: 7 days)")
args = parser.parse_args()

s3 = boto3.client('s3', region_name='us-east-1')

response = requests.get(args.url)
with open(args.key, 'wb') as f:
    f.write(response.content)
print(f"Downloaded file from {args.url} and saved as {args.key}.")

with open(args.key, 'rb') as data:
    s3.put_object(Bucket=args.bucket, Key=args.key, Body=data)
print(f"Uploaded {args.key} to S3 bucket {args.bucket}.")

presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': args.bucket, 'Key': args.key},
    ExpiresIn=args.expires
)

print("Presigned URL (valid for {} seconds):".format(args.expires))
print(presigned_url)

