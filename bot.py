import telebot
import os
from keep_alive import keep_alive

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salve, fã da FURIA! O bot já tá online 🔥")

@bot.message_handler(commands=['ultimajogo'])
def ultimajogo(message):
    bot.reply_to(message, "A FURIA venceu por 2x1 contra NAVI no último jogo. GG! 🐍🔥")

@bot.message_handler(commands=['proximojogo'])
def proximojogo(message):
    bot.reply_to(message, "Próximo jogo: FURIA x MIBR — amanhã às 18h! 🎯")

@bot.message_handler(commands=['destaque'])
def destaque(message):
    bot.reply_to(message, "Yuurih foi o destaque da partida com 28 abates! 🧠")

@bot.message_handler(commands=['frase'])
def frase(message):
    bot.reply_to(message, "‘A bala come e a FURIA responde.’ – ArT 🎤🔥")

@bot.message_handler(commands=['enquete'])
def enquete(message):
    bot.send_poll(message.chat.id, "Quem foi o melhor jogador da FURIA?", ["KSCERATO", "yuurih", "arT", "chelo", "fallen"])

keep_alive()
bot.polling()
