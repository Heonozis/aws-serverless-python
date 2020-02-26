import json


def publish_topic(topic, message):
    import boto3
    sns = boto3.client('sns')

    response = sns.publish(
        TopicArn=topic,
        Message=json.dumps(message),
    )

    print(f'Published SNS topic {topic} with message: {json.dumps(message)}')
