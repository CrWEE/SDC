import socket

clientSocket = socket.socket()
serverName = '192.168.0.31'
serverPort = 1234

def connect():
    clientSocket.connect((serverName, serverPort))

def sendEvent(message):
    clientSocket.sendall(message.name.encode('utf-8'))

def disconnect():
    clientSocket.close
