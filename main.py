from textblob import TextBlob

def analyze_sentiment():
    print("--- AI Sentiment Analyzer ---")
    print("Type 'exit' to stop.")
    
    while True:
        text = input("\nEnter text to analyze: ")
        
        if text.lower() == 'exit':
            break
            
        # AI Logic
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0:
            result = "Positive 😊"
        elif polarity == 0:
            result = "Neutral 😐"
        else:
            result = "Negative ☹️"
            
        print(f"Sentiment Result: {result} (Score: {round(polarity, 2)})")

if __name__ == "__main__":
    analyze_sentiment()