from model import get_sentiment

tests = [
    ("I absolutely loved this movie, it was fantastic!", "Positive"),
    ("The service was excellent and the staff were so kind.", "Positive"),
    ("What a wonderful day, everything went perfectly!", "Positive"),
    ("This is the best product I have ever purchased.", "Positive"),
    ("This is absolutely terrible, I hated every second.", "Negative"),
    ("The food was disgusting and the place was filthy.", "Negative"),
    ("I'm so disappointed, this was a complete waste of money.", "Negative"),
    ("Worst experience of my life, would never recommend.", "Negative"),
    ("The meeting is scheduled for 3pm on Tuesday.", "Neutral"),
    ("The report contains twelve pages of data.", "Neutral"),
    ("She walked to the store and bought some groceries.", "Neutral"),
    ("The conference will be held in the main hall.", "Neutral"),
]

correct = 0
for i, (sentence, expected) in enumerate(tests, 1):
    result = get_sentiment(sentence)
    predicted_sentiment = result["sentiment"]
    confidence = result["confidence"]
    if predicted_sentiment == expected:
        correct += 1
    print(f"{i:<4} {expected:<12} {predicted_sentiment:<12} {confidence:<8}")

print(f"\nAccuracy: {correct}/12 = {round(correct/12*100, 1)}%")