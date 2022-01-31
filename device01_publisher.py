from time import sleep
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

endpoint = "ax7j1tokadxlb-ats.iot.us-east-2.amazonaws.com"
client_id = "device01"
path_certificate = "D:\\AWS\\device01\\bbca1c3ef41424274a1576e916c2e4892fbaec4dfc06f3cf9fb289902c38470a-certificate.pem.crt"
path_privatekey = "D:\\AWS\\device01\\bbca1c3ef41424274a1576e916c2e4892fbaec4dfc06f3cf9fb289902c38470a-private.pem.key"
path_rootca1 = "D:\\AWS\\device01\\AmazonRootCA1.pem"

my_awsmqtt_client = AWSIoTPyMQTT.AWSIoTMQTTClient(client_id)
my_awsmqtt_client.configureEndpoint(endpoint, 8883)
my_awsmqtt_client.configureCredentials(path_rootca1, path_privatekey, path_certificate)

my_awsmqtt_client.connect()

topic = "test/status"
msg = "Hello World"

print('Inicio de publicação')

for i in range(5):
    my_awsmqtt_client.publish(topic, msg, 1) 
    print(f"Publicação 0{i+1}: {msg} ao tópico [{topic}]")
    sleep(0.5)

print('Fim de publicação')
my_awsmqtt_client.disconnect()