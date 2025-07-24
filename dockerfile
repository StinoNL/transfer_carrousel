# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/model/prediction prediction

COPY backend/model/stjin_model.pkl .

CMD uvicorn prediction.api_file:app --host 0.0.0.0 --port $PORT
