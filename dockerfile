FROM python:3.10-slim

COPY requirements.txt requirements.txt
COPY backend backend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn backend.model.prediction.api_file:app --host 0.0.0.0 --port $PORT
