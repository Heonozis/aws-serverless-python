import boto3
from app.config import project_location


def update_document(table, key, update_expression):
    dynamodb = boto3.resource('dynamodb', region_name=project_location)
    try:
        table = dynamodb.Table(table)
        response = table.update_item(Key=key, UpdateExpression=update_expression, ReturnValues="UPDATED_NEW")
        return response
    except Exception as e:
        print(f'Error occurred while updating {table} document with key {key} and update expression  "{update_expression}": {e}')
