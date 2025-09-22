from socket import * 
import threading
import random
import json

serverPort = 23451
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def service_Simple(socket: socket):
    while True:
        message = socket.recv(1024).decode().strip()
        if message == '':
            break
        
        if message == 'Exit':
            break

        cmd = message
        socket.send('Input numbers'.encode())
        numbers = socket.recv(1024).decode().strip().split(' ')
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        result = 'ERROR'
        if cmd == 'Random':
            result = random.randint(n1, n2)
        if cmd == 'Add':
            result = n1 + n2
        if cmd == 'Subtract':
            result = n1 - n2
        socket.send(f'{result}'.encode())
    
    socket.close()

def service_JSON(socket: socket):
    while True:
        message = socket.recv(1024).decode().strip()
        if message == '':
            break
        message = json.loads(message)
        
        if message[0] == 'Exit':
            break

        cmd = message[0]
        n1 = message[1]
        n2 = message[2]

        result = 'ERROR'
        if cmd == 'Random':
            result = random.randint(n1, n2)
        if cmd == 'Add':
            result = n1 + n2
        if cmd == 'Subtract':
            result = n1 - n2
        socket.send(f'{result}'.encode())
    
    socket.close()



while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=service_JSON, args=(connectionSocket,)).start()