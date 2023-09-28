FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update -y
RUN apt install -y wget \
    build-essential \
    libc6-dev
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN chmod +rx entrypoint.sh