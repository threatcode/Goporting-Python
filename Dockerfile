FROM python:3.13.0a3-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

WORKDIR $APP_HOME
COPY . ./

RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install -r requirments.txt

CMD [ "python", "./setup.py" ]
