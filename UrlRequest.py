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
            tempList = []
            for i in list :
                print(i[:-9])
                tempList.append(i[:-9])

            resultText = str(tag)
            #print(resultText)
            f = open('result.txt','w')
            f.write(resultText)
        else :
            print("matching element does not exist.")


        #access to div class attr way2
        #divs2 = soup.select('div[class*=forecast]')
        #print(id(divs2))



