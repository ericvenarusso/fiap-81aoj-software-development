import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from app.machine_learning.trainer import _load_data, _select_features_target, _map_target, _save_model


def test_load_data():
    """
        Test if the function _load_data loads correctly
        by comparing type, columns and size.
    """
    data = _load_data("tests/data/test.csv")

    assert isinstance(data, pd.DataFrame)
    assert list(data.columns) == ["id", "name", "mana", "attack", "health", "type", "god", "strategy"]
    assert data.shape == (14, 8)


def test_select_features_target():
    """
        Test if the function _select_features_target select correctly
        by comparing type, columns and size.
    """
    mocked_data = pd.read_csv("tests/data/test.csv")
    mocked_features_names = ["name", "god"]
    mocked_target = "strategy"

    X, y = _select_features_target(mocked_data, mocked_features_names, mocked_target)

    assert isinstance(X, pd.DataFrame)
    assert isinstance(y, pd.Series)
    assert list(X.columns) == mocked_features_names
    assert X.shape == (14, 2)
    assert y.shape == (14, )


def test_map_target():
    """
        Test if the function _map_target map the target correctly
        by comparing type, equality and size.   
    """
    mocked_data = np.array(["early", "late", "early"])
    mocked_mapped_data = pd.Series([0, 1, 0])

    mapped_data = _map_target(mocked_data)

    assert isinstance(mapped_data, pd.Series)
    assert mapped_data.tolist() == mocked_mapped_data.tolist()
    assert len(mapped_data) == len(mocked_mapped_data)


def test_save_model():
    """
        Test if the function _save_model serialize correctly the
        machine learning model.
    """
    mocked_model = RandomForestClassifier()
    mocked_model_path = "tests/models/test_model_train.pkl"
    
    _save_model(mocked_model, mocked_model_path)

    assert os.path.isfile(mocked_model_path)
