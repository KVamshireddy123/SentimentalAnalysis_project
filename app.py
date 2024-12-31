from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    # Get sentiment polarity
    sentiment_score = blob.sentiment.polarity
    
    # Determine sentiment category
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment

# Example usage
if __name__ == "__main__":
    input_text = input("Enter a text for sentiment analysis: ")
    sentiment_result = analyze_sentiment(input_text)
    print(f"The sentiment of the input text is: {sentiment_result}")
