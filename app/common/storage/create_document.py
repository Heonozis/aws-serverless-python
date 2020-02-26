import boto3
from app.config import project_location


def create_document(table, key, data):
    dynamodb = boto3.resource('dynamodb', region_name=project_location)
    try:
        table = dynamodb.Table(table)
        response = table.put_item(Item=data)
    except Exception as e:
        print(f'Error occurred while creating {table} document with key {key} and data {data}: {e}')


