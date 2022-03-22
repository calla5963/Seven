#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

# *****程式

def eatwhat(): #11項
    message = TextSendMessage(
        text='請選擇想吃的食物',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='牛肉麵',
                        text='@牛肉麵'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='雞肉飯',
                        text='@雞肉飯'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='臭豆腐',
                        text='@臭豆腐'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='蔥油餅',
                        text='@蔥油餅'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='包子',
                        text='@包子'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='日式',
                        text='@日式'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='韓式',
                        text='@韓式'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='義式',
                        text='@義式'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='早餐店',
                        text='@早餐店'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='早午餐',
                        text='@早午餐'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='牛排',
                        text='@牛排'
                    )
                ),
            ]
        )
    )
    return message

def chickenrice():
    message = TextSendMessage(
        text='請選擇想吃的食物',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='俊彥牌雞肉飯',
                        text='@俊彥牌雞肉飯'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='俊彥會噴水雞肉飯',
                        text='@俊彥會噴水雞肉飯'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='俊彥愛與和平火雞肉飯',
                        text='@俊彥愛與和平火雞肉飯'
                    )
                ),
            ]
        )
    )
    return message