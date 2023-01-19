from data_science.ds_model import DSModel
from utils import wait_for_table
import json

# training params from config
with open("training_config.json") as config_file:
    config = json.load(config_file)

# wait for feature_store table to be created
df = wait_for_table(config["feature_store_table"])

# init model
model = DSModel(config["max_depth"], config["random_state"])

# preprocess data
df = model.preprocess_data_train(df, config["feature_map_filepath"])

# split train / test set
df_test = df.sample(frac=config["test_ratio"])
df_train = df.drop(df_test.index)
df_test = df_test.reset_index(drop=True)
df_train = df_train.reset_index(drop=True)
X_train = df_train[config["feature_cols"]]
y_train = df_train[config["label_col"]].values
X_test = df_test[config["feature_cols"]]
y_test = df_test[config["label_col"]].values

# model training
model.fit(features=X_train, y=y_train)

# metrics
accuracy = model.compute_accuracy(X_test, y_test)  ## TODO: store with model

# save
model.save(config["output_filepath"])
