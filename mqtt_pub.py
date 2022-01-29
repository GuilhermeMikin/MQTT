import paho.mqtt.client as mqtt
import sys
from time import sleep

client = mqtt.Client()

if client.connect("3.134.40.193", 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.publish("test/status", "Hello World from paho-mqtt!")
sleep(0.2)
print("Publicado..")

client.disconnect()