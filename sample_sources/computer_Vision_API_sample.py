
########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json, os

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = ''
# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    # 'Content-Type': 'application/json',
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Adult',
    'language': 'en',
})
# def  analyze(url):
def analyze(image): 
    # Replace the three dots below with the URL of a JPEG image of a celebrity.
    # body = "{'url':'http://www.yokohamajapan.com/about/img/02_Minato-mirai.jpg'}"
    # body = "{'url' : '%s'}" % (url)
    # python３系では '%s'より.formatを利用することが多いようだが、カーリブラケットがネストするのでこちらで対応

    body = image
    try:
        # Execute the REST API call and get the response.
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        # print (json.dumps(parsed, sort_keys=True, indent=2))

        conn.close()
        # return json.dumps(parsed['description']['tags'],sort_keys=True, indent=2)
        # json の中の['description']['tags']を取得し整形する？w
        return json.dumps(parsed , sort_keys=True , indent= 2)
    except Exception as e:
        print('Error:')
        print(e)

####################################


# text = analyze("")
# text = analyze("http://kai-you.net/images/a/2016/10/f186e00d4e30087ad76b44ae7023d06b.jpg")

# print(os.getcwd()) 
# os command 'pwd'を擬似的に操作し、カレントワーキングディレクトリを表示する

image = open("sample.jpg", "br")
 # sample jpgを読み込む
text = analyze(image)
print(text)