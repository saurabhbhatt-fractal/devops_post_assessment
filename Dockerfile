# Official Python image
FROM python:3.9-slim

# Setting up the working directory
WORKDIR /DEVOPS_POST_ASSESSMENT

# Copying all the file in the container
COPY . .

# Installing the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Fastapi
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]