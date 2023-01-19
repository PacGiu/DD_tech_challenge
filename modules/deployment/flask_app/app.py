from flask import Flask, request
from joblib import load
import os
from data_science.ds_model import DSModel
import pandas as pd
import json

# training params from config
with open("training_config.json") as config_file:
    config = json.load(config_file)

# load model
MODEL = DSModel(config["max_depth"], config["random_state"])
MODEL.load(
    model_filepath="../../ds/models/model.joblib",
    feature_map_filepath="../../ds/models/feature_map.json",  # "./modules/ds/models/feature_map.json"
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Paco Giudice - DareData Tech Challenge"


@app.route("/predict", methods=["POST"])
def predict():
    # read inputs
    data = request.json

    # preprocess features
    df_features = pd.DataFrame([data["features"]])
    df_features = MODEL.preprocess_data_inference(df_features)

    # predicts
    label = MODEL.predict_with_logging(data["idx"], df_features)

    return {"label": int(label)}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
