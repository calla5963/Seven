import os
import json

from bus_crawler01 import *
from bus_crawler02 import *
from linebot.models import *
from load_json1 import *
from load_json2 import *

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from flask import Flask, request, abort, render_template

app = Flask(__name__)

Channel_Access_Token = '2bW7HyFGu1VsBHo/zwnokAJdwmyW3YWJwaO9b8nhCRgDAABqtWr8fNHNMgAYllInA6oC3HDQllHP5q57GGeSJezjr3eaTwZjL8GpY1kOIq7fG+lC296SBl1ySPPPX3k4de0kBwkiL47afD0MiyTXvgdB04t89/1O/w1cDnyilFU='
line_bot_api    = LineBotApi(Channel_Access_Token)
Channel_Secret  = '68760815a2bc959c25c2b0c480f0b35b'
handler = WebhookHandler(Channel_Secret)


# handle request from "/callback" 
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body      = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# handle text message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if "公車查詢" in msg:
        message = choosedirection()
        line_bot_api.reply_message(event.reply_token, message)
    elif "往森林遊樂區" in msg:
        message = load_json1() 
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = 'search for bus',
                contents = json.load(open('save_bus01.json', 'r', encoding='utf-8'))
            )
        )
    elif "往台東轉運站" in msg:
        message = load_json2() 
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = 'search for bus',
                contents = json.load(open('save_bus02.json', 'r', encoding='utf-8'))
            )
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=msg)
        )

def choosedirection():
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


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
