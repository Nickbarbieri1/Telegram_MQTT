import Bot
import MQTT
import Thinkspeak
import threading

a = threading.Thread(target=Bot.main)
b = threading.Thread(target=MQTT.main)
c = threading.Thread(target=Thinkspeak.main)
b.start()
c.start()
a.start()