

def download_from_bucket(bucket, path, destination):
    import boto3
    s3 = boto3.resource('s3')
    s3.Bucket(bucket).download_file(path, destination)
    print(f'File {bucket}/{path} downloaded to {destination}...')
