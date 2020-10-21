#!/usr/bin/python
import datetime
import time
import os
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

giorni_compleanni=[]
nomi_festeggiati=[]
TOKEN = '{YOUR TELEGRAM BOT TOKEN}'
bot = telepot.Bot(TOKEN)
x = datetime.datetime.now()

if x.strftime("%d-%m") in giorni_compleanni:
    pos=giorni_compleanni.index(x.strftime("%d-%m"))
    persona=nomi_festeggiati[pos]
    testo="Oggi e' il compleanno di: " + persona
    bot.sendMessage('{YOUR CHAT ID}',testo)
    print(testo)
    del giorni_compleanni[pos]
    del nomi_festeggiati[pos]
    if x.strftime("%d-%m") in giorni_compleanni:
        pos=giorni_compleanni.index(x.strftime("%d-%m"))
        persona=nomi_festeggiati[pos]
        testo="Oggi e' il compleanno di: " + persona
        bot.sendMessage('{YOUR CHAT ID}',testo)
        print(testo)
