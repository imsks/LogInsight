import datetime
import random
import json

# Variables
number_entries = 100
generated_logs = []

# Log Levels
log_levels = ["INFO", "WARNING", "ERROR"]

# Log Messages
log_messages = [
    "User logged in successfully.",
    "Disk space is running low.",
    "Database connection failed."
]

# Generate Timestamps
def generate_timestamps():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("[%Y-%m-%d %H:%M:%S]")
    return formatted_time

# Generate Log Entry => [2023-08-05 10:15:32] INFO: User logged in successfully.
def generate_log():
    timestamp = generate_timestamps()
    random_number = random.randint(0, len(log_levels) - 1)
    log_level = log_levels[random_number]
    log_message = log_messages[random_number]

    return f"[{timestamp}] {log_level}: {log_message}"

# Loop and Generate Logs
for i in range(number_entries):
    log = generate_log()
    generated_logs.append(log)

# Save logs into JSON
filename = "generated_logs.json"
with open(filename, 'w') as json_file:
    json.dump(generated_logs, json_file)