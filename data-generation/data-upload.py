import os
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

ROOT_DIR = 'images'
ACCOUNT_NAME = 'htn'
ACCOUNT_KEY = 'Wa6X+0mdj74FBEPczVimdRzj6Z7KDsUHKPckyP0UdGWpZRjbJuERLR8T/JJIpNBOxZA+Q+5aSmx1xYM/HmTLqQ=='
CONTAINER_NAME = 'htn-blob'

try:
    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)

    # Upload file
    block_blob_service.create_blob_from_path(CONTAINER_NAME, '1.jpg', 'images/1.jpg')

except Exception as e:
    print(e)


# n = 1
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         f = os.path.join(subdir, file)
#         os.rename(f, "image-new/"+ str(n) +".jpg")
#         n = n + 1
#         print(f)