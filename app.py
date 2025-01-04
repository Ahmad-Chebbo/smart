import logging
from flask import Flask, request, jsonify
from transformers import pipeline, set_seed

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the model with better parameters
enhance_prompt_model = pipeline(
    "text-generation",
    model="gpt2",
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    max_length=100,
    num_return_sequences=1
)

# Set seed for reproducibility
set_seed(42)

# Load the text generation pipeline with GPT-2 (no API key required)
# enhance_prompt_model = pipeline("text-generation", model="gpt2")

@app.route('/')
def hello_world():
    return "Hello, From Smart LLM!"

@app.route('/enhance_prompt', methods=['POST'])
def enhance_prompt():
    """
    Enhance the given text prompt with additional details and improved phrasing.
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify(error="Missing 'prompt' in request body"), 400

        prompt = data['prompt']
        max_length = int(data.get('max_length', 100))  # Default to 100 if not provided

        # Generate enhanced prompt
        enhanced = enhance_prompt_model(prompt, max_length=max_length, num_return_sequences=1)
        enhanced_text = enhanced[0]['generated_text']

        logging.info(f"Original prompt: {prompt}")
        logging.info(f"Enhanced prompt: {enhanced_text}")

        # Return the enhanced prompt
        return jsonify(original_prompt=prompt, enhanced_prompt=enhanced_text), 200

    except Exception as e:
        logging.error(f"Error enhancing prompt: {str(e)}")
        return jsonify(error="Failed to enhance prompt"), 500
