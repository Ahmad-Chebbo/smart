# Smart Prompt Enhancer

A simple Flask-based API that uses GPT-2 to enhance and expand text prompts. This application provides a basic prompt enhancement service without requiring any external API keys.

## Features

- Text prompt enhancement using GPT-2
- RESTful API endpoint
- Configurable prompt length
- Error handling and logging

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:

2. Install the required dependencies:

3. Run the application:

4. Access the API endpoint:

## Usage

1. Start the server:

2. Send a POST request to the `/enhance_prompt` endpoint with a JSON body containing the original prompt.

```bash
curl -X POST http://localhost:5000/enhance_prompt -H "Content-Type: application/json" -d '{"prompt": "A beautiful sunset over a calm ocean.", "max_length": 100}'
```

3. The API will return a JSON response with the enhanced prompt.


## Model Configuration

The application uses GPT-2 with the following parameters:
- Temperature: 0.7
- Top-k: 50
- Top-p: 0.95
- Maximum length: 100 (default)
- Number of return sequences: 1

## Error Handling

The API includes basic error handling for:
- Missing prompt in request
- Invalid request format
- Server-side processing errors

## Limitations

- Uses the basic GPT-2 model, which has limited capabilities compared to more advanced models
- No streaming responses
- Limited prompt length
- Basic prompt enhancement without fine-tuning

## License

[MIT License](LICENSE)

## Contributing

Feel free to submit issues and enhancement requests!

## Disclaimer

This is a basic implementation meant for educational purposes. For production use, consider using more robust models and adding additional security measures.
