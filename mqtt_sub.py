import paho.mqtt.client as mqtt
import sys
from time import sleep

print('-' * 100)
print('Welcome to paho-MQTT_Subscriber!!'.center(100))

# broker_addrs = "3.134.40.193"
# port = 1883
mqtt_broker = input('\nPlease, enter the MQTT Broker Host: ')
if mqtt_broker == "aws":
    broker_addrs = "3.134.40.193"
else:
    broker_addrs = mqtt_broker
port = int(input('Enter the Port: '))


def onMessage(client, userdata, msg):
    # print("Message received...")
    # print("Topic: " + str(msg.topic) + " Message: " + str(msg.payload.decode("utf-8")))
    print(str(msg.payload.decode("utf-8")))

client = mqtt.Client()
client.on_message = onMessage
if client.connect(broker_addrs, port, 60) !=0:
    print("\nCould not connect to MQTT Broker!")
    sys.exit(-1)
else:
    print("\nClient connected...")

topic = input('\nSubscribe to topic: ')
client.subscribe(topic)

try:
    print("\nSuccessfully Subscribed! Press CTRL+C to exit...\n")
    client.loop_forever()
except:
    print("\nDisconnecting from broker...\n")

client.disconnect()