# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install required system packages for psycopg2 and other dependencies
RUN # In your Dockerfile for the backend service, add the following line to install wait-for-it.
RUN apt-get update &&  \
    apt-get install -y wait-for-it&&\
    apt-get install -y libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Use CMD to set the host and run app.py when the container launches
CMD ["python", "app.py", "--host", "0.0.0.0"]
