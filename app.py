import telegram
from flask import Flask
from flask import render_template, request
import leancloud
from leancloud import Engine, Query, Object, LeanCloudError
import random
import sys
import urllib3
import json
import threading
import re
import datetime
import logging

app =Flask(__name__)
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

global bot
bot = telegram.Bot(token='219236769:AAFaL3eMxy8R7Dk8K9Gwy8q6opURlDrf9Kk')

@app.run('/token',method=['post'])
def runbot(token):
    if  request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True))
        manage_message(update.message)
    return 'ok'

def manage_message(message):
    text = message.text
    if '/who' in text:
        echo(message)



def echo(message):
    text = "I am Mokee bot ,my fater is qingliu!"
    chat_id = message.chat.id
    bot.sendMessage(chat_id=chat_id,text=text)

