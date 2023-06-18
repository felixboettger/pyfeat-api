from flask import Flask, render_template, request
from face_processor_2 import get_detection
import tempfile
import os
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/test/au_api')
def test_au_api():
    return render_template("test_au_api.html")

@app.route('/api/image_to_au', methods=['POST'])
def api_image_to_au():
    print(request.files)
    filestorage_image = request.files['image']
    with tempfile.NamedTemporaryFile(delete=True, suffix=os.path.splitext(filestorage_image.filename)[1]) as temp_file:
        filestorage_image.save(temp_file.name)
        print(temp_file.name)
        detection = get_detection(temp_file.name)

    return detection


if __name__ == '__main__':
    app.run(debug=True, port=5000, ssl_context='adhoc')