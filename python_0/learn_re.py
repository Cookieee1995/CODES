# re案例
# 爬取《斗破苍穹》全文小说

import requests,re,time
from bs4 import BeautifulSoup



headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
}

f = open('doupo.txt','a+')

def get_info(url):
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),
                              re.S)
        for content in contents:
            f.write(content+'\n')
            print('ok')
    else:
        pass

if __name__ == '__main__':
    urls = ['http://book.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(1,1665)]
    for url in urls:
        get_info(url)
        time.sleep(1)

f.close()