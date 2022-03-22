from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import http.client, json
from flask_sqlalchemy import SQLAlchemy
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('2bW7HyFGu1VsBHo/zwnokAJdwmyW3YWJwaO9b8nhCRgDAABqtWr8fNHNMgAYllInA6oC3HDQllHP5q57GGeSJezjr3eaTwZjL8GpY1kOIq7fG+lC296SBl1ySPPPX3k4de0kBwkiL47afD0MiyTXvgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('68760815a2bc959c25c2b0c480f0b35b')

# QnA Maker
host = '26test.azurewebsites.net'  #主機
endpoint_key = "9ba2c3ae-1b50-4b07-b189-be8aae319c96"  #授權碼
kb = "e22d17ae-e510-47a6-a152-db10e86bb055"  #GUID碼
method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"

# PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5432/ArknightsQA'
db = SQLAlchemy(app)

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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif msg == '@使用說明':
        sendUse(event)
    else:
        sendQnA(event, msg)
    # else:
    #     message = TextSendMessage(text=msg)
    #     line_bot_api.reply_message(event.reply_token, message)

def sendUse(event):  #使用說明
    try:
        text1 ='''
這是明日方舟公招的疑難解答，
請輸入關於公招相關問題。
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
        #將沒有解答的問題寫入資料庫
        userid = event.source.user_id
        sql_cmd = "insert into users (uid, question) values('" + userid + "', '" + mtext +"');"
        db.engine.execute(sql_cmd)
    else:
        result2 = result1[2:]  #移除「A：」
        text1 = result2  
    message = TextSendMessage(
        text = text1
    )
    line_bot_api.reply_message(event.reply_token,message)

@handler.add(PostbackEvent)
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
