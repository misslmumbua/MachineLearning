from flask import Flask, request, jsonify, render_template
import pickle, re

# Load trained model and vectorizer
model, vectorizer = pickle.load(open("model.pkl", "rb")), pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("review", "").strip()

    if not review:
        return jsonify({"error": "No review provided"}), 400

    transformed_review = vectorizer.transform([re.sub(r'[^\w\s]', '', review.lower())])
    prediction = model.predict(transformed_review)[0]
    confidence = max(model.predict_proba(transformed_review)[0]) * 100

    return jsonify({"sentiment": "Positive" if prediction == 1 else "Negative", "confidence": f"{confidence:.2f}%"})

app.run(host="0.0.0.0", port=5000)




