from socket import *

serverName = "192.168.0.187"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    operation = input('Operation:')
    value1 = input('Value 1:')
    value2 = input('Value2:')
    message = operation + ';' + value1 + ';' + value2

    clientSocket.send(message.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From server: ', modifiedSentence.decode())