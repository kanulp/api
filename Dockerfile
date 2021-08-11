FROM tiangolo/uvicorn-gunicorn:python3.7

COPY ./sql_app /app/sql_app
#COPY ./requirements.txt /sql_app

WORKDIR ./sql_app

#RUN pip3 install -r requirements.txt
RUN pip3 install fastapi uvicorn mysql-connector-python sqlalchemy

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "88" ]
