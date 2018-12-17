import json
for type_1 in open('json/m_json.txt','r',encoding='utf-8').readlines():
    string = type_1.replace("'", '"').replace('False','0').replace('True','0')
    # print(json.loads(string)["subjects"])
    title_all,id_all = [],[]
    for m_list in json.loads(string)['subjects']:
        title = m_list['title']
        id = m_list['id']
        title_all.append(title)
        id_all.append(id)
    print(title_all)
    print(id_all)
    print(len(id_all))
    print('#'*30)
