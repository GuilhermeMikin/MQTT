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

client = mqtt.Client()

if client.connect(broker_addrs, port, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

msg = ''
topic = input('\nPublish to topic: ')
while True:
    msg = int(input("Message [0 to exit]: "))
    if msg == 0:
        break
    else:
        client.publish(topic, msg)
        sleep(0.2)
        print("Message published...\n")

print('\nDisconnecting...')
sleep(1)
client.disconnect()