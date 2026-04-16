from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import get_sentiment

app = FastAPI(title="Sentiment Analysis API")

class TextInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float
    raw_label: str

@app.get("/")
def root():
    return {"message": "Sentiment API is running!"}    

@app.post("/predict",  response_model=SentimentResponse)
def analyze(input: TextInput):
    try:
        result = get_sentiment(input.text)
        return result
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))

