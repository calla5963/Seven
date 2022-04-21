import requests
import json

#取得json檔裡的資料並替代卡片中的資料
def load_taitung_json():
  url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-027?Authorization=CWB-6C68397A-8921-4160-8CAF-31A738F4416F&downloadType=WEB&format=JSON'
  datas = requests.get(url).json()     # 取得 JSON 檔案的內容為文字 and 轉換成 JSON 格式

  today_taitung_weather = []
  for i in range(3):
    today_taitung_weather.append(datas['cwbopendata']['dataset']['parameterSet']['parameter'][i]['parameterValue'])
  a = today_taitung_weather[0]
  b = today_taitung_weather[1]
  c = today_taitung_weather[2]

  after = []
  with open("json/weather/taitung_weather.json","r", encoding='utf-8') as f:
    data = json.load(f)
    data['body']['contents'][1]['text'] = a
    data['body']['contents'][2]['text'] = b
    data['body']['contents'][3]['text'] = c
    
    after = data 

  with open('json/weather/taitung_weather.json','w', encoding='utf-8') as f:
    #結構化輸出
    data = json.dump(after,f,ensure_ascii=False,indent=3)