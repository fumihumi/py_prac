# coding utf-8
import pprint
import requests

def main():
    #GETパラメータはparams引数に辞書で指定する
    url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/eece4c63-cbce-4eb5-a955-466739984503?subscription-key=8a894be66aa34146af5062cb7921f931&spellCheck=true&verbose=true&timezoneOffset=0&q="
    payload = "今日の天気は？"
    response = requests.get(
        url + payload)
    #レスポンスオブジェクトのjsonメソッドを使うと、
    #JSONデータをPythonの辞書オブジェクトを変換して取得できる。
    print(response.json())
    data = response.json()
    intents = data["intents"]
    result = sorted(intents, key=lambda e: e["score"])
    print(result)

if __name__== '__main__':
    main()


