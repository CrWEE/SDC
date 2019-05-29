import socket

global clientSocket

def sendEvent(message):
    clientSocket.sendall(message.name.encode('utf-8'))

def disconnect():
    clientSocket.close
