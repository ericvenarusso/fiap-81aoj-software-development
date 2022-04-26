from typing import List
from functools import lru_cache

import joblib

from app.settings import get_settings


class StrategyModel:
    def __init__(self):
        self.settings = get_settings()
        self.model = self._load_model(self.settings.model_path)

    @staticmethod
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


    def predict(self, data: List[int]) -> str:
        """
            Orchestrate the predict step.

            Args:
                data: Data to predict.

            Returns:
                Prediction.
        """
        
        return self.model.predict([data]).tolist()[0]
