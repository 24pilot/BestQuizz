from pydantic import BaseModel\

class QuizzQuestionPayload(BaseModel):
    statement: str
    yesno: bool
