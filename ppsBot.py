from facepy import GraphAPI
import json
import requests
import os

#install facepy module. Use pip install facepy
def downloadFile(url, fileName):
    r = requests.get(url, stream = True)
    try:
        with open(fileName, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)
                    f.flush()
    except:
        fileName = fileName.strip('/')
        with open(fileName, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)
                    f.flush()



groupId = "714685238558448"
#Generate access token here
#https://developers.facebook.com/tools/explorer/
accessToken = "###"

graph = GraphAPI(accessToken)
pages = graph.get(groupId + "/files", page = True, retry = 5, limit = 2000)
counter = 0

os.mkdir('fbPythonGroup')
os.chdir(os.getcwd() + '/fbPythonGroup')

for page in pages:
    for post in page['data']:
        url = post['download_link']
        #fileName is extracted from download url of the following type
        #https://www.facebook.com/download/837214882985735/scipy-ref-0.14.0.pdf
        fileName = url[50:]
        print "fetching " + url
        downloadFile(url, fileName)

