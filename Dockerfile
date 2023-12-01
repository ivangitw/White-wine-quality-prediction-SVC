FROM tiangolo/uvicorn-gunicorn:python3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
