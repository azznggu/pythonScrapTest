import requests
from bs4 import BeautifulSoup
import time

class UrlRequest:

# request method
    def get_html(self, url):
        url_head = url[:4]
        if url_head != "http":
            print("please check url format.")
            return ""
        html = ""
        r = requests.get(url)
        if r.status_code == 200 :
             html = r.text
        else :
            print("result does not exist.")
        return html

    def get_content(self, html):
        soup = BeautifulSoup(html,'html.parser')
        print(soup)
        soupText = str(soup.encode('utf-8'))
        f = open('result.txt','w')
        f.write(soupText)

        #access to div class attr way1
        divs = soup.findAll('div',{'class':'forecastCity'})
        print(id(divs))

        #access to div class attr way2
        #divs2 = soup.select('div[class*=forecast]')
        #print(id(divs2))



