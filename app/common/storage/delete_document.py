import boto3
from app.config import project_location


def delete_document(table, key):
    dynamodb = boto3.resource('dynamodb', region_name=project_location)
    table = dynamodb.Table(table)
    try:
        response = table.delete_item(Key=key)
    except Exception as e:
        print(f'Error occurred while deleting {table} document with key {key} and data: {e}')
