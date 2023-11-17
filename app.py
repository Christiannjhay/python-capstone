from datetime import datetime
import requests
import firebase_admin
from firebase_admin import credentials, firestore
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
from textblob import TextBlob
from explicit_terms import explicit_medical_terms
from flask import Flask, request, jsonify
import nltk
from flask_cors import CORS
import os
import numpy as np

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

nltk.download('vader_lexicon')
nlp = spacy.load("en_core_web_sm")


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
                 (token.text.lower() in negative_prefixes and token.text.lower() != "a") or
                 any(token.lemma_.lower() == verb for verb in negative_verbs)]
    
    print(f"Negations in '{text}': {negations}")
    return len(negations) >= 2

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def match_and_analyze(text):
    matched_terms = [term for term, definition in explicit_medical_terms.items() if term in text.lower()]
    sentiment_label = analyze_sentiment(text)
    return matched_terms, sentiment_label

@app.route('/report', methods=['POST'])
def report_and_store():
    try:
        # Get text data from Chrome extension's POST request
        data = request.json
        input_text = data.get('text', '')

         # Match Medical terms
        sample_text = input_text
        matched_terms, sentiment_label = match_and_analyze(sample_text)
        if bool(matched_terms) and sentiment_label in ['Positive', 'Neutral']:
            medical_term = True
        else: 
            medical_term = False

        double_negation_result = detect_double_negation(input_text)
        print("Input Text:", input_text)
        print("Double Negation Result:", double_negation_result)

        # Create a Firestore client
        db = firestore.client()

        # Define a collection and document to store the sentiment analysis results
        collection = db.collection("reports")
        document_data = {
            "text": input_text,
           
        }

        # Analyze text using Perspective API for toxicity
        perspective_params = {
            "key": "AIzaSyAjsgnyRwOG7iYUlgtK48CXT_y6o6u6DTA",  # Replace with your actual API key
        }

        perspective_data = {
            "comment": {"text": input_text},
            "languages": ["en"],
            "requestedAttributes": {
                "TOXICITY": {}, 
                "SEVERE_TOXICITY": {},
                "INSULT": {},
                "SEXUALLY_EXPLICIT": {},
                "PROFANITY": {},
                "LIKELY_TO_REJECT": {},
                "THREAT": {},
               
            }
        }

        response = requests.post(PERSPECTIVE_API_URL, params=perspective_params, json=perspective_data)

        # Check if the request was successful
        if response.status_code == 200:
            
            toxicity_score = response.json()["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
            severe_toxic_score = response.json()["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]
            insult_score = response.json()["attributeScores"]["INSULT"]["summaryScore"]["value"]
            sexually_explicit_score = response.json()["attributeScores"]["SEXUALLY_EXPLICIT"]["summaryScore"]["value"]
            profanity_score = response.json()["attributeScores"]["PROFANITY"]["summaryScore"]["value"]
            threat_score = response.json()["attributeScores"]["THREAT"]["summaryScore"]["value"]
            
        
        # Add the toxicity_score to the document data
        category_scores = {

            "Severe Toxicity": severe_toxic_score,
            "Threat": threat_score,
            "Insult": insult_score,
            "Sexually Explicit": sexually_explicit_score,
            "Profanity": profanity_score,
            
            
        }


        # Get the category with the highest score
        underline_decision = toxicity_score

        highest_category = max(category_scores, key=category_scores.get)

        print(highest_category)

        # Get the current date and time
        current_time = datetime.now()

        # Log the category with the highest score as "CATEGORY" in Firestore
        document_data["category"] = highest_category
        document_data["TOXCITY_SCORE"] = underline_decision
        document_data["timestamp"] = current_time

        if(medical_term):
            underline_decision = 0.0
        if(double_negation_result):
            underline_decision = 0.0
            
        # Add the document to Firestore
        doc_ref = collection.add(document_data)
        return jsonify({"message": "Sentiment analysis stored successfully", "highest_category": highest_category, 
                        "double_negation_result":double_negation_result,"underline_decision": underline_decision,
                        "medical_term": medical_term, "sentiment_label": sentiment_label})
          
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/log', methods=['POST'])
def analyze_tweet_and_store():
    try:
        # Get text data from Chrome extension's POST request
        data = request.json
        input_text = data.get('text', '')

        # Match Medical terms
        sample_text = input_text
        matched_terms, sentiment_label = match_and_analyze(sample_text)
        if bool(matched_terms) and sentiment_label in ['Positive', 'Neutral']:
            medical_term = True
        else: 
            medical_term = False

         # Detect double negation for the single input
        double_negation_result = detect_double_negation(input_text)
        print("Input Text:", input_text)
        print("Double Negation Result:", double_negation_result)
    
        # Create a Firestore client
        db = firestore.client()

        # Define a collection and document to store the sentiment analysis results
        collection = db.collection("tweets")
        document_data = {
            "text": input_text,
           
        }

        # Analyze text using Perspective API for toxicity
        perspective_params = {
            "key": "AIzaSyAjsgnyRwOG7iYUlgtK48CXT_y6o6u6DTA",  # Replace with your actual API key
        }

        perspective_data = {
            "comment": {"text": input_text},
            "languages": ["en"],
            "requestedAttributes": {
                "TOXICITY": {}, 
                "SEVERE_TOXICITY": {},
                "INSULT": {},
                "SEXUALLY_EXPLICIT": {},
                "PROFANITY": {},
                "LIKELY_TO_REJECT": {},
                "THREAT": {},
               
            }
        }

        response = requests.post(PERSPECTIVE_API_URL, params=perspective_params, json=perspective_data)

        # Check if the request was successful
        if response.status_code == 200:
            
            toxicity_score = response.json()["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
            severe_toxic_score = response.json()["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]
            insult_score = response.json()["attributeScores"]["INSULT"]["summaryScore"]["value"]
            sexually_explicit_score = response.json()["attributeScores"]["SEXUALLY_EXPLICIT"]["summaryScore"]["value"]
            profanity_score = response.json()["attributeScores"]["PROFANITY"]["summaryScore"]["value"]
            threat_score = response.json()["attributeScores"]["THREAT"]["summaryScore"]["value"]
            
        
        # Add the toxicity_score to the document data
        category_scores = {

            "Severe Toxicity": severe_toxic_score,
            "Threat": threat_score,
            "Insult": insult_score,
            "Sexually Explicit": sexually_explicit_score,
            "Profanity": profanity_score,
            
            
        }


        # Get the category with the highest score
        underline_decision = toxicity_score

        highest_category = max(category_scores, key=category_scores.get)

        print(highest_category)

        # Get the current date and time
        current_time = datetime.now()

        # Log the category with the highest score as "CATEGORY" in Firestore
        document_data["category"] = highest_category
        document_data["TOXCITY_SCORE"] = underline_decision
        document_data["timestamp"] = current_time
       
        if(medical_term):
            underline_decision = 0.0
        if(double_negation_result):
            underline_decision = 0.0
   

        # Add the document to Firestore
        doc_ref = collection.add(document_data)
        return jsonify({"message": "Sentiment analysis stored successfully", "highest_category": highest_category, "underline_decision": underline_decision,
                        "double_negation_result":double_negation_result, "medical_term": medical_term})
    
        
    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/analyze', methods=['POST'])
def analyze_drafts_and_store():
    try:
        # Get text data from Chrome extension's POST reque  st
        data = request.json
        input_text = data.get('text', '')

         # Match Medical terms
        sample_text = input_text
        matched_terms, sentiment_label = match_and_analyze(sample_text)
        if bool(matched_terms) and sentiment_label in ['Positive', 'Neutral']:
            medical_term = True
        else: 
            medical_term = False
        
       # Detect double negation for the single input
        double_negation_result = detect_double_negation(input_text)
        print("Input Text:", input_text)
        print("Double Negation Result:", double_negation_result)

        # Create a Firestore client
        db = firestore.client()

        # Define a collection and document to store the sentiment analysis results
        collection = db.collection("drafts")
        document_data = {
            "text": input_text,
        }

        # Analyze text using Perspective API for toxicity
        perspective_params = {
            "key": "AIzaSyAjsgnyRwOG7iYUlgtK48CXT_y6o6u6DTA",  # Replace with your actual API key
        }

        perspective_data = {
            "comment": {"text": input_text},
            "languages": ["en"],
            "requestedAttributes": {
                "TOXICITY": {}, 
                "SEVERE_TOXICITY": {},
                "INSULT": {},
                "SEXUALLY_EXPLICIT": {},
                "PROFANITY": {},
                "LIKELY_TO_REJECT": {},
                "THREAT": {},
               
            }
        }

        response = requests.post(PERSPECTIVE_API_URL, params=perspective_params, json=perspective_data)

        # Check if the request was successful
        if response.status_code == 200:
            
            toxicity_score = response.json()["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
            severe_toxic_score = response.json()["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]
            insult_score = response.json()["attributeScores"]["INSULT"]["summaryScore"]["value"]
            sexually_explicit_score = response.json()["attributeScores"]["SEXUALLY_EXPLICIT"]["summaryScore"]["value"]
            profanity_score = response.json()["attributeScores"]["PROFANITY"]["summaryScore"]["value"]
            threat_score = response.json()["attributeScores"]["THREAT"]["summaryScore"]["value"]
            

        # Add the toxicity_score to the document data
        category_scores = {
            
            "Severe Toxicity": severe_toxic_score,
            "Threat": threat_score,
            "Insult": insult_score,
            "Sexually Explicit": sexually_explicit_score,
            "Profanity": profanity_score,
            
        }


        # Get the category with the highest score
        
        underline_decision = toxicity_score


        highest_category = max(category_scores, key=category_scores.get)

        print(double_negation_result)

        print(highest_category)
         # Get the current date and time
        current_time = datetime.now()
        # Log the category with the highest score as "CATEGORY" in Firestore
        document_data["CATEGORY"] = highest_category
        document_data["TOXCITY_SCORE"] = underline_decision
        document_data["timestamp"] = current_time

        
        if(medical_term):
            underline_decision = 0.0
        if(double_negation_result):
            underline_decision = 0.0
        
      
        # Add the document to Firestore
        doc_ref = collection.add(document_data)
        return jsonify({"message": "Sentiment analysis stored successfully", "highest_category": highest_category, "underline_decision": underline_decision,
                        "double_negation_result":double_negation_result, "medical_term": medical_term,
                        "sentiment_label": sentiment_label})
    
        
    except Exception as e:
        return jsonify({"error": str(e)})


    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)