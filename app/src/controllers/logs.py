from flask import request
from utils.log_generator import generate_random_logs

# Handle Generated Logs
def generate_logs(count):
    generated_logs = generate_random_logs(count)

    return generated_logs