import boto3
from app.config import project_location


def get_document(table, key):
    dynamodb = boto3.resource('dynamodb', region_name=project_location)
    table = dynamodb.Table(table)
    try:
        response = table.get_item(Key=key)
        return response['Item']
    except Exception as e:
        print(f'Error occurred while getting {table} document with key {key} and data: {e}')
