FROM tiangolo/uvicorn-gunicorn:python3.11

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY model.joblib /app/model.joblib

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
