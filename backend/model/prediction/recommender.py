import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

def recommend_similar_players_by_name(df, player_name):
    features = ["age", "minutes_played", "goals", "assists", "max_market_value"]
    cluster_players = df[df["cluster"].notna()]

    # Find player row by name (case-insensitive)
    target_player = cluster_players[cluster_players["player_name"].str.lower() == player_name.lower()]
    if target_player.empty:
        return {"error": "Player not found."}

    # Filter same cluster
    target_cluster = target_player["cluster"].values[0]
    cluster_df = cluster_players[cluster_players["cluster"] == target_cluster].copy()

    # Prepare features
    X_cluster = cluster_df[features].dropna()
    player_ids = cluster_df.loc[X_cluster.index, "player_id"].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_cluster)

    # KNN to find similar
    knn = NearestNeighbors(n_neighbors=6)
    knn.fit(X_scaled)
    target_vec = scaler.transform(target_player[features])
    distances, indices = knn.kneighbors(target_vec)

    results = cluster_df.iloc[indices[0]].copy()
    cheaper = results[results["max_market_value"] < target_player["max_market_value"].values[0]].copy()
    cheaper["market_value_million"] = (cheaper["max_market_value"] / 1e6).round(2)

    # Optional cleanup for frontend
    display_cols = [
        "player_id", "player_name", "position", "age", "goals", "assists",
        "max_market_value", "market_value_million", "club_name", "image_url", "cluster_name"
    ]
    return cheaper[display_cols].to_dict(orient="records")
