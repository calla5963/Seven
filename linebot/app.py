from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from eatwhat import *
from load_json1 import *
from load_json2 import *
from get_taitung_weather import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import http.client, json
from urllib.parse import parse_qsl
import requests 
# from flask_sqlalchemy import SQLAlchemy
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('2bW7HyFGu1VsBHo/zwnokAJdwmyW3YWJwaO9b8nhCRgDAABqtWr8fNHNMgAYllInA6oC3HDQllHP5q57GGeSJezjr3eaTwZjL8GpY1kOIq7fG+lC296SBl1ySPPPX3k4de0kBwkiL47afD0MiyTXvgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('68760815a2bc959c25c2b0c480f0b35b')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


host = '26test.azurewebsites.net'  #主機
endpoint_key = "9ba2c3ae-1b50-4b07-b189-be8aae319c96"  #授權碼
kb = "1d68a3d1-4975-4cff-89bf-4ee2bffd5c2f"  #GUID碼
method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5432/NTUHQA'
# db = SQLAlchemy(app)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '美食地圖' in msg:
        try:
            message = eatwhat()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, message='error!')
    #******早餐系列******
    elif '初早餐' in msg:
        try:
            message = eatwhatbreakfast()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, message='error!')
    elif 'brunch' in msg:
        try:
            message = eatwhatbrunch()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, message='error!')
    elif '蘿蔔糕' in msg:
        try:
            line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = 'search for turnipcake',
                contents = json.load(open('json/foodmap/eat_turnipcake.json', 'r', encoding='utf-8'))
            )
        )
        except:
            line_bot_api.reply_message(event.reply_token, message='error!')
    elif '咖啡館' in msg:
        try:
            line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = 'search for coffeeshop',
                contents = json.load(open('json/foodmap/coffeeshop.json', 'r', encoding='utf-8'))
            )
        )
        except:
            line_bot_api.reply_message(event.reply_token, message='error!')
    elif '紅麴飯' in msg:
        try:
            line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = 'search for redyeastrice',
                contents = json.load(open('json/foodmap/eat_redyeastrice.json', 'r', encoding='utf-8'))
            )
        )
        except:
            line_bot_api.reply_message(event.reply_token, message='error!')
    #******早餐系列******
    #******台東天氣系列******
    elif '台東天氣' in msg:
        message = load_taitung_json() 
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = '臺東天氣資訊',
                contents = json.load(open('json/weather/taitung_weather.json', 'r', encoding='utf-8'))
            )
        )
    #******台東天氣系列******
    # elif '@使用說明' in msg:
    #     sendUse(event)
    #******公車查詢系列******
    elif "公車查詢" in msg:
        message = choosedirection()
        line_bot_api.reply_message(event.reply_token, message)
    elif "往森林遊樂區" in msg:
        message = load_json1() 
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = 'search for bus',
                contents = json.load(open('json/bus/bus_container01.json', 'r', encoding='utf-8'))
            )
        )
    elif "往台東轉運站" in msg:
        message = load_json2() 
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = 'search for bus',
                contents = json.load(open('json/bus/bus_container02.json', 'r', encoding='utf-8'))
            )
        )
    #******公車查詢系列******
    #******部落神話小遊戲******
    
    #******部落神話小遊戲******
    #******選課推薦******
    elif "選課推薦" in msg:
        try:
            image_message = ImageSendMessage(
            original_content_url='https://upload.cc/i1/2022/04/20/B4IQms.jpg',
            preview_image_url='https://upload.cc/i1/2022/04/20/B4IQms.jpg'
            )
            line_bot_api.reply_message(event.reply_token, image_message)
        except:
            line_bot_api.reply_message(event.reply_token, message='error!')
    #******選課推薦******
    #******選課推薦呼叫Qna******
    else:
        sendQnA(event, msg)
    #******選課推薦呼叫Qna******


def sendUse(event):  #使用說明
    try:
        text1 ='''
這是台東美食地圖的疑難解答，
請輸入關於美食相關問題。
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendQnA(event, mtext):  #QnA
    question = {
        'question': mtext,
    }
    content = json.dumps(question)
    headers = {
        'Authorization': 'EndpointKey ' + endpoint_key,
        'Content-Type': 'application/json',
        'Content-Length': len(content)
    }
    conn = http.client.HTTPSConnection(host)
    conn.request ("POST", method, content, headers)
    response = conn.getresponse ()
    result = json.loads(response.read())
    result1 = result['answers'][0]['answer']
    if 'No good match' in result1:
        text1 = '很抱歉，資料庫中無適當解答！\n請再輸入問題。'
        try:
            message = TextSendMessage(
                text = '測試中',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action=PostbackAction(label="ptt",data='action=get data'&mtext,text='')
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)  
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='error!'))
        #將沒有解答的問題寫入資料庫
        # userid = event.source.user_id
        # sql_cmd = "insert into users (uid, question) values('" + userid + "', '" + mtext +"');"
        # db.engine.execute(sql_cmd)
    else:
        result2 = result1[2:]  #移除「A：」
        text1 = result2  
    message = TextSendMessage(
        text = text1
    )
    line_bot_api.reply_message(event.reply_token,message)


def choosedirection(): #公車方向
    message = TextSendMessage(
        text='請選擇方向',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='往森林遊樂區',
                        text='往森林遊樂區'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='往台東轉運站',
                        text='往台東轉運站'
                    )
                ),
            ]
        )
    )
    return message

@handler.add(PostbackEvent)
def handle_postback(event):
    backdata = dict(parse_qsl(event.postback.data))
    #******早餐系列******
    if backdata.get('action') == 'breakfast':
        message = get_breakfast()
        line_bot_api.reply_message(event.reply_token, message)
    #早餐店
    elif backdata.get('action') == 'hello早餐店1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for breakfast1',
                    contents = json.load(open('json/foodmap/breakfast_food_card1.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello早餐店2':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for breakfast2',
                    contents = json.load(open('json/foodmap/breakfast_food_card2.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello早餐店3':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for breakfast3',
                    contents = json.load(open('json/foodmap/breakfast_food_card3.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello早餐店4':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for breakfast4',
                    contents = json.load(open('json/foodmap/breakfast_food_card4.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello早午餐店1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for brunch1',
                    contents = json.load(open('json/foodmap/brunch_food_card1.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello早午餐店2':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for brunch2',
                    contents = json.load(open('json/foodmap/brunch_food_card2.json', 'r', encoding='utf-8'))
                )
        )
    #******早餐系列******
    #******午餐、晚餐系列******
    if backdata.get('action') == 'lunch':
        message = get_lunch()
        line_bot_api.reply_message(event.reply_token, message)
    #小吃店
    elif backdata.get('action') == 'eatery':
        message = get_eatery()
        line_bot_api.reply_message(event.reply_token, message)
    elif backdata.get('action') == 'eatery_noodles':
        message = choose_eatery_noodles()
        line_bot_api.reply_message(event.reply_token, message)
    elif backdata.get('action') == 'hello_eatery_noodles1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for eatery_noodles',
                    contents = json.load(open('json/foodmap/eatery_noodles1.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello_eatery_noodles2':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for eatery_noodles',
                    contents = json.load(open('json/foodmap/eatery_noodles2.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'eatery_rice':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for eatery_rice',
                    contents = json.load(open('json/foodmap/eatery_rice.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'eatery_soup':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for eatery_soup',
                    contents = json.load(open('json/foodmap/eatery_soup.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'eatery_eateries':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for eatery_eateries',
                    contents = json.load(open('json/foodmap/eatery_eateries.json', 'r', encoding='utf-8'))
                )
        )
    #素食8
    elif backdata.get('action') == 'vegetarian':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for vegetarian',
                    contents = json.load(open('json/foodmap/vegetarian.json', 'r', encoding='utf-8'))
                )
        )
    #餃子5
    elif backdata.get('action') == 'dumplings':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for dumplings',
                    contents = json.load(open('json/foodmap/dumplings.json', 'r', encoding='utf-8'))
                )
        )
    #包子4
    elif backdata.get('action') == 'bao':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for bao',
                    contents = json.load(open('json/foodmap/bao.json', 'r', encoding='utf-8'))
                )
        )
    #餐館18
    elif backdata.get('action') == 'restaurant':
        message = choose_restaurant()
        line_bot_api.reply_message(event.reply_token, message)
    elif backdata.get('action') == 'hello餐館1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for restaurant',
                    contents = json.load(open('json/foodmap/hello_restaurant1.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello餐館2':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for restaurant',
                    contents = json.load(open('json/foodmap/hello_restaurant2.json', 'r', encoding='utf-8'))
                )
        )
    #原民3
    elif backdata.get('action') == 'aboriginal_restaurant':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for aboriginal_restaurant',
                    contents = json.load(open('json/foodmap/aboriginal_restaurant.json', 'r', encoding='utf-8'))
                )
        )
    #牛肉麵6
    elif backdata.get('action') == 'beefnoodles':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for beefnoodles',
                    contents = json.load(open('json/foodmap/beefnoodles.json', 'r', encoding='utf-8'))
                )
        )
    #披薩2
    elif backdata.get('action') == 'pizza':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for pizza',
                    contents = json.load(open('json/foodmap/pizza.json', 'r', encoding='utf-8'))
                )
        )
    #拉麵7
    elif backdata.get('action') == 'ramen':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for ramen',
                    contents = json.load(open('json/foodmap/ramen.json', 'r', encoding='utf-8'))
                )
        )
    #咖啡館
    elif backdata.get('action') == 'coffeeshop':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for coffeeshop',
                    contents = json.load(open('json/foodmap/coffeeshop.json', 'r', encoding='utf-8'))
                )
        )
    #日式5
    elif backdata.get('action') == 'japanese-style':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for japanese-style',
                    contents = json.load(open('json/foodmap/japanese-style.json', 'r', encoding='utf-8'))
                )
        )
    #韓式10
    elif backdata.get('action') == 'korean-style':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for korean-style',
                    contents = json.load(open('json/foodmap/korean-style.json', 'r', encoding='utf-8'))
                )
        )
    #義式14 italy-style
    elif backdata.get('action') == 'italy-style':
        message = choose_italy_style()
        line_bot_api.reply_message(event.reply_token, message)
    elif backdata.get('action') == 'hello義式餐廳1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for italy-style-restaurant',
                    contents = json.load(open('json/foodmap/italy-style-restaurant1.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello義式餐廳1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for italy-style-restaurant',
                    contents = json.load(open('json/foodmap/italy-style-restaurant2.json', 'r', encoding='utf-8'))
                )
        )
    #泰式2
    elif backdata.get('action') == 'thai-style':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for thai-style',
                    contents = json.load(open('json/foodmap/thai-style.json', 'r', encoding='utf-8'))
                )
        )
    #海鮮6
    elif backdata.get('action') == 'seafood':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for seafood',
                    contents = json.load(open('json/foodmap/seafood.json', 'r', encoding='utf-8'))
                )
        )
    #豬排3
    elif backdata.get('action') == 'pork chop':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for pork chop',
                    contents = json.load(open('json/foodmap/food_porkchop.json', 'r', encoding='utf-8'))
                )
        )
    #牛排7
    elif backdata.get('action') == 'steak':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for steak',
                    contents = json.load(open('json/foodmap/steak.json', 'r', encoding='utf-8'))
                )
        )
    #早午餐
    elif backdata.get('action') == 'brunch':
        message = eatwhatbrunch()
        line_bot_api.reply_message(event.reply_token, message)
    #咖哩4
    elif backdata.get('action') == 'curry':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for curry',
                    contents = json.load(open('json/foodmap/curry.json', 'r', encoding='utf-8'))
                )
        )
    #火鍋21
    elif backdata.get('action') == 'hotpot':
        message = choose_hotpot()
        line_bot_api.reply_message(event.reply_token, message)
    elif backdata.get('action') == 'hello火鍋店1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for hot pot',
                    contents = json.load(open('json/foodmap/hotpot1.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello火鍋店2':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for hot pot',
                    contents = json.load(open('json/foodmap/hotpot2.json', 'r', encoding='utf-8'))
                )
        )
    #便當21
    elif backdata.get('action') == 'bento':
        message = choose_bento()
        line_bot_api.reply_message(event.reply_token, message)
    elif backdata.get('action') == 'hello便當店1':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for bento',
                    contents = json.load(open('json/foodmap/bento1.json', 'r', encoding='utf-8'))
                )
        )
    elif backdata.get('action') == 'hello便當店2':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for bento',
                    contents = json.load(open('json/foodmap/bento2.json', 'r', encoding='utf-8'))
                )
        )
    #晚餐
    if backdata.get('action') == 'dinner':
        message = get_dinner()
        line_bot_api.reply_message(event.reply_token, message)
    #滷味
    elif backdata.get('action') == 'Taiwanesebraiseddish':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for Taiwanesebraiseddish',
                    contents = json.load(open('json/foodmap/Taiwanesebraiseddish.json', 'r', encoding='utf-8'))
                )
        )
    #炸物
    elif backdata.get('action') == 'friedfood':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for friedfood',
                    contents = json.load(open('json/foodmap/friedfood.json', 'r', encoding='utf-8'))
                )
        )
    #燒肉
    elif backdata.get('action') == 'Yakiniku':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for Yakiniku',
                    contents = json.load(open('json/foodmap/Yakiniku.json', 'r', encoding='utf-8'))
                )
        )
    #******午餐、晚餐系列******
    #******宵夜系列******
    if backdata.get('action') == 'late night supper':
        message = get_late_night_supper()
        line_bot_api.reply_message(event.reply_token, message)
    #******宵夜系列******
    #******點心系列******
    if backdata.get('action') == 'dessert':
        message = get_dessert_menu()
        line_bot_api.reply_message(event.reply_token, message)
    #蔥油餅
    elif backdata.get('action') == 'ScallionPancake':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for ScallionPancake',
                    contents = json.load(open('json/foodmap/ScallionPancake.json', 'r', encoding='utf-8'))
                )
        )
    #冰品
    elif backdata.get('action') == 'iceproduct':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for iceproduct',
                    contents = json.load(open('json/foodmap/iceproduct.json', 'r', encoding='utf-8'))
                )
        )
    #肉圓
    elif backdata.get('action') == 'Ba-Wan':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for Ba-Wan',
                    contents = json.load(open('json/foodmap/Ba-Wan.json', 'r', encoding='utf-8'))
                )
        )
    #臭豆腐
    elif backdata.get('action') == 'Stinkytofu':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for Stinkytofu',
                    contents = json.load(open('json/foodmap/Stinkytofu.json', 'r', encoding='utf-8'))
                )
        )
    #春捲
    elif backdata.get('action') == 'EggRoll':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for EggRoll',
                    contents = json.load(open('json/foodmap/EggRoll.json', 'r', encoding='utf-8'))
                )
        )
    #東粄香粿
    elif backdata.get('action') == 'savory_rice_pudding':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for savory_rice_pudding',
                    contents = json.load(open('json/foodmap/savory_rice_pudding.json', 'r', encoding='utf-8'))
                )
        )
    #******點心系列******
    #******飲料系列******
    if backdata.get('action') == 'beverage':
        line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text = 'search for beverage',
                    contents = json.load(open('json/foodmap/beverage.json', 'r', encoding='utf-8'))
                )
        )
    #******飲料系列******
    
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
