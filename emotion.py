from textblob import TextBlob

emotions = {
    "happy": ["happy", "joy", "glad", "delighted", "awesome"],
    "sad": ["sad", "unhappy", "depressed", "cry", "bad"],
    "angry": ["angry", "furious", "mad", "irritated", "annoyed"],
    "fear": ["scared", "afraid", "fear", "terrified", "nervous"]
}

text = input("Enter text: ").lower()
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

detected = None
for emo, words in emotions.items():
    if any(w in text for w in words):
        detected = emo
        break

if detected:
    print(f"Detected Emotion: {detected.capitalize()} 🧡")
elif sentiment > 0:
    print("Detected Emotion: Happy 😊")
elif sentiment < 0:
    print("Detected Emotion: Sad 😞")
else:
    print("Detected Emotion: Neutral 😐")
