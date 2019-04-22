import pzgram

with open("file.txt","r") as file:
    token=file.readline()
bot = pzgram.Bot(token)
#MESSAGES
msg = "Choose one of the following buttons\n"
err_msg="Sorry, the time of execution is less than the specified time..."

ist=pzgram.create_button("ist","ist")
min_1=pzgram.create_button("1 min","1 min")
min_10=pzgram.create_button("10 min","10 min")
h_1=pzgram.create_button("1 h","1 h")
k =[[ist, min_1], [min_10,h_1]]
keyboard=pzgram.create_inline(k)

#VARIABLES
istante=None
minuto_1=None
minuto_10=None
ora_1=None

#CONTATORE
cont=1


def start(chat):
    global msg, keyboard
    # Send the pool message, attaching the inline keyboard
    chat.send(msg, reply_markup=keyboard)


def get_istant(query, data, message, chat):
    global keyboard, err_msg, msg, cont
    if istante==None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura istantaneo è {}".format(istante))
        start(chat)

def get_min1(query, data, chat):
    global keyboard, err_msg, msg, cont
    if minuto_1==None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 1 minuto è {}".format(minuto_1))
        msg = msg + "Misura {}: {}\n".format(cont,minuto_1)
        cont+=1
        start(chat)

def get_min10(chat, query, data, message):
    global keyboard, err_msg, msg, cont
    if minuto_10==None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 10 minuto è {}".format(minuto_10))
        msg=msg + "Misura {}: {}\n".format(cont,minuto_10)
        cont+=1
        start(chat)

def get_h1(chat, query, data, message):
    global keyboard, err_msg, msg, cont
    if ora_1==None:
        chat.send(err_msg)
        start(chat)
    else:
        chat.send("Il valore di temperatura dopo 1 ora è {}".format(ora_1))
        msg = msg + "Misura {}: {}\n".format(cont,ora_1)
        cont+=1
        start(chat)


commands = {"begin": start}
bot.set_commands(commands)

queries = {"ist": get_istant, "1 min": get_min1, "10 min":get_min10, "1 h": get_h1}
bot.set_query(queries)

bot.run()