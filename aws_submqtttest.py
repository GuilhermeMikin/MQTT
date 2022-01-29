import time as t
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
ENDPOINT = "ax7j1tokadxlb-ats.iot.us-east-2.amazonaws.com"
CLIENT_ID = "testDevice"
PATH_TO_CERTIFICATE = "D:\\AWS\\thingtest\\31d8a33563-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "D:\\AWS\\thingtest\\31d8a33563-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "D:\\AWS\\thingtest\\AmazonRootCA1.pem.txt"
TOPIC = "test/status"

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

myAWSIoTMQTTClient.connect()
print('Begin Subscription \n')

def customCallback(client, userdata, message):
    print(message.payload.decode("utf-8"))
myAWSIoTMQTTClient.subscribe(TOPIC, 1, customCallback)

print('waiting for the callback. Click to conntinue...')
x = input()

myAWSIoTMQTTClient.unsubscribe(TOPIC)
print("Client unsubscribed") 


myAWSIoTMQTTClient.disconnect()
print("Client Disconnected")