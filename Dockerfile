FROM python:3
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt update -y
CMD [ "python3", "./main.py" ]
