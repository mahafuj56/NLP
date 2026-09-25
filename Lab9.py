import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required VADER resource
nltk.download('vader_lexicon')

# Create VADER analyzer
sia = SentimentIntensityAnalyzer()

# Input text
text = input("Enter a text: ")

# Analyze sentiment
scores = sia.polarity_scores(text)

# Display scores
print("\nSentiment Scores:")
print(scores)

# Determine sentiment
if scores['compound'] >= 0.05:
    sentiment = "Positive"
elif scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Display result
print("Sentiment:", sentiment)