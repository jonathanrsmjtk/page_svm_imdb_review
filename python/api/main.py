from fastapi import FastAPI
from starlette.responses import Response
from starlette.requests import Request
from starlette.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Volumes/Hard Disk/Programming/page_svm_imdb_review/app/python/api/')
import schemas, read
app = FastAPI()

#Add CORS permissions
origins = [
    "http:localhost",
    "http:localhost:8080",
    "http:localhost:3000",
    "http://localhost:3000",
    "http:localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Classify
@app.post("/tweets/classify", response_model=schemas.TweetBase)
def tweet_sentiment(tweet_test: schemas.TweetClassify):
    sentiment_res = read.check_tweet_sentiment(tweets=tweet_test)
    
    return sentiment_res

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)