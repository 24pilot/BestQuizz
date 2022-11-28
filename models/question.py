from typing import TypedDict

from bson import ObjectId
from pydantic import BaseModel


class QuizzQuestion(BaseModel):
    _id: ObjectId
    statement: str
    yesno: bool
