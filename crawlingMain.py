from bs4 import BeautifulSoup
import time
from UrlRequest import UrlRequest

def main() :
    req = UrlRequest()
    #request get html and find specific content in every 5seconds
    url ='https://finance.naver.com/marketindex/'
    flag = True
    counter = 0
    #while flag :
    result = req.get_html(url)
    if result :
        req.get_content(result)
        #time.sleep(3)


main()


