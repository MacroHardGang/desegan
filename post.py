#make a POST request
import requests
import urllib.request as urllib2
import base64
import json

req = {
        "descriptions": [
            {
                "text": "male 34 years old brown hair",
                "desc_id": 4071370886
            }
        ],
        "image": "https://htn.blob.core.windows.net/htn-blob/1.jpg",
        "img_id": 401
    }
res = requests.post('http://localhost:5000/tests/queryModel', json=req)

print ('response from server:',res.text)
