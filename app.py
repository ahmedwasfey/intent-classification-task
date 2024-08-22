from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define your intents
intents = ["greeting", "farewell", "query_weather", "set_alarm", "play_music"]

@app.route('/classify', methods=['POST'])
def classify_intent():
    data = request.json
    utterance = data.get('utterance')
    
    if not utterance:
        return jsonify({"error": "No utterance provided"}), 400
    
    # Perform classification
    result = classifier(utterance, intents)
    
    # Get the highest scoring intent
    top_intent = result['labels'][0]
    top_score = result['scores'][0]
    
    # Check if the top score is below a threshold to identify out-of-scope queries
    if top_score < 0.3:  # You can adjust this threshold
        response = {
            "intent": "out_of_scope",
            "confidence": 1 - top_score
        }
    else:
        response = {
            "intent": top_intent,
            "confidence": top_score
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)