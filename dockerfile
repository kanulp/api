#dockerfile
FROM tiangolo/uvicorn-gunicorn:python3.7

RUN pip install --no-cache-dir fastapi

COPY ./sql_app /app