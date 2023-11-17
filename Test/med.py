from textblob import TextBlob
from explicit_terms import explicit_medical_terms

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

# Match Medical terms
sample_text = "Fuck you"
matched_terms, sentiment_label = match_and_analyze(sample_text)

# Print "True" if there are matched terms, otherwise print "False"
print("Matched Terms:", bool(matched_terms))
print("Sentiment Label:", sentiment_label)

if bool(matched_terms) and sentiment_label in ['Positive', 'Neutral']:
    toxicity = 0.0

print(toxicity)
