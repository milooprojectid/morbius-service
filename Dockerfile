FROM python:3.7-alpine

WORKDIR /app

COPY ./main.py /app
COPY ./requirements.txt /app
COPY ./.env /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
