# Use an official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker's caching for dependencies
COPY requirements.txt /app/

# Install any required packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . /app/

# Expose a port if needed (e.g., Flask app runs on 5000)
# EXPOSE 5000

# Command to run the Python script (replace with your main file)
CMD ["python", "app.py"]
