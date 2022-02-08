FROM python:3
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt update -y
RUN apt install fim -y
RUN apt install pip -y
RUN apt install nmap -y
RUN apt install python3-nmap -y
RUN pip install nmap
RUN pip install python3-nmap
RUN pip3 install nmap
RUN pip3 install python3-nmap
CMD [ "python3", "./main.py" ]
