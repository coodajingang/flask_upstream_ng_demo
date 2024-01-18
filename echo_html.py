from flask import Blueprint,render_template, make_response

echohtml = Blueprint('echo_html', __name__)


@echohtml.route("/echo_html")
def echo_html(): 
    return render_template('file_upload.html')

@echohtml.route("/echo_html/hello")
def echo_html_hello(): 
    return make_response('asdfasdf')