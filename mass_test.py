from datetime import datetime
import requests
import firebase_admin
from firebase_admin import credentials, firestore
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textblob
from flask import Flask, request, jsonify
import nltk
from flask_cors import CORS
import os
import numpy as np
import spacy


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

nlp = spacy.load("en_core_web_sm")
nltk.download('vader_lexicon')

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

# Define Perspective API endpoint
PERSPECTIVE_API_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

# Define Perspective API endpoint
PERSPECTIVE_API_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

def detect_double_negation(text):
    doc = nlp(text)
    negative_prefixes = ["un", "in", "im", "ir", "non"]
    negative_verbs = ["disagree", "reject", "refuse", "deny", "fail"]
    negations = [token for token in doc if token.dep_ == 'neg' or 
                 any(token.text.startswith(prefix) for prefix in negative_prefixes) or 
                 any(token.lemma_ == verb for verb in negative_verbs)]
    print(f"Negations in '{text}': {negations}")
    return len(negations) >= 2

@app.route('/analyze', methods=['POST'])
def analyze_drafts_and_store():
    try:

        # Get text data from Chrome extension's POST request
        data = request.json
        input_text = data.get('texts', [])  # Expect a list of texts

       # Detect double negation for the single input
        double_negation_result = detect_double_negation(input_text)
        print("Input Text:", input_text)
        print("Double Negation Result:", double_negation_result)

     
        return jsonify({"message": "Sentiment analysis stored successfully", })
    except Exception as e:
        return jsonify({"error": str(e)})
    

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
