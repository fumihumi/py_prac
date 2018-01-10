import urllib.request, json, requests

def zip2address(zipcode):
    hostUrl = "http://zipcloud.ibsnet.co.jp/api/search"
    headers = {
        'Content-Type' : 'application/json',
    }
    payload = {'zipcode': zipcode}
    r = requests.get(hostUrl, params = payload).text
    print(r)
    return r

zip2address(2534353)