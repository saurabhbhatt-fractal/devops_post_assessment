# Official Python image
FROM python:3.9-slim

# Setting up the working directory
WORKDIR /devops_post_assessment

# Copying requirements txt
COPY requirements.txt .

# Installing the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying all the file in the container
COPY . .

EXPOSE 8080

# Command to run the Fastapi
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
