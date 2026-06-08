import boto3
    
def list_s3_buckets():
    try:
        s3= boto3.client("s3", region_name= "us-east-1")
        bucket_names = []
        response = s3.list_buckets()
        for bucket in response["Buckets"]:
            bucket_names.append(bucket["Name"])
        return bucket_names
    
    except Exception as e:
        print(f"Error fetching S3 buckets: {e}")
        return []
