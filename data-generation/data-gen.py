import requests
import json

# Microsoft Face API Key
SUBSCRIPTION_KEY = "d344c023fa454be4b04928925c3d0d59"
FACE_API_URL = "https://eastus.api.cognitive.microsoft.com/face/v1.0/detect"

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
    print(description_string)

desc = retrieveFaceDesc("https://htn.blob.core.windows.net/htn-blob/13234.jpg")
createDescString(desc)



