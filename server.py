# Simple server to handle post request from client 

from flask import Flask, render_template, request, url_for, jsonify, send_file
app = Flask(__name__)

# Test purposes
test_filepath = './test_data/'
test_filename = 'tiff_yhack.png'


# Handles POST request from client

@app.route('/tests/queryModel', methods=['POST']) 

def my_test_endpoint():
    input_json = request.get_json(force=True)
    descr_inst = input_json.get('descriptions')
    print ('Client input:', descr_inst)
    
    ## SEND TO MODEL

    status = {'Data received': 'Success'}
    return jsonify(status)

@app.route('/')
def index():
    return 'Hello Hansen, if you see this you went to address localhost:5000/'

if __name__ == '__main__':
    app.run(debug=True)


