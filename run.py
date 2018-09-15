from azure.storage.blob import BlockBlobService, PublicAccess
import random

ACCOUNT_NAME = 'htn'
ACCOUNT_KEY = 'Wa6X+0mdj74FBEPczVimdRzj6Z7KDsUHKPckyP0UdGWpZRjbJuERLR8T/JJIpNBOxZA+Q+5aSmx1xYM/HmTLqQ=='
CONTAINER_NAME = 'generated-images'
IMAGE_LOCAL_URL = 'data-generation/images/1.jpg'

''' Queries the model which generate a photo and saves it to the output folder'''
def queryModel(description):
    # Run model
    print("Running model")

''' Uploads the image to blob storage '''
def uploadImage():
    uuid = str(random.randint(1,100000000))
    try:
        block_blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)
        block_blob_service.create_blob_from_path(CONTAINER_NAME, uuid + '.jpg', IMAGE_LOCAL_URL)
    except Exception as e:
        print(e)
    url = 'https://htn.blob.core.windows.net/generated-images/' + uuid + '.jpg'
    print("Image uploaded to "+ url)
    return url

''' Generates the potential look of the criminal '''
def generateCriminal(description):
    queryModel(description)
    image_url = uploadImage()
    return image_url
