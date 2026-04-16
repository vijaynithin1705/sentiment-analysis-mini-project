from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text.strip():
        raise ValueError("Input cannot be empty")
    
    result = classifier(text)[0]
    label = result["label"]   
    score = result["score"]   
    
    if score < 0.70:
        sentiment = "Neutral"
    elif label == "POSITIVE":
        sentiment = "Positive"
    else:
        sentiment = "Negative"
    
    return {"sentiment": sentiment, "confidence": round(score, 4), "raw_label": label}