# Simple server to handle post request from client 

from flask import Flask, render_template, request, url_for, jsonify, send_file
from run import generateCriminal

app = Flask(__name__)

# Handles POST request from client
@app.route('/generate-image', methods=['POST']) 
def generateImage():
    description = request.form['description']
    print ('Client input:', description)
    # Send to model
    generated_image_url = generateCriminal(description)
    result = {'image_url': generated_image_url}
    return jsonify(result)

@app.route('/')
def index():
    return 'Test passed.'

if __name__ == '__main__':
    app.run(debug=True)


