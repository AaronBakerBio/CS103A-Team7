from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OPENAI_API_KEY = 'your-api-key'

def get_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }
    data = {
        'prompt': prompt,
        'temperature': 0.5,
        'max_tokens': 100,
        'top_p': 1,
        'frequency_penalty': 0,
        'presence_penalty': 0,
    }
    api_endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    response = requests.post(api_endpoint, headers=headers, json=data)
    return response.json()['choices'][0]['text']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response_from_api():
    prompt = request.form['prompt']
    response = get_response(prompt)
    return response

if __name__ == '__main__':
    app.run(debug=True)
