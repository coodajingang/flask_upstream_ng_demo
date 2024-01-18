
from datetime import datetime, timedelta
from flask import Blueprint, make_response
from flask import Flask, jsonify, request
from tools import json_headers, html_headers
from log import configure_logger

logger = configure_logger()

echo = Blueprint('echo_json', __name__)

@echo.route("/echo-json-with-nocache")
def echo_json_with_nocache(): 
    data = json_headers(request) 
    res = make_response(jsonify(data))
    return res

@echo.route("/echo-json-with-cache")
def echo_json_with_cache(): 
    data = json_headers(request) 
    res = make_response(jsonify(data))
    res.headers['ETag'] = 'etage1223'
    res.headers['Last-Modified'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    res.headers['Cache-Control'] = 'public, max-age=60' 
    return res

# exp=60 pub=true vary= etag= modified= conn=keep-alive/close
@echo.route("/echo-json")
def echo_json(): 
    logger.info('Access echo  json !')
    exp = None; pub=None; vary=None; etag=None; modified=None; 
    if_none_match = request.headers.get('If-None-Match')
    if_modified_since = request.headers.get('If-Modified-Since')
    
    if if_none_match and if_none_match == str('echo-json1234'):
        print(f'Have etag = {if_none_match}, check...')
        response = make_response("", 304)
        response.headers['Etag'] = 'echo-json1234'
        print('echo 304')
        return response

    if if_modified_since:
        modified_since = datetime.strptime(if_modified_since, "%a, %d %b %Y %H:%M:%S %Z")
        expires_time = datetime.now() + timedelta(seconds=600*-1)
        print(f'Have if_modified_since = {modified_since}, check...')
        if modified_since >= expires_time:
            response = make_response("", 304)
            response.headers['Etag'] = 'echo-json1234'
            print('echo 304')
            return response
    if request.method == 'GET': 
        exp = request.args.get('exp')
        pub = request.args.get('pub')
        vary = request.args.get('vary')
        etag = request.args.get('etag')
        modified = request.args.get('modified')
        conn = request.args.get('conn')
    elif request.method == 'POST': 
        exp = request.form.get('exp')
        pub = request.form.get('pub')
        vary = request.form.get('vary')
        etag = request.form.get('etag')
        modified = request.form.get('modified')
        conn = request.form.get('conn')
    
    data = json_headers(request) 
    res = make_response(jsonify(data))

    ispublic = 'private'
    if pub is not None and pub == 'true': 
        ispublic = 'public'

    if exp is not None and exp.isnumeric():
        res.headers['Cache-Control'] = f'{ispublic}, max-age={exp}'
        current_time = datetime.now()
        expires_time = current_time + timedelta(seconds=int(exp))
        res.headers['Expires'] = expires_time.strftime('%a, %d %b %Y %H:%M:%S %Z')
    else: 
        res.headers['Cache-Control'] = f'{ispublic}' 
    if vary is not None: 
        res.headers['Vary'] = vary
    if etag is not None:
        res.headers['ETag'] = etag
    if modified is not None: 
        current_time = datetime.now()
        expires_time = current_time + timedelta(seconds=int(modified)*-1)
        res.headers['Last-Modified'] = expires_time.strftime("%a, %d %b %Y %H:%M:%S %Z")

    if conn is not None: 
        res.headers['Connection'] = f'{conn}'
    
    return res