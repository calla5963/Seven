import json
import requests

#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================

#往森林遊樂區
def load_json1():
    busstop = ['台東轉運站','台東大學','知本火車站']
    url = 'https://www.taiwanbus.tw/eBUSPage/Query/ws/getRData.ashx?type=4&key=812901'
    datas = requests.get(url).json()
    # msg = msg.replace('01','')
    name = []
    ptime = []
    for data in datas['data']:
        for i in range(3):
            if data['na'] == busstop[i]:
                for j in range(1):
                    name.append(data['na'])
                    ptime.append(data['ptime'])
    print(name)
    print(ptime)

    #台東轉運站、台東大學、知本火車站
    # ['17:00發車', '17:20', '17:32']

    after = []
    with open("json/bus/bus_container01.json","r", encoding='utf-8') as f:
        data = json.load(f)
        Right_time1 = ptime[0] #台東轉運站
        Right_time2 = ptime[1] #台東大學
        Right_time3 = ptime[2] ##知本火車站

        print(data['body']['contents'][1]['contents'][0]['text']) #台東轉運站
        data['body']['contents'][1]['contents'][0]['text'] = Right_time1

        print(data['body']['contents'][3]['contents'][0]['contents'][0]['text']) #台東大學
        data['body']['contents'][3]['contents'][0]['contents'][0]['text'] = Right_time2

        print(data['body']['contents'][5]['contents'][0]['text']) #知本火車站
        data['body']['contents'][5]['contents'][0]['text'] = Right_time3
        
        after = data 

    with open('json/bus/bus_container01.json','w', encoding='utf-8') as f:
        #結構化輸出
        data = json.dump(after,f,ensure_ascii=False,indent=3)