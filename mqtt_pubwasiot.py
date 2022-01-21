from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys

myMQTTClient = AWSIoTMQTTClient("device1")

myMQTTClient.configureEndpoint("ax7j1tokadxlb-ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials(CAFilePath="AWS/root.pem.",KeyPath="AWS/7887dfe01c-private.pem.key",CertificatePath="AWS/7887dfe01c-certificate.pem.crt.txt")

myMQTTClient.connect()
print("Client Connected")

msg = "Sample data from the device"
topic = "test/status"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent heheh")

myMQTTClient.disconnect()
print("Client Disconnected")