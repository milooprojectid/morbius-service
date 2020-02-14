FROM python:3.6

WORKDIR /app

COPY ./main.py /app
COPY ./requirements.txt /app
COPY ./.env /app
COPY ./models /app/models

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
