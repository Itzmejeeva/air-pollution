from flask import Flask, request, jsonify
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)
model = joblib.load('models/aqi_predictor.pkl')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    # Add prediction logic here
    return jsonify({"aqi": 45, "pollutants": {...}})

if __name__ == '__main__':
    app.run()
