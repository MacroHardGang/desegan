import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

ROOT_DIR = 'images'
ACCOUNT_NAME = 'htn'
ACCOUNT_KEY = 'Wa6X+0mdj74FBEPczVimdRzj6Z7KDsUHKPckyP0UdGWpZRjbJuERLR8T/JJIpNBOxZA+Q+5aSmx1xYM/HmTLqQ=='
CONTAINER_NAME = 'htn-blob'

def uploadImage(n):
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)
        # Upload file
        print("Uploading Image #" + str(n))
        block_blob_service.create_blob_from_path(CONTAINER_NAME, str(n) + '.jpg', 'images/'+ str(n) +'.jpg')
    except Exception as e:
        print(e)

for n in range(1,13248):
    uploadImage(n)
