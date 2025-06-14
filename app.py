# app.py

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from llava.llava_api import LlavaInference
import time

app = Flask(__name__, static_folder='static')
CORS(app)  # Allow cross-origin requests (adjust as needed)

inference_instances = {}  # Cache for loaded models


@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    prompt = request.form.get('prompt', 'Describe the image.')
    temperature = float(request.form.get('temperature', 0.2))
    conv_mode = request.form.get('conv_mode', 'qwen_2')
    model_path = request.form.get('model_path', './weights/llava-fastvithd_0.5b_stage3')

    if model_path not in inference_instances:
        try:
            inference_instances[model_path] = LlavaInference(model_path)
        except Exception as e:
            return jsonify({'error': f'Failed to load model: {e}'}), 500

    analyzer = inference_instances[model_path]

    start = time.time()
    try:
        result, image_size = analyzer.analyze(image.read(), prompt, temperature, conv_mode)
    except Exception as e:
        return jsonify({'error': f'Inference error: {e}'}), 500

    elapsed = round(time.time() - start, 2)
    return jsonify({
        'output': result,
        'process_time': elapsed,
        'image_size': f'{image_size[0]}x{image_size[1]}',
        'token_count': len(result.split()),
        'confidence': int(90 + temperature * 10)  # Simulated confidence
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
