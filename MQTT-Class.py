import paho.mqtt.client as paho
#pip3 install paho-mqtt
global mqttclient;
global broker;
global port;


broker = "0.0.0.0";
port = 1883;

client_uniq = "pubclient_123"

mqttclient = paho.Client(client_uniq, True) 

def test(client, userdata, message):
  print("client:"+ str(client))
  print("userdata:"+ userdata)
  print("message:"+ message.payload)

def _on_message(client, userdata, msg):
# 	print("Received: Topic: %s Body: %s", msg.topic, msg.payload)
	print(msg.topic+" "+str(msg.payload))
	 
#Subscribed Topics 
def _on_connect(mqttclient, userdata, flags, rc):
# 	print("New Client: "+str(mqttclient)+ " connected")
# 	print(rc)
	mqttclient.subscribe("IOT/#", qos=0)	
  
mqttclient.message_callback_add("IOT/test", test)

mqttclient.connect(broker, port, keepalive=1, bind_address="")
  
mqttclient.on_connect = _on_connect

mqttclient.loop_forever()
