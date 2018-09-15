# Simple server to handle post request from client 

from flask import Flask, render_template, request, url_for, jsonify, send_file
app = Flask(__name__)

# Test purposes
test_filepath = './test_data/'
test_filename = 'tiff_yhack.png'

# Handles POST request from client
@app.route('/tests/endpoint', methods=['POST'])
def my_test_endpoint():
    input_json = request.get_json(force=True) 
    print ('Client input:', input_json)
    status = {'Data received': 'Success'}
    return send_file(test_filepath + test_filename, mimetype='image/png')

@app.route('/')
def index():
    return 'Good job you went to the landing page wow'

if __name__ == '__main__':
    app.run(debug=True)


