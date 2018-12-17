import requests
url = 'https://movie.douban.com/j/search_subjects'
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'bid=HYDCYFr8owY; douban-fav-remind=1; viewed="2201479"; ap_v=0,6.0; ll="108303"; ps=y; dbcl2="175318921:N0n6NKPm9ZI"; ck=kbmZ; push_noty_num=0; push_doumail_num=0; ct=y',
    'DNT':'1',
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com/explore',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}
m_list = open('m_json.txt','w',encoding='utf-8')
type = ['动作','喜剧','爱情','科幻','悬疑','恐怖','成长']
for type_1 in type:
    para = {
        'type':'movie',
        'tag':type_1,
        'sort':'recommend',
        'page_limit':'20',
        'page_start':'0',
    }
    html = requests.get(url,params=para,headers=headers)
    # 显示正常中文字符
    m_list.write(str(html.json()))
    print('{}done'.format(type_1))
m_list.close()
# 总结：应该使用json dumps进行存储json格式


