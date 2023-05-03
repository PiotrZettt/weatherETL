# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# create a virtual environment
RUN python -m venv /opt/venv

# activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# upgrade pip and install packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# copy the content of the local src directory to the working directory
COPY src/main.py /app

# command to run on container start
CMD [ "python", "./main.py" ]
