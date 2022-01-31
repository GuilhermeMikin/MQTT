import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

endpoint = "a2agzq0m7iu93l-ats.iot.us-east-2.amazonaws.com"
client_id = "device01"
path_certificate = "D:\\AWS\\device01\\bbca1c3ef41424274a1576e916c2e4892fbaec4dfc06f3cf9fb289902c38470a-certificate.pem.crt"
path_privatekey = "D:\\AWS\\device01\\bbca1c3ef41424274a1576e916c2e4892fbaec4dfc06f3cf9fb289902c38470a-private.pem.key"
path_rootca1 = "D:\\AWS\\device01\\AmazonRootCA1.pem"

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(client_id)
myAWSIoTMQTTClient.configureEndpoint(endpoint, 8883)
myAWSIoTMQTTClient.configureCredentials(path_rootca1, path_privatekey, path_certificate)

print('-' * 100)
print('MQTT Subscriber'.center(100))
topic = input('\nInscrever-se no tópico: ')

myAWSIoTMQTTClient.connect()
print('Inicio de Inscrição \n')


def customCallback(client, userdata, message):
    print(message.payload.decode("utf-8"))

myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
print(f'\nInscrito com sucesso no tópico [{topic}]! Pressione Enter para sair...\n')
x = input()

myAWSIoTMQTTClient.unsubscribe(topic)
print("Cliente não mais inscrito...") 

myAWSIoTMQTTClient.disconnect()
print("Cliente desconectado!")