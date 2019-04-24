from MQTT import *
import subprocess
import time

start = time.time()
count = 0

def UnMinuto():
    global count
    rec = 'GET https://api.thingspeak.com/update?api_key=LHYVUYXS94NNTEF4&field2=' + str(listaFinale[1])
    u = subprocess.Popen(['echo', rec], stdout=subprocess.PIPE)
    subprocess.call(['nc', 'api.thingspeak.com', '80'], stdin=u.stdout)
    count += 1

def DiesciMinuti():
    Rec = 'GET https://api.thingspeak.com/update?api_key=LHYVUYXS94NNTEF4&field3=' + str(listaFinale[2])
    u = subprocess.Popen(['echo', Rec], stdout=subprocess.PIPE)
    subprocess.call(['nc', 'api.thingspeak.com', '80'], stdin=u.stdout)

while True:
    time.sleep(60.0 - ((time.time() - start) % 60.0))
    UnMinuto()
    if count % 10 == 0:
        time.sleep(15)
        DiesciMinuti()