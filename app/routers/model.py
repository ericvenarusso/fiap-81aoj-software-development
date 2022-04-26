from typing import List

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.schemas.cards import Cards, CardsAnalyzed
from app.machine_learning.model import StrategyModel
from app.database_context.mongo import MongoContext
from app.database_context.repository import Repository

router = APIRouter()
repo = Repository(MongoContext("godsunchained"))


@router.post("/predict", tags=["model"])
def post_predict(cards: Cards) -> str:
    """
        Predict the cards strategy(early, late) from its attributes.
    """
    strategy_model = StrategyModel()
    prediction = strategy_model.predict([cards.mana, cards.attack, cards.health])
    
    cards_dict = cards.dict()
    cards_dict.update(strategy=prediction)
    
    repo.insert("cards", jsonable_encoder(cards_dict))

    return prediction


@router.get("/cards_analyzed", response_model=List[CardsAnalyzed], tags=["model"])
def list_cards_analyzed():
    """
        List 100 of the cards that were analyzed.
    """
    return list(repo.select("cards"))[:100]
