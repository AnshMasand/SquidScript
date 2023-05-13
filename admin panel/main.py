from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/configure', methods=['POST'])
def configure_proxy():
    config = request.form.get('config')
    target_url = request.form.get('target_url')
    response = requests.post(f'http://{target_url}/configure', data={'config': config})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)