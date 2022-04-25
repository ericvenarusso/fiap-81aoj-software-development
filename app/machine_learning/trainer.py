from typing import List, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import hydra
from omegaconf import DictConfig


def _load_data(data_path: str) -> pd.DataFrame:
    """
        Load train data from a csv file.

        Args:
            data_path: Path from the data.
        
        Returns:
            Loaded data into a pandas DataFrame.
    """
    return pd.read_csv(data_path)


def _select_features_target(
    data: pd.DataFrame,
    features: List[str],
    target: str = None) -> Tuple[pd.DataFrame, pd.Series]:
    """"
        Select train features and separate in DS notation.

        Args:
            X: Features that is going to be used to train the model.
            y: Target variable.

        Returns:
            A tuple with two objects(DataFrame, Series) separated into
            Features and target variables.
    """
    X = data[features]
    y = data[target]

    return X, y

def _map_target(target: np.array) -> pd.Series:
    """"
        Binarize a target column.

        Args:
            target: Target column object.
        
        Returns:
            Binarized target column.
    """
    return pd.Series(target).map({"early": 0, "late": 1})


def _evaluate_metric(y_true: pd.Series, y_test: pd.Series, metric):
    """
        Evaluate machine learning model using a metric.

        Args:
            y_true: True target column object.
            y_test: Test target column object.
            metric: Metric that will evaluate the model.

        Returns:
            Metric Score.
    """
    y_true_mapped = _map_target(y_true) 
    y_test_mapped = _map_target(y_test)
    return hydra.utils.instantiate(metric, y_true_mapped, y_test_mapped)


def _save_model(model, model_path: str) -> None:
    """
        Save the machine learning model into a serilized object.

        Args:
            model: Machine Learning Model.
            model_path: Path to save the serialized machine learning object.
    """
    joblib.dump(model, model_path)


@hydra.main(config_path="config/train", config_name="config.yaml")
def train(config: DictConfig) -> None:
    """
        Orchestrate the train process using Hydra library.

        Args:
            config: Hydra configuration file.
    """
    print(f"Training model with configuration:")
    print(f"Dataset features: {config.dataset}")
    print(f"Model parameters: {config.machine_learning.model}")

    data = _load_data(config.dataset.path)
    X, y = _select_features_target(data, config.dataset.features, config.dataset.target)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=22)

    model = hydra.utils.instantiate(config.machine_learning.model)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    metric = _evaluate_metric(y_test, y_pred, config.machine_learning.metric)

    _save_model(model, config.machine_learning.path)

    print(f"Your model was sucessfully trained!! Metric {config.machine_learning.metric._target_}: {metric}")


if __name__ == "__main__":
    train()
