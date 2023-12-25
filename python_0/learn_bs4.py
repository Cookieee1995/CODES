# BeautifulSoup
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
}

url = 'http://book.doupoxs.com/doupocangqiong/1.html'
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

title1 = soup.find('div','entry-tit')
title2 = soup.select('div > div > h1')

print(title2)

# print(type(soup))
#
# print(title1.text)
# print(type(title1))
# print(soup.prettify())