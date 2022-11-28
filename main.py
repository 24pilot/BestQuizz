import pymongo
from fastapi import FastAPI

from models.question import QuizzQuestion
from models.question_payload import QuizzQuestionPayload

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/all")
async def show_all():
    client = pymongo.MongoClient(
        "mongodb+srv://test:test@cluster0.sgileys.mongodb.net/?retryWrites=true&w=majority"
    )
    #mongodb+srv://test:<password>@cluster0.sgileys.mongodb.net/?retryWrites=true&w=majority
    print("client ->>", client)
    db = client.test
    print("DB->>", db)
    all_questions = list(db.bestquizz.find())
    print("Respond>>> ",all_questions)
    return {"all questions": all_questions}

@app.put("/create")
async def create(question: QuizzQuestionPayload) -> str:
    client = pymongo.MongoClient(
        "mongodb+srv://test:test@cluster0.sgileys.mongodb.net/?retryWrites=true&w=majority"
    )
    #mongodb+srv://test:<password>@cluster0.sgileys.mongodb.net/?retryWrites=true&w=majority
    print("client ->>", client)
    db = client.test
    print("DB->>", db)
    db_question = question.dict()
    print("db_ques>>", db_question)
    result = db.bestquizz.insert_one(db_question)
    print("ID>>", result.inserted_id, type(result.inserted_id))
    return str(result.inserted_id)


