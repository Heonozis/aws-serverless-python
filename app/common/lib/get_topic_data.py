import base64
import json


def get_topic_data(event):
    try:
        data = event['Records'][0]['Sns']['Message']
        data = json.loads(data)
    except KeyError as e:
        raise ValueError('Invalid SNS message.')

    print(f'Received SNS message: {json.dumps(data)}')

    return data
