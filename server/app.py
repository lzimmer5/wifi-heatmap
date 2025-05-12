from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__, static_folder="../static")
data = pd.read_csv("wifi_data.csv")

@app.route("/api/wifi_data")

def wifi_data():
    min_lat = float(request.args.get("min_lat"))
    max_lat = float(request.args.get("max_lat"))
    min_lng = float(request.args.get("min_lng"))
    max_lng = float(request.args.get("max_lng"))

    filtered = data[
        (data["lat"] >= min_lat) &
        (data["lat"] <= max_lat) &
        (data["lng"] >= min_lng) &
        (data["lng"] <= max_lng)
    ]

    return jsonify([
        {"lat": row["lat"], "lng": row["lng"], "weight": row["strength"]}
        for _, row in filtered.iterrows()
    ])

@app.route("/")
def root():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(port=80, debug=True)