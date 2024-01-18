import requests
from flask import Flask, jsonify, request
from tools import json_headers, html_headers
from echo_json import echo;
from echo_html import echohtml;
from files import file;
from log import configure_logger

logger = configure_logger();

app = Flask(__name__)

@app.after_request
def add_custom_header(response):
    # 在每个响应后都会执行这个函数，可以在这里添加头部信息
    response.headers['Custom-Header'] = 'Custom Header Value'
    response.set_cookie('custom-cookie', '12345')
    return response

@app.route("/")
def index():
    return """
    <h1>ECHO with python flask!</h1>
    <p>A sample web-app for running Flask inside Docker.</p>
    """ + html_headers(request)

@app.route("/rest")
def rest():
    return jsonify(json_headers(request));


app.register_blueprint(echo)
app.register_blueprint(echohtml)
app.register_blueprint(file)

app.config['UPLOAD_FOLDER'] = 'uploads'

logger.info('App start!')
logger.warn('App start')
logger.error('App start')
logger.debug('App start')

if __name__ == '__main__': 
    print('Start flask web')
    app.run(host='0.0.0.0', port=8801, debug=True)
