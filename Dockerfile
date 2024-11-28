From python:3

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt