#!/bin/bash

# Bash script to upload a file to S3 and presign the URL
# How to use it (make sure your in the Lab_7 dir): bash upload_and_presign.sh <picture file> ds2002-dxw2ds <expiration in seconds>

LOCAL_FILE=$1
BUCKET=$2
EXPIRES_IN=$3

aws s3 cp "$LOCAL_FILE" s3://$BUCKET/

aws s3 presign s3://$BUCKET/$LOCAL_FILE --expires-in $EXPIRES_IN
