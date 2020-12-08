import json
import requests
from urllib.request import urlopen, quote
import pprint

address = quote("长沙")
key = "dajskjda1231390kjbnreitie1043"
url = "http://api.map.baidu.com/geocoder/v2/"
new_url = url + "?address=" + address + "&output=json" + "&ak=" + key
url = "http://restapi.amap.com/v3/geocode/geo"
res = requests.get(new_url)
json_data = json.loads(res.text)

print('经度是：' + str(json_data['result']['location']['lat']))
print('维度是：' + str(json_data['result']['location']['lng']))
