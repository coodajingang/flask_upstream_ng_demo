from flask import Flask, render_template, request, redirect, url_for, Blueprint, current_app, send_from_directory
import os

file = Blueprint('file', __name__)

@file.route('/upload', methods=['GET'])
def upload_page(): 
    return render_template('file_upload.html')


@file.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    print(f"Upload dir = {current_app.config.get('UPLOAD_FOLDER')}")
    if file:
        filename = os.path.join(current_app.config.get('UPLOAD_FOLDER'), file.filename)
        file.save(filename)
        return 'File uploaded successfully'

@file.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(current_app.config.get('UPLOAD_FOLDER'), filename, as_attachment=True)


# send_from_directory 会自动为文件资源添加etag 、last-modified 、cache-control等头部 
@file.route('/preview/<filename>')
def preview_file(filename):
    return send_from_directory(current_app.config.get('UPLOAD_FOLDER'), filename, mimetype='text/plain', as_attachment=False)

'''
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.9.9
Date: Wed, 17 Jan 2024 09:36:24 GMT
Content-Disposition: inline; filename=test1.txt
Content-Type: text/plain; charset=utf-8
Content-Length: 14
Last-Modified: Wed, 17 Jan 2024 09:36:08 GMT
Cache-Control: no-cache
ETag: "1705484168.1634119-14-3871153982"
Date: Wed, 17 Jan 2024 09:36:24 GMT
Custom-Header: Custom Header Value
Set-Cookie: custom-cookie=12345; Path=/
Connection: close
'''


