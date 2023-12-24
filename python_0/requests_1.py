import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
}
url = 'https://www.baidu.com/'

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

# print(res)
# print(res.text)
print(soup.prettify())
