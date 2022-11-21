import pymongo
from fastapi import FastAPI

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
    db = client.test

    all_questions = list(db.inventory.find(
        True
    ))
    print(all_questions)
    return {"all questions": all_questions}

