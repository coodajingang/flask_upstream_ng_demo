
import datetime

from flask import jsonify


def json_headers(request):
    unidata = {}
    headers = dict(request.headers)
    unidata['request_line'] = request_line(request)
    unidata['reqeust_headers'] = headers;
    unidata['rsp_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    return unidata;

def html_headers(request):
    headers = f"<h2>{request_line(request)}</h2>"
    headers += f"<h2>Request headers: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h2>"
    headers += "<ul>"
    for key, value in request.headers.items():
        headers += f"<li><strong>{key}:</strong> {value}</li>"
    headers += "</ul>"
    
    return headers

def request_line(request): 
    request_line = f"Method: {request.method}, Path: {request.path}, Protocol: {request.environ['SERVER_PROTOCOL']}"
    return request_line