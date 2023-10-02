import requests
import firebase_admin
from firebase_admin import credentials, firestore
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textblob
from flask import Flask, request, jsonify
import nltk
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

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

# Sample data
polarity = 0.5  # Replace with the actual polarity value
subjectivity = 0.3  # Replace with the actual subjectivity value
toxicity_score = 0.3  # Replace with the actual toxicity_score value
compound = 0.2  # Replace with the actual compound value
neg = 0.1  # Replace with the actual negation value

# Define the categorize_combined function
def categorize_combined(polarity, subjectivity, toxicity_score, compound, neg):
    # Define a threshold for categorization
    threshold = 0.2  # Adjust this threshold as needed

    # Determine the final category based on scores and thresholds
    if polarity >= threshold and toxicity_score < threshold:
        final_category = "Positive"
    elif polarity < -threshold and toxicity_score < threshold:
        final_category = "Negative"
    else:
        # Check for other categories based on toxicity_score
        if toxicity_score >= threshold:
            if toxicity_score >= 0.6:
                final_category = "Severe Toxicity"
            elif toxicity_score >= 0.4:
                final_category = "Threat"
            elif toxicity_score >= 0.3:
                final_category = "Profanity"
            elif toxicity_score >= 0.2:
                final_category = "Sexually Explicit"
            else:
                final_category = "Insult"
        else:
            final_category = "Neutral"

    return final_category

# Categorize the sample data
category = categorize_combined(polarity, subjectivity, toxicity_score, compound, neg)
print(f"Category: {category}")



@app.route('/analyze', methods=['POST'])
def analyze_sentiment_and_store():
    try:
        # Get text data from Chrome extension's POST request
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
        collection = db.collection("sentiment")
        document_data = {
            "text": input_text,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": sentiment_label,
            "vader_scores": vader_scores
        }

        # Analyze text using Perspective API for toxicity
        perspective_params = {
            "key": "AIzaSyAjsgnyRwOG7iYUlgtK48CXT_y6o6u6DTA",  # Replace with your actual API key
        }

        perspective_data = {
            "comment": {"text": input_text},
            "languages": ["en"],
            "requestedAttributes": {"TOXICITY": {}}
        }

        response = requests.post(PERSPECTIVE_API_URL, params=perspective_params, json=perspective_data)

        # Check if the request was successful
        if response.status_code == 200:
            perspective_score = response.json()["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
        else:
            print(f"An error occurred: {response.status_code}")
            perspective_score = None

        # Add the toxicity_score to the document data
        document_data["toxicity_score"] = perspective_score

        # Calculate the final category using categorize_combined function
        final_category = categorize_combined(polarity, subjectivity, perspective_score, vader_scores['compound'], vader_scores['neg'])
        document_data["final_category"] = final_category

        # Add the document to Firestore
        doc_ref = collection.add(document_data)
        return jsonify({"message": "Sentiment analysis stored successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
