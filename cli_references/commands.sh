#!/bin/bash
# Write an array of buckets name
# For loop to iterate over buckets array
buckets=("b2201-b1" "themejexi")

for bucket in "${buckets[@]}"
do
  echo $bucket
  aws s3api put-bucket-lifecycle-configuration --bucket $bucket --lifecycle-configuration file://lifecycle.json
  echo "Lifecycle Applied in bucket"$bucket
done
