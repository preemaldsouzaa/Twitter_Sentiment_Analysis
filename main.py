import nltk
nltk.download("stopwords")
from flask import Flask, render_template, request, jsonify
import pickle
from utils import preprocess_text, preprocess  

tfidf_ = pickle.load(open(r'C:\Users\LENOVO\ML Algorithms\Twitter Sentiment Analysis\my_flask_app\venv\tfidf_instance.pkl', 'rb'))
model = pickle.load(open(r'C:\Users\LENOVO\ML Algorithms\Twitter Sentiment Analysis\my_flask_app\venv\logistic_regression.pkl', 'rb'))
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("twitter.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    tweet = request.form.get("tweet", "")

    # Preprocess the user input
    preprocessed_tweet = preprocess_text(tweet)
    preprocessed_tweet = preprocess(preprocessed_tweet)
    preprocessed_tweet = tfidf_.transform([preprocessed_tweet])  # Note: pass as a list

    # Make predictions using the model
    sentiment = model.predict(preprocessed_tweet)[0]

    # Map numerical label to sentiment
    sentiment_map = {0: "Neutral", 1: "Positive", 2: "Negative"}
    result = sentiment_map[sentiment]

    # Return the sentiment as JSON
    return jsonify(sentiment=result)

if __name__ == "__main__":
    app.run(debug=True)
