# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5001
EXPOSE 5001

# Define environment variable
ENV NAME World

# Use CMD to set the host and run app.py when the container launches
CMD ["python", "app.py", "--host", "0.0.0.0"]
