FROM tiangolo/uvicorn-gunicorn:python3.7

COPY ./sql_app /app
COPY ./requirements.txt /sql_app

WORKDIR /sql_app

RUN pip3 install -r requirements.txt

CMD [ "uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "4400" ]
