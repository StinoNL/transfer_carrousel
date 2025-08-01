# Dockerfile

FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

RUN mkdir -p /app/clean_data /app/prediction

WORKDIR /app/prediction
COPY backend/model/prediction/api_file.py .
COPY backend/model/prediction/recommender.py .

COPY backend/model/stjin_model.pkl    /app/stjin_model.pkl
COPY backend/clean_data/clean_players_clustered.csv \
     /app/clean_data/clean_players_clustered.csv

EXPOSE 8080
ENV PORT=8080

CMD ["sh", "-c", "uvicorn api_file:app --host 0.0.0.0 --port $PORT"]
