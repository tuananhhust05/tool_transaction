FROM python:3.8.10

ADD  index.py . 

RUN pip3 install apscheduler mysql-connector-python redis==3.5.3 python-dotenv

CMD ["python3","./index.py"]
