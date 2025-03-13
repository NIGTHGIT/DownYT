import telebot
from telebot import types
import yt_dlp
import os
from download import descargar_mp3, descargar_mp4





bot = telebot.TeleBot("MI-APY-KEY", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,'By: @Nigth_pg (Cesar Alb.)')
    bot.reply_to(message, "Hello! I'm a bot to download videos from youtube. Send me the link of the video and I will send it to you in mp3 or mp4 format. 😍 Click in /Choose 👆👆👆")
@bot.message_handler(commands=['Choose'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("MP3")
    item2 = types.KeyboardButton("MP4")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Select the format :", reply_markup=markup)

	


@bot.message_handler(func=lambda message: message.text == "MP3")
def mp3(message):
    bot.send_message(message.chat.id, "Send me the link of the youtube video")
    bot.register_next_step_handler(message, mp3_link)

def mp3_link(message):
    url = message.text
    bot.reply_to(message, "Downloads... please wait")	
    #downloand the video and get de filename
    titulos = descargar_mp3(url)
    #trying to send the file to the user
    try:
     with open(titulos, "rb") as file:
        bot.send_document(message.chat.id, file, caption="Here are you MP3 🎵",timeout=220)
    except Exception as e:
     bot.send_message(message.chat.id, f"Error sending MP3: {e}")

    if os.path.exists(titulos):
         os.remove(titulos)
    else:
        print('Not found the file')



@bot.message_handler(func=lambda message: message.text == "MP4")
def mp4(message):
    bot.send_message(message.chat.id, "Send me the link of the youtube video")
    bot.register_next_step_handler(message, mp4_link)


def mp4_link(message):
    url = message.text
    bot.reply_to(message, "Downloads... please wait")
    try:
        #downloand the video and get de filename
        video = descargar_mp4(url)
        with open(video, "rb") as file:
            #trying to send the file to the user
            bot.send_document(message.chat.id, file, caption="Here is your MP4 file  🎥",timeout=220)
        bot.reply_to(message, "Download complete")
        if os.path.exists(video):
         os.remove(video)
        else:
         print('Not found the file')


    except Exception as e:
        bot.reply_to(message, f"❌ Error sending video {e}")
        if os.path.exists(video):
         os.remove(video)
        else:
         print('Not found the file')
    





bot.infinity_polling()