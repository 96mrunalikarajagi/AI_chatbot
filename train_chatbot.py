import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('punkt')
nltk.download('wordnet')
import os
import json
import os
print("Current working directory:", os.getcwd())





# Print intents to verify it's loaded correctly (for debugging)
#print("Loaded intents:", intents)
file_path = "C:/Users/aishw/OneDrive/Desktop/django3/Flask-1/intents.json"
with open(file_path, "r") as file:
    intents = json.load(file)


print("Current working directory:", os.getcwd())

# Example: Use the intents for training your chatbot
for intent in intents["intents"]:
    print(f"Tag: {intent['tag']}")
    print(f"Patterns: {intent['patterns']}")
    print(f"Responses: {intent['responses']}")


# Load intents

lemmatizer = WordNetLemmatizer()

# Prepare training data
patterns = []
tags = []
responses = {}
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

# Tokenize and lemmatize
def preprocess(text):
    tokens = nltk.word_tokenize(text)
    return " ".join([lemmatizer.lemmatize(token.lower()) for token in tokens])

patterns = [preprocess(p) for p in patterns]

# Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)
y = tags

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X, y)

# Save the model and vectorizer
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer, responses), f)
