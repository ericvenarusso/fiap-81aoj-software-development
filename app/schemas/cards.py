from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Cards(BaseModel):
    _id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    id: int = Field(...)
    mana: int = Field(...)
    attack: int = Field(...)
    health: int = Field(...)
    creted_date: datetime = Field(default_factory=datetime.now)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "mana": 3,
                "attack": 2,
                "health": 2 
            }
        }
    

class CardsAnalyzed(BaseModel):
    _id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    id: int = Field(...)
    mana: int = Field(...)
    attack: int = Field(...)
    health: int = Field(...)
    strategy: str = Field(...)
    creted_date: datetime = Field(default_factory=datetime.now)
