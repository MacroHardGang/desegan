import requests
import json
import random

# Microsoft Face API Key
SUBSCRIPTION_KEY = "d344c023fa454be4b04928925c3d0d59"
FACE_API_URL = "https://eastus.api.cognitive.microsoft.com/face/v1.0/detect"

''' Retrieve facial descriptions using Microsoft Face API'''
def retrieveFaceDesc(image_url):
    headers = {"Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY}
    params = {
        "returnFaceId": "true",
        "returnFaceLandmarks": "false",
        "returnFaceAttributes": "age,gender,headPose,smile,facialHair,glasses," +
        "emotion,hair,makeup,occlusion,accessories,blur,exposure,noise"
    }
    data = {"url": image_url}
    response = requests.post(FACE_API_URL, params=params, headers=headers, json=data)
    faces = response.json()
    return faces[0]

''' Create description strings '''
def createDescString(description):
    # Gender
    gender = description["faceAttributes"]["gender"] + " "
    # Age
    age = str(int(description["faceAttributes"]["age"])) + " years old "
    # Facial hair
    facial = "" 
    if (description["faceAttributes"]["facialHair"]["moustache"] > 0.3):
        facial = facial + "moustache "
    if (description["faceAttributes"]["facialHair"]["beard"] > 0.3):
        facial = facial + "beard "
    if (description["faceAttributes"]["facialHair"]["sideburns"] > 0.3):
        facial = facial + "sideburns "
    # Glasses
    glasses = ""
    if (description["faceAttributes"]["glasses"] != "NoGlasses"):
        glasses = glasses + "glasses "
    # Hair
    hair = ""
    if (description["faceAttributes"]["hair"]["invisible"]):
        hair = hair + "bald "
    else:
        highest_confidence = 0.0
        color = "black"
        for x in description["faceAttributes"]["hair"]["hairColor"]:
            if (x["confidence"] > highest_confidence):
                color = x["color"]
                highest_confidence = x["confidence"] 
        hair = hair + color + " hair"
    # Create string
    description_string = gender + age + facial + glasses + hair
    return description_string

image_id = 401
data = []
for n in range(1,4):
    image_url = "https://htn.blob.core.windows.net/htn-blob/" + str(n) + ".jpg"
    msft_desc = retrieveFaceDesc(image_url)
    desc_string = createDescString(msft_desc)
    desc = {
            "img_id": image_id,
            "image": image_url,
            "descriptions": [
                {
                    "desc_id": random.randint(1,10000000000),
                    "text": desc_string
                }
            ]
        }
    data.append(desc)
    image_id = image_id + 1
    print("Image #" + str(n) + ": " + desc_string)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)



