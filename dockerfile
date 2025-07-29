FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p clean_data prediction

# 👇 Now move into /app/prediction BEFORE copying app files
WORKDIR /app/prediction

COPY backend/model/prediction/api_file.py .
COPY backend/model/prediction/recommender.py .
COPY backend/model/stjin_model.pkl ../
COPY backend/clean_data/clean_players_clustered.csv ../clean_data/

CMD ["uvicorn", "api_file:app", "--host=0.0.0.0", "--port=8000"]
