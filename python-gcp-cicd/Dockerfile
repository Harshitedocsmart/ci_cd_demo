# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy current directory contents into container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available for Cloud Run
EXPOSE 8080

# Run your app (adjust if your main script has a different name)
CMD ["python", "main.py"]
 