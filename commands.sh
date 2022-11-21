#!/bin/bash

# TODO: don't forget to change this values for your db!
export MONGO_USER="test" && \
    export MONGO_PASS="test" && \
    export MONGO_URL="mongodb+srv://${MONGO_USER}:${MONGO_PASS}@cluster0.sgileys.mongodb.net/?retryWrites=true&w=majority" && \
    export APP_ENV="dev" && \
    python -m uvicorn main:app --reload
# "mongodb+srv://test:test@cluster0.sgileys.mongodb.net/?retryWrites=true&w=majority"