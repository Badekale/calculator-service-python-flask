# The first instruction is what image we want to base our container on
# We use an official Python runtime as a parent image
FROM python:3.7

# Copy source file and python requirements and set the working directory to /app
COPY . /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set image's main command and run the command within the container
ENTRYPOINT ["python"]
CMD ["app.py"]