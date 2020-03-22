FROM python:3.6-slim

WORKDIR /app

COPY ./main.py /app
COPY ./requirements.txt /app
COPY ./.env /app
COPY ./models /app/models
COPY ./modules /app/modules

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
