import paho.mqtt.client as mqtt
import time 
import requests
import http.client
import json
from datetime import timedelta, datetime
from pytz import timezone
import os, ssl

import logging

MQTT_BROKER_HOST = '54.157.211.208'
MQTT_BROKER_PORT = 1883
MQTT_KEEP_ALIVE_INTERVAL = 60
print('try to connect with mqtt')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("meter/data/#")

def on_message(client, userdata, msg):
    global hubid_recv, subtopic
    print("Message Recieved. ", msg.payload.decode())
    data = msg.payload.decode()
    print (data)
    string = data.split(":")
    strng ='okkk' #string[0]
    print(strng)
    hub = string[1]
    if (strng == "okkk"):
        
        # subtopic = hub+"/downlink"
        # print(subtopic)
        # hubid_recv = True
        # client.publish(subtopic, "ack");
        # print("sent")
        str1 = data.split(":")
        hub_id = str1[1]
        print("hubid is",hub_id)
        hubid_recv = True
        datajs = {"data":data}
        #datajs = {"data" : data}
        print (datajs)
        x = requests.post("http://localhost:8000/mqtttest/", json = datajs, verify = False)
        print(x)
    else:
        if(hubid_recv == True):
            client.publish(subtopic, "ack");    
        print("kuch ni aaya")

client = mqtt.Client()
print(client)
client.username_pw_set(username="sstpl",password="sstpl@123")
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_KEEP_ALIVE_INTERVAL)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

