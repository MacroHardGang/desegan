# Simple server to handle post request from client 

from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)

# Handles POST request from client
@app.route('/tests/endpoint', methods=['POST'])
def my_test_endpoint():
    input_json = request.get_json(force=True) 
    print ('Client input:', input_json)
    status = {'Data received': 'Success'}
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True)


