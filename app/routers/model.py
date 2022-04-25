from typing import List

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from app.settings import get_settings
from app.schemas.cards import Cards, CardsAnalyzed
from app.machine_learning.predictor import predict


settings = get_settings()
router = APIRouter()

client = AsyncIOMotorClient(settings.mongodb_url)
db = client.godsunchained


@router.post("/predict", tags=["model"])
async def post_predict(cards: Cards) -> str:
    """
        Predict the cards strategy(early, late) from its attributes.
    """
    prediction = predict([cards.mana, cards.attack, cards.health])
    
    cards_dict = cards.dict()
    cards_dict.update(strategy=prediction)
    await db["cards"].insert_one(jsonable_encoder(cards_dict))

    return prediction


@router.get("/cards_analyzed", response_model=List[CardsAnalyzed], tags=["model"])
async def list_cards_analyzed():
    """
        List 100 of the cards that were analyzed.
    """
    cards_analyzed = await db["cards"].find().to_list(100)
    return cards_analyzed
