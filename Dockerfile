FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update -y
RUN apt install -y wget \
    build-essential \
    libc6-dev
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod +rx entrypoint.sh
CMD [ "python", "manage.py", "runserver",  "8000" ]