#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from cgitb import text
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


# **吃什麼 大選項大分類
def eatwhat(): #11項
    message = TemplateSendMessage(
        alt_text='想吃什麼。･ﾟ･(つд`ﾟ)･ﾟ･',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/3184183/pexels-photo-3184183.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='幾點吃ヽ(￣■￣)ゝ',
                    text='好餓(◕ H ◕)',
                    actions=[
                        PostbackTemplateAction(
                            label='早餐',
                            data='action=breakfast'
                        ),
                        PostbackTemplateAction(
                            label='午餐',
                            data='action=lunch'
                        ),
                        PostbackTemplateAction(
                            label='晚餐',
                            data='action=dinner'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/2725744/pexels-photo-2725744.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='嘴饞ヾ(*´∀ ˋ*)ﾉ',
                    text='吃飽沒◑ω◐',
                    actions=[
                        PostbackTemplateAction(
                            label='宵夜',
                            data='action=late night supper'
                        ),
                        PostbackTemplateAction(
                            label='點心',
                            data='action=dessert'
                        ),
                        PostbackTemplateAction(
                            label='飲料',
                            data='action=beverage'
                        )
                    ]
                )
            ]
        )
    )
    return message

#早餐選擇
def get_breakfast():
    message = TextSendMessage(
        text='(ゝ∀･)想要吃什麼早餐?',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='只想初早餐',
                        text='初早餐'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='早午餐',
                        text='brunch'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='蘿蔔糕',
                        text='蘿蔔糕'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='咖啡館',
                        text='咖啡館'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='紅麴飯',
                        text='紅麴飯'
                    )
                ),
            ]
        )
    )
    return message

# 選早餐店
def eatwhatbreakfast():
    message = TemplateSendMessage(
        alt_text='請選擇早餐店',
        template=ButtonsTemplate(
            text='請選擇早餐店',
            actions=[
                PostbackTemplateAction(
                    label='早餐店清單1',
                    data='action=hello早餐店1'
                ),
                PostbackTemplateAction(
                    label='早餐店清單2',
                    data='action=hello早餐店2'
                ),
                PostbackTemplateAction(
                    label='早餐店清單3',
                    data='action=hello早餐店3'
                ),
                PostbackTemplateAction(
                    label='早餐店清單4',
                    data='action=hello早餐店4'
                )
            ]
        )
    )
    return message

#請選擇早午餐
def eatwhatbrunch():
    message = TemplateSendMessage(
        alt_text='早午餐店',
        template=ButtonsTemplate(
            text='請選擇早午餐',
            actions=[
                PostbackTemplateAction(
                    label='早午餐店清單1',
                    data='action=hello早午餐店1'
                ),
                PostbackTemplateAction(
                    label='早午餐店清單2',
                    data='action=hello早午餐店2'
                ),
            ]
        )
    )
    return message

#午餐選擇
def get_lunch(): #21項
    message = TemplateSendMessage(
        alt_text='想吃什麼。･ﾟ･(つд`ﾟ)･ﾟ･',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/960856/pexels-photo-960856.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='隨便吃ヽ(￣■￣)ゝ',
                    text='( Φ ω Φ )',
                    actions=[
                        PostbackTemplateAction(
                            label='小吃店',
                            data='action=eatery'
                        ),
                        PostbackTemplateAction(
                            label='素食',
                            data='action=vegetarian'
                        ),
                        PostbackTemplateAction(
                            label='餃子',
                            data='action=dumplings'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/1310777/pexels-photo-1310777.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='荷包君難受(=´ω`=)',
                    text='(=´ᴥ`)',
                    actions=[
                        PostbackTemplateAction(
                            label='包子',
                            data='action=bao'
                        ),
                        PostbackTemplateAction(
                            label='餐館',
                            data='action=restaurant'
                        ),
                        PostbackTemplateAction(
                            label='原住民風味餐廳',
                            data='action=aboriginal_restaurant'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/2664216/pexels-photo-2664216.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='麵團之亂',
                    text='(o･e･)',
                    actions=[
                        PostbackTemplateAction(
                            label='牛肉麵',
                            data='action=beefnoodles'
                        ),
                        PostbackTemplateAction(
                            label='披薩',
                            data='action=pizza'
                        ),
                        PostbackTemplateAction(
                            label='拉麵',
                            data='action=ramen'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/3968061/pexels-photo-3968061.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
                    title='午後時光',
                    text='(•ө•)',
                    actions=[
                        PostbackTemplateAction(
                            label='咖啡館',
                            data='action=coffeeshop'
                        ),
                        PostbackTemplateAction(
                            label='日式',
                            data='action=japanese-style'
                        ),
                        PostbackTemplateAction(
                            label='韓式',
                            data='action=korean-style'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/699953/pexels-photo-699953.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='多重味覺的饗宴',
                    text='(❍ᴥ❍ʋ)',
                    actions=[
                        PostbackTemplateAction(
                            label='義式',
                            data='action=italy-style'
                        ),
                        PostbackTemplateAction(
                            label='泰式',
                            data='action=thai-style'
                        ),
                        PostbackTemplateAction(
                            label='海鮮',
                            data='action=seafood'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/109395/pexels-photo-109395.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='滋滋作響的餐點ヾ(*´∀ ˋ*)ﾉ',
                    text='(･8･)',
                    actions=[
                        PostbackTemplateAction(
                            label='豬排',
                            data='action=pork chop'
                        ),
                        PostbackTemplateAction(
                            label='牛排',
                            data='action=steak'
                        ),
                        PostbackTemplateAction(
                            label='早午餐',
                            data='action=brunch'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/954677/pexels-photo-954677.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='(つ´ω`)つ溫暖你心',
                    text='ก็ʕ•͡ᴥ•ʔ ก้',
                    actions=[
                        PostbackTemplateAction(
                            label='咖哩',
                            data='action=curry'
                        ),
                        PostbackTemplateAction(
                            label='火鍋',
                            data='action=hotpot'
                        ),
                        PostbackTemplateAction(
                            label='便當',
                            data='action=bento'
                        )
                    ]
                )
            ]
        )
    )
    return message

# 選擇小吃店
def get_eatery():
    message = TemplateSendMessage(
        alt_text='請選擇小吃店',
        template=ButtonsTemplate(
            text='4種讓你選',
            actions=[
                PostbackTemplateAction(
                    label='麵類',
                    data='action=eatery_noodles'
                ),
                PostbackTemplateAction(
                    label='飯類',
                    data='action=eatery_rice'
                ),
                PostbackTemplateAction(
                    label='湯類',
                    data='action=eatery_soup'
                ),
                PostbackTemplateAction(
                    label='小吃店(都有)',
                    data='action=eatery_eateries'
                )
            ]
        )
    )
    return message

#選擇麵類的小吃店
def choose_eatery_noodles():
    message = TemplateSendMessage(
        alt_text='請選擇麵類的小吃店',
        template=ButtonsTemplate(
            text='吃麵麵囉',
            actions=[
                PostbackTemplateAction(
                    label='麵類的小吃店清單1',
                    data='action=hello_eatery_noodles1'
                ),
                PostbackTemplateAction(
                    label='麵類的小吃店清單2',
                    data='action=hello_eatery_noodles2'
                ),
            ]
        )
    )
    return message

#選擇餐廳
def choose_restaurant():
    message = TemplateSendMessage(
        alt_text='請選擇餐館',
        template=ButtonsTemplate(
            text='請選擇餐館',
            actions=[
                PostbackTemplateAction(
                    label='餐館清單1',
                    data='action=hello餐館1'
                ),
                PostbackTemplateAction(
                    label='餐館清單2',
                    data='action=hello餐館2'
                ),
            ]
        )
    )
    return message

#選擇義式
def choose_italy_style():
    message = TemplateSendMessage(
        alt_text='請選擇義式餐廳',
        template=ButtonsTemplate(
            text='請選擇義式餐廳',
            actions=[
                PostbackTemplateAction(
                    label='請選擇義式餐廳清單1',
                    data='action=hello義式餐廳1'
                ),
                PostbackTemplateAction(
                    label='請選擇義式餐廳清單2',
                    data='action=hello義式餐廳2'
                ),
            ]
        )
    )
    return message

#選擇火鍋店
def choose_hotpot():
    message = TemplateSendMessage(
        alt_text='請選擇火鍋店',
        template=ButtonsTemplate(
            text='請選擇火鍋店',
            actions=[
                PostbackTemplateAction(
                    label='火鍋店清單1',
                    data='action=hello火鍋店1'
                ),
                PostbackTemplateAction(
                    label='火鍋店清單2',
                    data='action=hello火鍋店2'
                ),
            ]
        )
    )
    return message

#選擇便當店
def choose_bento():
    message = TemplateSendMessage(
        alt_text='請選擇便當店',
        template=ButtonsTemplate(
            text='請選擇便當店',
            actions=[
                PostbackTemplateAction(
                    label='便當店清單1',
                    data='action=hello便當店1'
                ),
                PostbackTemplateAction(
                    label='便當店清單2',
                    data='action=hello便當店2'
                ),
            ]
        )
    )
    return message

#晚餐選擇
def get_dinner(): #23項
    message = TemplateSendMessage(
        alt_text='想吃什麼。･ﾟ･(つд`ﾟ)･ﾟ･',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://images.unsplash.com/photo-1602273660127-a0000560a4c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8amFwYW5lc2UlMjBmb29kfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
                    title='又要吃飯了!',
                    text='(๑•̀ㅂ•́)و✧',
                    actions=[
                        PostbackTemplateAction(
                            label='便當',
                            data='action=bento'
                        ),
                        PostbackTemplateAction(
                            label='拉麵',
                            data='action=ramen'
                        ),
                        PostbackTemplateAction(
                            label='餃子',
                            data='action=dumplings'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/8148149/pexels-photo-8148149.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
                    title='辛香料的對決',
                    text='σ(´∀｀*)',
                    actions=[
                        PostbackTemplateAction(
                            label='牛肉麵',
                            data='action=beefnoodles'
                        ),
                        PostbackTemplateAction(
                            label='小吃店',
                            data='action=eatery'
                        ),
                        PostbackTemplateAction(
                            label='咖哩',
                            data='action=curry'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/8914623/pexels-photo-8914623.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='一起吃飯吧!',
                    text='(♛‿♛)',
                    actions=[
                        PostbackTemplateAction(
                            label='日式',
                            data='action=japanese-style'
                        ),
                        PostbackTemplateAction(
                            label='韓式',
                            data='action=korean-style'
                        ),
                        PostbackTemplateAction(
                            label='義式',
                            data='action=italy-style'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/1731535/pexels-photo-1731535.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='好香、好濃、好純',
                    text='(΄◞ิ౪◟ิ‵)',
                    actions=[
                        PostbackTemplateAction(
                            label='泰式',
                            data='action=thai-style'
                        ),
                        PostbackTemplateAction(
                            label='餐館',
                            data='action=restaurant'
                        ),
                        PostbackTemplateAction(
                            label='火鍋',
                            data='action=hotpot'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://image.shutterstock.com/image-photo/taiwan-night-food-market-raohe-600w-1929320525.jpg',
                    title='想吃什麼自己拿',
                    text='(❁´ω`❁)*✲ﾟ*',
                    actions=[
                        PostbackTemplateAction(
                            label='滷味',
                            data='action=Taiwanesebraiseddish'
                        ),
                        PostbackTemplateAction(
                            label='素食',
                            data='action=vegetarian'
                        ),
                        PostbackTemplateAction(
                            label='炸物',
                            data='action=friedfood'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/2233730/pexels-photo-2233730.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='友愛提醒:記得吃蔬菜喔',
                    text='(◍•ᴗ•◍)ゝ',
                    actions=[
                        PostbackTemplateAction(
                            label='燒肉',
                            data='action=Yakiniku'
                        ),
                        PostbackTemplateAction(
                            label='原住民風味餐廳',
                            data='action=aboriginal_restaurant'
                        ),
                        PostbackTemplateAction(
                            label='披薩',
                            data='action=pizza'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/5672398/pexels-photo-5672398.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
                    title='大俠愛吃han包包',
                    text='(▰˘◡˘▰)',
                    actions=[
                        PostbackTemplateAction(
                            label='豬排',
                            data='action=pork chop'
                        ),
                        PostbackTemplateAction(
                            label='牛排',
                            data='action=steak'
                        ),
                        PostbackTemplateAction(
                            label='包子',
                            data='action=bao'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.pexels.com/photos/725997/pexels-photo-725997.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                    title='回甘就像現泡',
                    text='◝(　ﾟ∀ ﾟ )◟',
                    actions=[
                        PostbackTemplateAction(
                            label='海鮮',
                            data='action=seafood'
                        ),
                        PostbackTemplateAction( #找晚上的
                            label='咖啡館',
                            data='action=coffeeshop'
                        ),
                        PostbackTemplateAction( #找晚上的
                            label='他只是個按鈕',
                            data='action='
                        ),
                    ]
                )
            ]
        )
    )
    return message

#宵夜選擇
def get_late_night_supper():
    message = TemplateSendMessage(
        alt_text='吃宵夜喔!!',
        template=ButtonsTemplate(
            text='好餓!好想吃宵夜!!',
            actions=[
                PostbackTemplateAction(
                    label='滷味',
                    data='action=Taiwanesebraiseddish'
                ),
                PostbackTemplateAction(
                    label='炸物',
                    data='action=friedfood'
                ),
            ]
        )
    )
    return message

#點心選擇
def get_dessert_menu():
    message = TemplateSendMessage(
        alt_text='想吃什麼。･ﾟ･(つд`ﾟ)･ﾟ･',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.gqfood.com.tw/archive/image/product1/images/mwogzb_03.jpg',
                    title='點心時刻!!!',
                    text='(✪ω✪)',
                    actions=[
                        PostbackTemplateAction(
                            label='蔥抓餅',
                            data='action=ScallionPancake'
                        ),
                        PostbackTemplateAction(
                            label='冰品',
                            data='action=iceproduct'
                        ),
                        PostbackTemplateAction(
                            label='肉圓',
                            data='action=Ba-Wan'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://smlpoints.com/wp-content/uploads/food-taipei-stinky-tofu-1.jpg',
                    title='好臭喔!你有聞到嗎?',
                    text='ヽ(・×・´)ゞ',
                    actions=[
                        PostbackTemplateAction(
                            label='臭豆腐',
                            data='action=Stinkytofu'
                        ),
                        PostbackTemplateAction(
                            label='春捲',
                            data='action=EggRoll'
                        ),
                        PostbackTemplateAction(
                            label='東粄香粿',
                            data='action=savory_rice_pudding'
                        ),
                    ]
                )
            ]
        )
    )
    return message