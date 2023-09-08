import requests
import tensorflow as tf
import firebase_admin
from firebase_admin import credentials, firestore
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textblob
import nltk

nltk.download('vader_lexicon')
# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\sugar\\Desktop\\python\\firebase_credentials.json")
firebase_admin.initialize_app(cred)

# Define Perspective API endpoint
PERSPECTIVE_API_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

def analyze_sentiment_and_store(text):
    # Analyze sentiment using VADER sentiment analysis
    vader_analyzer = SentimentIntensityAnalyzer()
    vader_scores = vader_analyzer.polarity_scores(text)
    
    # Create a TextBlob object with the input text
    blob = textblob.TextBlob(text)
    

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
        "text": text,
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
        "comment": {"text": text},
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

    # Add the document to Firestore
    doc_ref = collection.add(document_data)
    print("Sentiment analysis stored successfully.")

if __name__ == "__main__":
    # Input text for sentiment analysis
    input_text = input("Enter text for sentiment analysis: ")

    # Perform sentiment analysis and store the results in Firestore
    analyze_sentiment_and_store(input_text)
