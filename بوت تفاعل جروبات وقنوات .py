import pyfiglet
import requests
import json 
import telebot
import random
from telebot import types

lost = pyfiglet.figlet_format('OWNER USER @DD0D2')
print(lost)

API_TOKEN = '7727396968:AAGt7odCWGrclfAKWINCXDfmMVGbSkMXbJ0'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        C4_ = types.InlineKeyboardMarkup()
        C4_.row_width = 2
        TC4 = types.InlineKeyboardButton(text="مطور رعد", url="tg://user?id=7473147273")
        AIM = types.InlineKeyboardButton(text="سورس رعد ", url="https://t.me/BBBi19")
        X = types.InlineKeyboardButton(text="Add me to a group", url="https://t.me/Bot_rashq_bot?startgroup")
        HLTV = types.InlineKeyboardButton(text="Add me to a channel", url="https://t.me/Bot_rashq_bot?startchannel")
        C4_.add(AIM, TC4, X, HLTV)
        name_of_C4 = f"{message.from_user.first_name}"
        text = f'''* مرحبا عزيزي {name_of_C4}, أنا بوت تفاعل برموز تعبيرية يمكنك إضافتي إلى مجموعة أو قناة للتفاعل *'''
        bot.send_message(message.chat.id, text, reply_markup=C4_, parse_mode='Markdown')

@bot.channel_post_handler()
def react_to_channel_message(message):
    reactions = ["👍", "❤️", "🔥", "🥰", "👏", "😁", "❤️‍🔥", "🤯", "😘", "👨‍💻", "😎", "🕊", "🗿", "😐"]
    emoji = random.choice(reactions)
    send_message_react({
        'chat_id': message.chat.id,
        'message_id': message.message_id,
        'reaction': json.dumps([{'type': "emoji", "emoji": emoji}])
    })

@bot.message_handler(func=lambda message: True)
def react_to_message(message):
    reactions = ["👍", "❤️", "🔥", "🥰", "👏", "😁", "❤️‍🔥", "🤯", "😘", "👨‍💻", "😎", "🕊", "🗿", "😐"]
    emoji = random.choice(reactions)
    response = send_message_react({
        'chat_id': message.chat.id,
        'message_id': message.message_id,
        'reaction': json.dumps([{'type': "emoji", "emoji": emoji}])
    })

def send_message_react(datas={}):
    url = "https://api.telegram.org/bot" + API_TOKEN + "/" + 'setmessagereaction'
    response = requests.post(url, data=datas)

    if response.status_code != 200:
        return "Error: " + response.text
    else:
        return response.json()

bot.infinity_polling()
