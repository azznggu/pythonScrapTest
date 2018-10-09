import json
import urllib.request

j1 = {'a':'aa','b':'bb','c':30}
print(j1)


j = json.dumps(j1)
print(j)


with open("C:/Users/JONGPARK/Source/Repos/pythonTest/test.json") as f :
    data = json.load(f)

print(type(data))

url = "http://www.google.com"
data