import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Event: {}".format(event))
    # Get Data top ten student info from DB
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
