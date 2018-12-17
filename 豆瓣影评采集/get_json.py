import time
import requests
import json
import math
from bs4 import BeautifulSoup
import re
import lxml.html
etree = lxml.html.etree
from tomorrow import threads
urls = [
    'https://movie.douban.com/subject/20435622/comments',
]
# urls = urls*5
#多线程版本
print(urls)
data = {
    'start':'20',
    'limit':'20',
    'sort':'new_score',
    'status':'P',
    'percent_type':'l',
    'comments_only':'0',
}
# print('*'*100)
# @threads(100)
def download(url):
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'bid=HYDCYFr8owY; douban-fav-remind=1; viewed="2201479"; ap_v=0,6.0; ll="108303"; ps=y; dbcl2="175318921:N0n6NKPm9ZI"; ck=kbmZ; push_noty_num=0; push_doumail_num=0; ct=y',
            'DNT': '1',
            'Host': 'movie.douban.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        return requests.get(url,headers=headers,params=data,timeout=0.7)
    except:
        pass
start = time.time()
responses = [download(url) for url in urls]
# hasattr判断其中的属性，使用循环和判断进行输出
html = [response for response in responses if hasattr(response,"text")]
for i in html:
    print(i.url)
    json_all = i.text
    etree_text = etree.HTML(json_all)
    number_text = etree_text.xpath('.//li[@class="is-active"]/span/text()')
    number = re.findall(r"\d+\.?\d*", number_text[0])
    print(number)
    # 使用向上取整
    print(math.ceil(int(number[0])/20+1))



