# Simple server to handle post request from client 

from flask import Flask, render_template, request, url_for, jsonify, send_file
app = Flask(__name__)

# Test purposes
test_filepath = './test_data/'
test_filename = 'tiff_yhack.png'

# Handles POST request from client
@app.route('/tests/endpoint', methods=['POST'])
def myTestEndpoint():
    return "sup"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


