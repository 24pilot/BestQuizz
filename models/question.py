from typing import TypedDict

from bson import ObjectId


class QuizzQuestion(TypedDict):
    _id: ObjectId
    question: str
    answer: str
    yesno: bool
