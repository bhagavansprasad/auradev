#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("aura_net_news/#")

def on_message(client, userdata, msg):
    print (msg)
    #client.disconnect()
    
client = mqtt.Client()
client.connect("iot.eclipse.org",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

