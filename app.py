from flask import Flask, jsonify, make_response, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

SWAGGER_URL = '/docs'
API_URL = '/static/api.yml'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'API docs'})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/')
def index():
    return 'mdating server'

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5002, debug=False)
