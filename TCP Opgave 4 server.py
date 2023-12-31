from socket import *
import threading
import random

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

def handleCommunication(connectionSocket, addr):
    print(f'User {addr} has connected')
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print(f'Received: {sentence}')

        myList = sentence.split(';')
        print(f'Received: {sentence}')
        
        value1 = int(myList[1])
        value2 = int(myList[2])
        result = 0

        if myList[0]== 'Add':
            result = value1 + value2

        elif myList[0]== 'Subtract':
            result = value2 - value1
           
        elif myList[0]== 'Random':
            result = random.randint(value1, value2)
        
        result = str(result)
        connectionSocket.send(result.encode())

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleCommunication, args=(connectionSocket, addr)).start()