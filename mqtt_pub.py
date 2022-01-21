import paho.mqtt.client as mqtt
import sys
from time import sleep

broker_addrs = "127.0.0.1"
port = 1883

iot_endpoint = "ax7j1tokadxlb-ats.iot.us-east-2.amazonaws.com"
key_prefix = ""
root = ""
cert = ""
key = ""

client = mqtt.Client()

if client.connect(iot_endpoint, 8883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

# client.publish("test/status", "Hello World from paho-mqtt!")
# sleep(0.2)
# print("Publicado..")

client.publish("test/status", "now we're talking")
sleep(0.2)
print("Publicado..")

client.disconnect()