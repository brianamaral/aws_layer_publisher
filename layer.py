import os
import zipfile
import subprocess
import sys
import boto3

PATH = 'python/lib/python3.8/site-packages'

os.makedirs(PATH,exist_ok=True)

#os.chdir(path=PATH)

subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests','-t',PATH])

def zip_folders(file: str) -> None:
    with zipfile.ZipFile(file,'w') as zip:
        for root,dirs,files in os.walk('python'):
            for filename in files:
                file_path = os.path.join(root,filename)
                zip.write(file_path)

zip_folders('python.zip')

client_aws = boto3.client('lambda',region_name='us-east-1',aws_access_key_id='',aws_secret_access_key='')

with open('python.zip','rb') as zip:
    file = zip.read()  

client_aws.publish_layer_version(
    LayerName='layer_novo',
    Description='lorem ipsum',
    Content={
        'ZipFile': file
    },
    CompatibleRuntimes=[
        'python3.6','python3.7','python3.8'
    ],
    LicenseInfo='string'
)
