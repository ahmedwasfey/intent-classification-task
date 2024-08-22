

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
