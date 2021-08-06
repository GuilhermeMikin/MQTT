import paho.mqtt.client as mqtt
import sys
import time

broker = "127.0.0.1"

client = mqtt.Client()

if client.connect(broker, 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.publish("test/status", "Hello World from paho-mqtt!", 0)

client.disconnect()