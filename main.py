import os
import telebot

bot = telebot.Telebot("API Key here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
	 bot.reply_to(message,"Hello! I'm Hashan Dimuthu Chat Bot")

@bot.message_handler(commands=["youtube"])
def send_message(message):
	bot.send_message.(message.chat.id "https://www.youtube.com/channel/UCMb9Rcf7mh71x9glgb5oR8A")

bot.polling()