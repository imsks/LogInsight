# Use an official Lambda base image
FROM public.ecr.aws/lambda/python:3.8

# Copy the Lambda function code into the container
COPY core/app.py /var/task/

# Set environment variables for the Lambda handler and the runtime interface emulator
ENV AWS_LAMBDA_FUNCTION_NAME=LogInsightsFunction
ENV AWS_LAMBDA_FUNCTION_MEMORY_SIZE=256
ENV AWS_LAMBDA_FUNCTION_TIMEOUT=3
ENV AWS_LAMBDA_EVENT_BODY=/var/runtime/events/event.json

# Expose the runtime interface emulator on port 8080
EXPOSE 8080


# Start the runtime interface emulator
CMD ["runtime", "docker", "run", "-v", "/var/task:/var/task", "-v", "/tmp:/tmp", "8000"]
