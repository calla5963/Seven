import json
import requests
# from bs4 import BeautifulSoup


def bus_crawler02(msg):
    url = 'https://www.taiwanbus.tw/eBUSPage/Query/ws/getRData.ashx?type=4&key=812902'
    datas = requests.get(url).json()
    msg = msg.replace('02','')
    for data in datas['data']:
        if data['na'] == msg:
            for i in range(1):
                # print(column[0], end=':')
                name = data['na']
                ptime = data['ptime']

    content = ""
    content += f"名稱: {name}\n到站時間還有: {ptime}"

    # print(content)     
    return content

# if __name__ == "__main__":
#     bus_crawler01('內溫泉01')