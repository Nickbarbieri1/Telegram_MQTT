import paho.mqtt.client as mqtt
#VARIABLES
cont = 0
cont1 = 0
cont2 = 0
listaTemp=[]
listaFinale=[None,None,None,None]

def on_connect(client, userdata, flags,rc):
	print('result from connect: {}'.format(mqtt.connack_string(rc)))
	client.subscribe('calvino-08/temperatura', qos = 0)
def on_subscribe(client, userdata, mid, granted_qos):
	print('subscribed topic with QoS: {}'.format(granted_qos[0]))

def get_istant(istantanea):
	return istantanea

def get_min1(lista):
	T1 = 0
	temp = 0
	for i in range(1, 13):
		temp = temp + float(lista[-i])
	T1 = temp / 12
	T1 = float(round(T1,1))
	return T1

def get_min10(lista):
	T2 = 0
	temp = 0
	for i in range(1, 121):
		temp = temp + float(lista[-i])
	T2 = temp / 120
	T2 = float(round(T2,1))
	return T2

def get_h1(lista):
	T3 = 0
	temp = 0
	for i in range(1, 721):
		temp = temp + float(lista[-i])
	T3 = temp / 720
	T3 = float(round(T3,1))
	return T3

def on_message(client, userdata, msg):
	global cont, cont1, cont2, listaTemp, listaFinale
	temperatura = float(msg.payload.decode("utf-8"))
	listaTemp.append(temperatura)
	cont += 1
	cont1 += 1
	cont2 += 1
	listaFinale[0]=get_istant(temperatura)
	if (cont == 12):
		cont = 0
		listaFinale[1]=get_min1(listaTemp)
	if (cont1 == 120):
		cont1 = 0
		listaFinale[2]=get_min10(listaTemp)
	if (cont2 == 720):
		cont2 = 0
		listaFinale[3]=get_h1(listaTemp)
		listaTemp=[]
	print(listaFinale)
	return listaFinale #return of the final list with the measures
def main():
	client = mqtt.Client(protocol = mqtt.MQTTv311)
	client.on_connect = on_connect
	client.on_subscribe = on_subscribe
	client.on_message = on_message
	client.username_pw_set(username = "calvino00", password = "0123456789")
	client.connect(host = 'broker.shiftr.io', port = 1883, keepalive = 60)
	try:
		client.loop_forever()
	except KeyboardInterrupt:
		print()

if __name__ == '__main__':
	main()