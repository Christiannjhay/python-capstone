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


# Sample data
polarity = 0.5
subjectivity = 0.3
toxicity_score = 0.3
compound = 0.2
neg = 0.1

# Define weights for each score
polarity_weight = 0.5
subjectivity_weight = 0.25
toxicity_score_weight = 0.25
compound_weight = 0.25
neg_weight = 0.25

# Define the categorize_combined function
def categorize_combined(polarity, subjectivity, toxicity_score, compound, neg):
    """Categorizes a text based on its polarity, subjectivity, toxicity score, compound score, and negation score.

    Args:
        polarity: A float between -1.0 and 1.0, where -1.0 represents very negative and 1.0 represents very positive.
        subjectivity: A float between 0.0 and 1.0, where 0.0 represents very objective and 1.0 represents very subjective.
        toxicity_score: A float between 0.0 and 1.0, where 0.0 represents very non-toxic and 1.0 represents very toxic.
        compound: A float between -1.0 and 1.0, where -1.0 represents very negative and 1.0 represents very positive.
        neg: A float between 0.0 and 1.0, where 0.0 represents no negation and 1.0 represents strong negation.

    Returns:
        A string representing the final category.
    """

    # Define thresholds for categorization
    positive_threshold = 0.3
    negative_threshold = -0.3
    toxicity_threshold_low = 0.1
    toxicity_threshold_medium = 0.3
    toxicity_threshold_high = 0.5

    # Calculate the weighted average of the scores
    weighted_average = (
        (polarity * polarity_weight)
        + (subjectivity * subjectivity_weight)
        + (toxicity_score * toxicity_score_weight)
        + (compound * compound_weight)
        + (neg * neg_weight)
    )

    # Determine the final category based on the weighted average and thresholds
    if weighted_average >= positive_threshold:
        final_category = "Positive"
    elif weighted_average <= negative_threshold:
        final_category = "Negative"
    elif toxicity_score >= toxicity_threshold_high:
        final_category = "Severe Toxicity"
    elif toxicity_score >= toxicity_threshold_medium:
        final_category = "Threat"
    elif toxicity_score >= toxicity_threshold_low:
        final_category = "Insult"
    else:
        final_category = "Neutral"
    
    print(final_category)
    return final_category

# Call the categorize_combined function
final_category = categorize_combined(polarity, subjectivity, toxicity_score, compound, neg)



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
    app.run(host='0.0.0.0', port=5000, debug=True)
