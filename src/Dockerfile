# Use the Python 3.6.9 image
FROM python:3.6.9-stretch

WORKDIR /client

# Copy current directory contents into the container at /client
ADD . /client

# Install the dependencies, update vm
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt update

# start uWSGI
CMD ["uwsgi", "app.ini"]