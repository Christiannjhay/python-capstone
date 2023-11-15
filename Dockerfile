# Use an official Python runtime as a parent image
FROM python:3.8.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy only the necessary files to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
