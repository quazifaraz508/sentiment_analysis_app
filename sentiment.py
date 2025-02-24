import streamlit as st
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK resources
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Streamlit App
st.title("Sentiment Analysis App")
st.write("Analyze the sentiment of your text (Positive, Negative, or Neutral).")

# User Input
text_input = st.text_area("Enter text for sentiment analysis:")

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Get polarity score from TextBlob
    
    sentiment_scores = sia.polarity_scores(text)  # Get sentiment scores from VADER
    compound_score = sentiment_scores['compound']

    # Determine sentiment based on compound score
    if compound_score >= 0.05:
        sentiment = "Positive 😀"
    elif compound_score <= -0.05:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    return sentiment, polarity, compound_score

# Display sentiment analysis result
if st.button("Analyze Sentiment"):
    if text_input.strip():
        sentiment, polarity, compound = analyze_sentiment(text_input)
        
        st.subheader("Sentiment Result:")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Polarity Score:** {polarity:.2f}")
        st.write(f"**Compound Score (VADER):** {compound:.2f}")
    else:
        st.warning("Please enter some text to analyze.")
