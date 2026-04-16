# Sentiment Analysis Mini Project

## 📌 Overview

This project is a simple Sentiment Analysis API built using FastAPI and Hugging Face Transformers.
It accepts text input and classifies it into **Positive, Negative, or Neutral** sentiment.

---

## 🚀 Features

* REST API using FastAPI
* Pre-trained Transformer model (Hugging Face)
* Input validation (empty & non-string input)
* Neutral sentiment handling using confidence threshold
* Tested on multiple sample sentences

---

## 🧠 Tech Stack

* Python
* FastAPI
* Hugging Face Transformers
* Uvicorn

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```
---

## ▶️ Run the Application

```bash
python -m uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST /predict

**Input:**

```
text (string)
```
---

## Input Validation
- Non-string input → 422 error
- Empty string → 400 error

---

## 🧪 Test Cases

The model was tested on 12 sentences:

### Positive

* I absolutely loved this movie, it was fantastic!
* The service was excellent and the staff were so kind.
* What a wonderful day, everything went perfectly!
* This is the best product I have ever purchased.

### Negative

* This is absolutely terrible, I hated every second.
* The food was disgusting and the place was filthy.
* I'm so disappointed, this was a complete waste of money.
* Worst experience of my life, would never recommend.

### Neutral

* The meeting is scheduled for 3pm on Tuesday.
* The report contains twelve pages of data.
* She walked to the store and bought some groceries.
* The conference will be held in the main hall.

---

## 📌 Notes

* The Hugging Face model returns only Positive/Negative
* Neutral sentiment is derived using a confidence score threshold (< 0.7)

---


## 👨‍💻 Author

Vijay Nithin Kumar

