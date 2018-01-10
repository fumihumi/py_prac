# import http.client, urllib.request, urllib.parse, urllib.error, base64, json, os
import urllib.request, json, requests
subscription_key = ""
hostUrl = "https://westus.api.cognitive.microsoft.com/qnamaker/v2.0"
path =  "/knowledgebases/d7a01245-302e-44a2-8956-c2b7cabab0e7/generateAnswer"
headers = {
    'Content-Type' : 'application/json',
    'Ocp-Apim-Subscription-Key' : subscription_key
}
body = {
    "question" : "hi"
}
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}
url = hostUrl + path
r = requests.post(url, data=json.dumps(body), headers=headers)
print(r.json()['answers'][0])
