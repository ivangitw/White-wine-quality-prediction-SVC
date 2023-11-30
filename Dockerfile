# Install base Python image
FROM tiangolo/uvicorn-gunicorn:python3.11

# Copy files to the container
COPY . /app

# Set working directory to previously added app directory
WORKDIR /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port uvicorn is running on
EXPOSE 8000

COPY model.joblib /app/model.joblib

# Run uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
