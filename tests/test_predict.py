import joblib

from app.machine_learning.model import StrategyModel


def test_load_model():
    """
        Test if the function _load_model load
        correctly the serialized machine learning model.
    """
    mocked_model_path = "tests/models/test_model_predict.pkl"
    mocked_model = joblib.load(mocked_model_path)


    model = StrategyModel._load_model(mocked_model_path)

    assert type(mocked_model) == type(model)


def test_predict():
    """
        Test if the function predict return a str variable.
    """
    mock_data_one_row = [1, 2, 3]

    one_row_prediction = StrategyModel().predict(mock_data_one_row)

    assert isinstance(one_row_prediction[0], str)
