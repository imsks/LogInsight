import json
import requests

def set_logs():
    print("THIS IS POST CALL")

def get_logs():
    print("THIS IS GET CALL")

def lambda_handler(event, context):
    try:
        http_method = event['httpMethod']
        body = event['body']
        print("HERE", body)

        if http_method == "GET":
            get_logs()
        elif http_method == "POST":
            set_logs()
            
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
