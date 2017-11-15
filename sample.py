import requests
import random
import time
# array = [1,2,3,4,5,6,7,7,8]

# r = requests.get("http://weather.livedoor.com/forecast/webservice/json/v1?city=400040")

for i in range(10):
    v = random.randint(0,50)
    r = requests.get("https://dweet.io/dweet/for/fumihumi?count=%s" %v)
    time.sleep(1)
    print(r.json()["with"]["content"]["count"]) 
