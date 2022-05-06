FROM python:3
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt update -y
RUN apt install sudo -y
RUN apt install p7zip-full -y
RUN apt install libncurses5-dev -y
RUN apt install nmap -y
RUN apt install python3-nmap -y
RUN pip3 install -r requirements.txt
RUN pip3 install nmap
RUN pip3 install python3-nmap
CMD [ "python3", "./main.py" ]