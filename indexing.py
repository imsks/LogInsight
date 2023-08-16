import json
import re
import requests

# Generate Log Entry from JSON
def generate_log_entry(parts):
    pattern = r'\[(.*?)\] (\w+): (.*)'
    match = re.match(pattern, parts)

    if match:
        timestamp = match.group(1)
        log_level = match.group(2)
        log_message = match.group(3)

        return {
            "timestamp": timestamp,
            "log_level": log_level,
            "log_message": log_message
        }
    
    else:
        print("Log entry does not match the expected format.")

# Variables
log_file_path = "generated_logs.json"
log_entries = []
mapped_log_entries = []

with open(log_file_path, "r") as log_file:
    log_entries = json.load(log_file)

for line in log_entries:
    parts = line.strip()
    log_entry = generate_log_entry(parts)
    mapped_log_entries.append(log_entry)


def run_indexing():
    index_name = "logs"  # Replace with your index name
    es_url = f"http://localhost:5601/{index_name}/_doc"

    for log_entry in log_entries:
        response = requests.post(es_url, json=log_entry)
        print("response", response)

        if response.status_code == 201:
            print("Log entry indexed successfully.")
        else:
            print("Failed to index log entry:", response.content)

run_indexing()