fromfrom textblob  import  TextBlob


def analyze_sentiment(statement):
    blob = TextBlob(statement)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Neutral"

text = "I love this product! It's amazing!"
print("Sentiment:", analyze_sentiment(text)) 
