#make a POST request
import requests

text = 'he looks like a pinus'

# Do some things

req = {'description':text}
res = requests.post('http://localhost:5000/tests/endpoint', json=req)
print ('response from server:',res.text)

# Response from server
dictFromServer = res.json()