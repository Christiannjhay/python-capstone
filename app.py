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

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

nltk.download('vader_lexicon')

print("Current working directory:", os.getcwd())

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

# Define Perspective API endpoint
PERSPECTIVE_API_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

# Define Perspective API endpoint
PERSPECTIVE_API_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"


@app.route('/report', methods=['POST'])
def report_and_store():
    try:
        # Get text data from Chrome extension's POST request
        data = request.json
        input_text = data.get('text', '')

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
       
      
   

        # Add the document to Firestore
        doc_ref = collection.add(document_data)
        return jsonify({"message": "Sentiment analysis stored successfully", "highest_category": highest_category, "underline_decision": underline_decision})
    
        
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/log', methods=['POST'])
def analyze_tweet_and_store():
    try:
        # Get text data from Chrome extension's POST request
        data = request.json
        input_text = data.get('text', '')

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
       
      
   

        # Add the document to Firestore
        doc_ref = collection.add(document_data)
        return jsonify({"message": "Sentiment analysis stored successfully", "highest_category": highest_category, "underline_decision": underline_decision})
    
        
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/analyze', methods=['POST'])
def analyze_drafts_and_store():
    try:
        # Get text data from Chrome extension's POST reque  st
        data = request.json
        input_text = data.get('text', '')

        # Analyze sentiment using VADER sentiment analysis
        vader_analyzer = SentimentIntensityAnalyzer()
        vader_scores = vader_analyzer.polarity_scores(input_text)

        # Create a TextBlob object with the input text
        blob = textblob.TextBlob(input_text)

        # Perform sentiment analysis using TextBlob
        sentiment = blob.sentiment

        # Get the polarity (positive/negative) and subjectivity (objective/subjective) scores
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity

        # Determine sentiment labels based on polarity
        if polarity > 0:
            sentiment_label = "positive"
        elif polarity < 0:
            sentiment_label = "negative"
        else:
            sentiment_label = "neutral"

        # Create a Firestore client
        db = firestore.client()

      

        # Define a collection and document to store the sentiment analysis results
        collection = db.collection("drafts")
        document_data = {
            "text": input_text,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": sentiment_label,
            "vader_scores": vader_scores,
           
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

        sentiment = sentiment_label

        print(highest_category)
         # Get the current date and time
        current_time = datetime.now()
        # Log the category with the highest score as "CATEGORY" in Firestore
        document_data["CATEGORY"] = highest_category
        document_data["TOXCITY_SCORE"] = underline_decision
        document_data["timestamp"] = current_time

        

      
        # Add the document to Firestore
        doc_ref = collection.add(document_data)
        return jsonify({"message": "Sentiment analysis stored successfully", "highest_category": highest_category, "underline_decision": underline_decision})
    
        
    except Exception as e:
        return jsonify({"error": str(e)})
    

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)