# sentiment-analysis-mini-project
Sentiment Analysis API using FastAPI and Hugging Face

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

## 🧪 Test Cases

The model was tested on 12 sentences:

### Positive

* I love this product
* This is amazing and works perfectly
* I am very happy with the results
* Excellent service and quality

### Negative

* I hate this item
* This is the worst experience ever
* Very bad quality and disappointing
* I am extremely unhappy with this

### Neutral

* The product arrived yesterday
* It is a phone with a 6-inch display
* The meeting is scheduled for tomorrow
* This is a table

---

## 📌 Notes

* The Hugging Face model returns only Positive/Negative
* Neutral sentiment is derived using a confidence score threshold (< 0.6)

---


## 👨‍💻 Author

Vijay Nithin Kumar

