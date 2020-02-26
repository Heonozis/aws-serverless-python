from app.common.lib import get_topic_data, publish_topic
from app.common.constants import TOPIC_COMMON_HEALTH_OK


def health_handler(event, context):
    data = get_topic_data(event)

    message = data.__dict__()

    publish_topic(TOPIC_COMMON_HEALTH_OK, message)

    return message
