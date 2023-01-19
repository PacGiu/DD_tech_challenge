from sklearn.ensemble import AdaBoostClassifier
from joblib import dump, load
from collections import Counter
from machine_learning_engineering.mle_model import MLEModel
from sklearn import preprocessing
import json
import pandas as pd


class DSModel(MLEModel):
    """
    MLOps class to train and load a model.
    """

    def __init__(self, max_depth, random_state):
        self.model = AdaBoostClassifier()
        self.feature_map = None

    def load(self, model_filepath, feature_map_filepath, *args, **kwargs):
        """
        Loads the model and any required artifacts.
        """
        # load model
        self.model = load(model_filepath)

        # load feature_map
        with open(feature_map_filepath) as f:
            self.feature_map = json.load(f)

    def preprocess_data_inference(self, features):
        """
        Map 'attr_b' categorical column into ints
        """
        features["attr_b"] = features["attr_b"].map(self.feature_map)
        return features

    def predict_batch(self, features):
        """Predicts the labels of data in batch."""
        return self.model.predict(
            features
        )  # TODO: make sure the data is of correct size

    def predict(self, features) -> int:
        """Predicts the label of unseen data."""
        return self.model.predict(features.values)[
            0
        ]  # TODO: make sure the data is of correct size

    def preprocess_data_train(self, df, feature_map_filepath):
        """
        Learn feature_map for 'attr_b' categorical column into ints
        Store the artefact in feature_map_filepath
        TODO: checks on final dataframe types
        """
        # learn categorical feature
        le = preprocessing.LabelEncoder()
        le.fit(df["attr_b"].values)
        df["attr_b"] = le.transform(df["attr_b"].values)

        # save artefact
        self.feature_map = dict(zip(le.classes_, range(len(le.classes_))))
        with open(feature_map_filepath, "w") as f:
            json.dump(self.feature_map, f)

        # downsample majority class
        df_neg = df[df["label"] == 0]  # TODO: labels should not be hardcoded
        df_pos = df[df["label"] == 1]
        df_neg_down = df_neg.sample(len(df_pos), random_state=42)
        df = (
            pd.concat([df_neg_down, df_pos])
            .sample(frac=1, random_state=42)  # shuffle
            .reset_index(drop=True)
        )

        return df

    def fit(self, features, y):
        """Fits the model to the data."""
        self.model.fit(features, y)  # TODO: make sure the data is of correct size

    def save(self, model_filename="model.joblib") -> None:
        """
        Saves the model and any required artifacts to a given location.
        """
        dump(self.model, model_filename)  # TODO: save model with timestamp / accuracy

    def compute_accuracy(self, features, y):
        """
        Computes accuracy on test set
        """
        predictions = self.predict_batch(features)
        counts = Counter(predictions == y)
        accuracy = counts[True] / len(y)
        print("Accuracy:", accuracy)
        return accuracy
