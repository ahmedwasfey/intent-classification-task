

# Intent Classification Task

This project implements a RESTful API for an intent classification service using Docker. The service classifies user utterances into predefined intents and can identify out-of-scope queries.
*This was a required task for a hiring process.*

## Features

- RESTful API built with Flask
- Uses Hugging Face's pretrained "facebook/bart-large-mnli" model for zero-shot classification
- Dockerized for easy deployment
- Handles out-of-scope queries

## Prerequisites

- Docker

## Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/ahmedwasfey/intent-classification-task.git
   cd intent-classification-task
   ```

2. Build the Docker image:
   ```
   docker build -t intent-classifier .
   ```

3. Run the Docker container:
   ```
   docker run -p 5000:5000 intent-classifier
   ```

The service will be available at `http://localhost:5000`.

## API Usage

### Endpoint

POST `/classify`

### Request Format

```json
{
  "utterance": "What's the weather like today?"
}
```

### Response Format

For a recognized intent:
```
{
  "intent": "query_weather",
  "confidence": 0.85
}
```

For an out-of-scope query:
```
{
  "intent": "out_of_scope",
  "confidence": 0.75
}
```

## Customization

You can customize the intents by modifying the `intents` list in `app.py`:

```
intents = ["greeting", "farewell", "query_weather", "set_alarm", "play_music"]
```

## Technical Details

- The service uses the "facebook/bart-large-mnli" model, which is fine-tuned for zero-shot text classification.
- Flask is used to create the RESTful API.
- The classification threshold for out-of-scope queries is set to 0.3 and can be adjusted in the code.

## Possible Improvements

- Implement caching to improve response times
- Add more comprehensive error handling and logging
- Use a production-ready WSGI server like Gunicorn
- Fine-tune the model on domain-specific data for improved accuracy

## Model usage (testing ) examples 
I have also added [test_notebook.ipynb](test_notebook.ipynb) notebook to show model capabilities on some examples 
```
test_utterances = [
    "Hello there!",
    "Goodbye, see you later!",
    "What's the weather like today?",
    "Set an alarm for 7 AM",
    "Play some jazz music",

    "Calculate the square root of 256",
    "What's the recipe for chocolate chip cookies?",

]
```

### Results 
```
Utterance: 'Hello there!'
Classified as: greeting
Confidence: 0.96

Utterance: 'Goodbye, see you later!'
Classified as: farewell
Confidence: 0.92

Utterance: 'What's the weather like today?'
Classified as: query_weather
Confidence: 0.89

Utterance: 'Set an alarm for 7 AM'
Classified as: set_alarm
Confidence: 0.65

Utterance: 'Play some jazz music'
Classified as: play_music
Confidence: 0.84

Utterance: 'Calculate the square root of 256'
Classified as: out_of_scope
Confidence: 0.70

Utterance: 'What's the recipe for chocolate chip cookies?'
Classified as: out_of_scope
Confidence: 0.70
```

