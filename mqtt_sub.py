import paho.mqtt.client as mqtt
import sys
from time import sleep

broker_addrs = "127.0.0.1"
port = 1883

def onMessage(client, userdata, msg):
    sleep(1)
    print("Mensagem recebida..")
    print("Topic: " + str(msg.topic) + "  Message: " + str(msg.payload.decode("utf-8")))

client = mqtt.Client()
client.on_message = onMessage

if client.connect(broker_addrs, port, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)
else:
    print("Client connected..")

client.subscribe("test/status")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except:
    print("Disconnecting from broker")
client.disconnect()