FROM python:3.10

ADD main.py .
ADD requirements.txt .
ADD .env .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]