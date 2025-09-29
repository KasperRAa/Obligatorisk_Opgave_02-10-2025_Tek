#Now Exists On My Laptop
from socket import *
import json

serverPort = 23451
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', serverPort))

def user_Simple():
    while True:
        cmd = input('Enter command (Random, Add, Subtract, Exit): ')
        clientSocket.send(cmd.encode())
        if cmd == 'Exit':
            break
        print(clientSocket.recv(1024).decode())
        numbers = input()
        clientSocket.send(numbers.encode())
        print(clientSocket.recv(1024).decode())
    clientSocket.close()

def user_JSON():
    while True:
        cmd = input('Enter command (Random, Add, Subtract, Exit): ')
        if cmd == 'Exit':
            break
        n1 = int(input('Enter number #1: '))
        n2 = int(input('Enter number #2: '))
        string = [cmd, n1, n2]
        string = json.dumps(string)
        clientSocket.send(string.encode())
        print(clientSocket.recv(1024).decode())
    clientSocket.close()

user_JSON()