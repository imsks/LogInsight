import os
import time
import json
import boto3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up AWS Lambda client
lambda_client = boto3.client('lambda', region_name='us-west-2')

class LogFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("HERE", event)
        if event.is_directory:
            return

        if event.src_path.endswith('.json'):
            json_file_path = event.src_path
            invoke_lambda_function(json_file_path)

def invoke_lambda_function(json_file_path):
    response = lambda_client.invoke(
        FunctionName='HelloWorldFunction',  # Update with your Lambda function name
        InvocationType='Event',
        Payload=json.dumps({"file_path": json_file_path})
    )
    print("Lambda invoked with response:", response)

def main():
    path_to_watch = "../generated_logs.json"  # Update with the JSON log file path
    event_handler = LogFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(path_to_watch), recursive=False)
    observer.start()
    print("RUNNING")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()
