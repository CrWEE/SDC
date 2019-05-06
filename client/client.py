import socket

clientSocket = socket.socket()
serverName = '192.168.0.31'
serverPort = 1234

message = 'test 123'

clientSocket.connect((serverName, serverPort))
clientSocket.sendto(message.encode(), (serverName, serverPort))
print(clientSocket.recv(1024))
clientSocket.close
