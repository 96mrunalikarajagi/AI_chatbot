from flask import Flask, request, jsonify, render_template
import json
import random
import pickle
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download("punkt")
nltk.download("wordnet")

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and data
lemmatizer = WordNetLemmatizer()
with open("chatbot_model.pkl", "rb") as file:
    model, vectorizer, responses = pickle.load(file)

def preprocess(text):
    """Tokenize and lemmatize input text."""
    tokens = nltk.word_tokenize(text)
    return " ".join([lemmatizer.lemmatize(token.lower()) for token in tokens])

@app.route("/")
def index():
    """Serve the chatbot interface."""
    return render_template("chatbot.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat messages and generate a response."""
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"response": "I didn't receive any message."})

    # Preprocess the user input
    processed_input = preprocess(user_message)
    X_test = vectorizer.transform([processed_input])
    predicted_tag = model.predict(X_test)[0]

    # Fetch a response from intents

    response = random.choice(responses[predicted_tag])
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

