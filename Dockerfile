# FROM python:3.10-slim

FROM python:alpine

RUN pip install --upgrade pip


WORKDIR /app

COPY ./requirements.txt /app/
RUN python3 -m pip install -r requirements.txt
COPY . /app/



# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]


