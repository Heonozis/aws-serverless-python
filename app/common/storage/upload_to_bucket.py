from mimetypes import guess_type


def upload_to_bucket(bucket, path, data, metadata=None):
    import boto3

    client = boto3.client('s3')
    content_type = guess_type(path)[0]

    client.put_object(Body=data, Bucket=bucket, Key=path, ContentType=content_type, Metadata=metadata)

    print(f'File {path} saved to S3 {bucket}...')

    return path
