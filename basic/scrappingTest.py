#request test
#link: http://docs.python-requests.org/en/master/user/quickstart/

import requests
from bs4 import BeautifulSoup


payload = {'key1':'value1','key2':'value2'}
#r = requests.get('https://api.github.com/events', payload)
#print(r)
#check text of response
#print(r.text)

#r = requests.post('https://httpbin.org/post', data = {'key':'value'})
#print(r)

#check url of response
#print(r.url)
#print(r.content)

#JSON Response Content
#print(r.json())

#Raw Response Content
#r = requests.get('https://api.github.com/events', stream=True)
#print(r.raw)
#print(r.raw.read(10))

#with open("C:/Users/JONGPARK/Source/Repos/pythonTest/test.txt", 'wb') as f:
#    for chunk in r.iter_content(chunk_size = 128):
#        f.write(chunk)

# request method
def get_html(url):
    url_head = url[:4]
    if url_head != "http":
        print("check url format.")
        return ""

    html = ""
    r = requests.get(url)
    if r.status_code == 200 :
        html = r.text
        print()
    else :
        print("result does not exist.")
    return html



#request get html and find specific content in every 5seconds
import time
url ='https://weather.yahoo.co.jp/weather/jp/13/4410.html'
#url = input("enter url to request :")
flag = True
counter = 0
while flag :
    result = get_html(url)
    if result :
        counter+=1
        soup = BeautifulSoup(result,'html.parser')
        print(soup)
        soupText = str(soup.encode('utf-8'))
        f = open('result.txt','w')
        f.write(soupText)

        #access to div class attr way1
        divs = soup.findAll('div',{'class':'forecastCity'})
        print(id(divs))

        #access to div class attr way2
        divs2 = soup.select('div[class*=forecast]')
        print(id(divs2))
        time.sleep(10)








