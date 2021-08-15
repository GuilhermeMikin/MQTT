import paho.mqtt.client as mqtt
import sys

broker = "127.0.0.1"
port = 1883

def onMessage(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode())

client = mqtt.Client()
client.on_message = onMessage

if client.connect(broker, port, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.subscribe("test/status")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except:
    print("Disconnecting from broker")
client.disconnect()