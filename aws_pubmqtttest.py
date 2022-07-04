import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

ENDPOINT = "a14esw6xzioxj2-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "testDevice"
PATH_TO_CERTIFICATE = "D:\\AWS\\esteira_certs\\esteiraic-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "D:\\AWS\\esteira_certs\\esteiraic-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "D:\\AWS\\esteira_certs\\AmazonRootCA1.pem"
MESSAGE = "Ok.. now we're talking heheh"
TOPIC = "test/status"
RANGE = 5

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"message" : data}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)
print('Publish End')
myAWSIoTMQTTClient.disconnect()