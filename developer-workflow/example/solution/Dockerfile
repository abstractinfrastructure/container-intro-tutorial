# This example uses Python
# Alpine is a lightweight OS that makes for smaller containers
FROM python:alpine

# Copy the current working directory contents into the /code folder 
COPY . /code

# Set the default directory to be /code
WORKDIR /code

# Install Python dependencies
RUN pip install -r requirements.txt

# Set the default command to be `python app.py`
CMD ["python", "app.py"]
