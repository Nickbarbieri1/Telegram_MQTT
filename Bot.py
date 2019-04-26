import pzgram
from MQTT import *

#with open("file.txt","r") as file:
#    token=file.readline()
bot = pzgram.Bot("713980055:AAFVGg-LrMkba3K6MgbaHej1t4zcuzwGbns")
#MESSAGES
msg = "Choose one of the following buttons\n"
err_msg="Sorry, the time of execution is less than the specified time..."

ist=pzgram.create_button("ist","ist")
min_1=pzgram.create_button("1 min","1 min")
min_10=pzgram.create_button("10 min","10 min")
h_1=pzgram.create_button("1 h","1 h")
k =[[ist, min_1], [min_10,h_1]]
keyboard=pzgram.create_inline(k)

#CONTATORE
cont=1


def start(chat):
    global msg, keyboard
    # Send the pool message, attaching the inline keyboard
    chat.send(msg, reply_markup=keyboard)


def get_istant(query, data, message, chat):
    global keyboard, err_msg, msg, cont
    if listaFinale[0] == None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura istantaneo è {}".format(listaFinale[0]))
        start(chat)

def get_min1(query, data, chat):
    global keyboard, err_msg, msg, cont
    if listaFinale[1] == None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 1 minuto è {}".format(listaFinale[1]))
        msg = msg + "Misura {}: {}\n".format(cont, listaFinale[1])
        cont+=1
        start(chat)

def get_min10(chat, query, data, message):
    global keyboard, err_msg, msg, cont
    if listaFinale[2] == None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 10 minuto è {}".format(listaFinale[2]))
        msg=msg + "Misura {}: {}\n".format(cont,listaFinale[2])
        cont+=1
        start(chat)

def get_h1(chat, query, data, message):
    global keyboard, err_msg, msg, cont
    if listaFinale[3] == None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 1 ora è {}".format(listaFinale[3]))
        msg = msg + "Misura {}: {}\n".format(cont, listaFinale[3])
        cont+=1
        start(chat)


commands = {"begin": start}
bot.set_commands(commands)

queries = {"ist": get_istant, "1 min": get_min1, "10 min":get_min10, "1 h": get_h1}
bot.set_query(queries)

def main():
    bot.run()

if __name__ == '__main__':
    main()
