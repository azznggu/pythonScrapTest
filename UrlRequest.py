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
        #print(soup)
        soupText = str(soup.encode('utf-8'))

        #access to div class attr way1
        tag = soup.findAll('ul',{'id':'exchangeList'})
        if len(tag) :
            count = 3
            blind = str(soup.find_all('span',{'class':'blind'}))
            value = str(soup.find_all('span',{'class':'value'}))
            list = value.split('<span class="value">')
            resultList = []
            for i in list :
                #print(i[:-9])
                resultList.append(i[:-9])
             
            resultText = str(tag)
            f = open('result.txt','w')
            f.write(resultText)
            return resultList
        else :
            print("matching element does not exist.")
            return resultList
