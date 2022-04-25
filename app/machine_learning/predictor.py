from typing import List
from functools import lru_cache

import joblib

from app.settings import get_settings


@lru_cache
def _load_model(model_path: str):
    """
        Load the machine learning serialized model object and
        include in the cache by using the lru algorithm.

        Args:
            model_path: Path of the serialized model object.

        Returns:
            Serialized model object.
    """
    return joblib.load(model_path)


def predict(data: List[int]) -> str:
    """
        Orchestrate the predict step.

        Args:
            data: Data to predict.

        Returns:
            Prediction.
    """
    settings = get_settings()
    model = _load_model(settings.model_path)
    prediction = model.predict([data]).tolist()[0]
    return prediction
