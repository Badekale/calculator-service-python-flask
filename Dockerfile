# Set base image to python
FROM python:3.7

# Copy source file and python req's
COPY . /app
WORKDIR /app

# Install requirements
RUN pip install -r requirements.txt

# Set image's main command and run the command within the container
ENTRYPOINT ["python"]
CMD ["app.py"]
