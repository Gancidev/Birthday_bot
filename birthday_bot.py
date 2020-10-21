#!/usr/bin/python
import datetime
import time
import os
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

giorni_marty=['20-01','05-02','07-02','15-02','16-02','19-03','25-03','28-03','31-03','02-04','01-06','10-06','11-06','17-07','24-07','04-09','02-10','31-10','10-11','17-11','1-12']
nomi_marty=['Nonno Marty','Aurora','Martina','Michelle Cug. Marty','Cristina Cug. Marty','Zia Anna','Ginevra Zia Anna','Giusi Zia Anna','Suocera','Zia Francesca Marty','Suocero','Angela Zia Manu','Mari Zia Manu','Nonna Maria Marty','Zio Salvo Marty','Zia Manu','Raimondo','Salvo Zia Manu','Zio Nino Marty','Angela Zia Manu','Zio Carlo Marty']

giorni_peppe=['01-01','05-01','18-01','31-01','01-02','11-02','18-02','18-02','19-02','28-02','20-03','08-05','06-06','12-07','16-07','06-08','16-08','03-09','27-09','28-09','28-09','29-09','05-10','11-10','13-10','23-10','2-12','3-12','18-12','24-12','23-09']
nomi_peppe=['Nonna Marilena','Zio Gabry','Marghy Zio Pino','Nonna Cetty','Zia Cinzia','Antonino Zio Mario','Mamma','Antonino Zio Ignazio','TU','Zio Pino','Giorgia Zio Calogero','Zia Ignazia','Papi','Giulia Zio Mario','Alessia Zia Rosy','Zia Maria','Zia Paola','Giuseppe Zio Igny','Marco Zio Calogero','Andrea Fratellino','Zio Ignazio','Zia Rosy','Cetty Zio Pino','Antonio Fratello','Nonno Giuseppe','Zio Mario','Nonno Nino','Zio Calogero','Karol Zia Rosy','Simona','Ignazio Cetty Zio Pino']

TOKEN = '1261997134:AAFOkbG4vix8qAwwjIKzViDg61Fh-GVIRn8'
bot = telepot.Bot(TOKEN)

#print("Martina:"+str(len(giorni_marty))+" "+str(len(nomi_marty)))
#print("Peppe:"+str(len(giorni_peppe))+" "+str(len(nomi_peppe)))

x = datetime.datetime.now()
#print(x.strftime("%d-%m"))

if x.strftime("%d-%m") in giorni_marty:
    pos=giorni_marty.index(x.strftime("%d-%m"))
    persona=nomi_marty[pos]
    testo="Oggi e' il compleanno di: " + persona
    bot.sendMessage('151511468',testo)
    print(testo)
    del giorni_marty[pos]
    del nomi_marty[pos]
    if x.strftime("%d-%m") in giorni_marty:
        pos=giorni_marty.index(x.strftime("%d-%m"))
        persona=nomi_marty[pos]
        testo="Oggi e' il compleanno di: " + persona
        bot.sendMessage('151511468',testo)
        print(testo)
else:
    #bot.sendMessage('151511468','Nessun compleanno da Marty oggi.')
    print('Nessun Compleanno Da Marty oggi.')

if x.strftime("%d-%m") in giorni_peppe:
    pos=giorni_peppe.index(x.strftime("%d-%m"))
    persona=nomi_peppe[pos]
    testo="Oggi e' il compleanno di: " + persona
    bot.sendMessage('151511468',testo)
    print(testo)
    del giorni_peppe[pos]
    del nomi_peppe[pos]
    if x.strftime("%d-%m") in giorni_peppe:
        pos=giorni_peppe.index(x.strftime("%d-%m"))
        persona=nomi_peppe[pos]
        testo="Oggi e' il compleanno di: " + persona
        bot.sendMessage('151511468',testo)
        print(testo)
else:
    #bot.sendMessage('151511468','Nessun compleanno da Peppe oggi.')
    print('Nessun Compleanno Da Peppe oggi')
