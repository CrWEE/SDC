import socket

serverSocket = socket.socket()
host = '192.168.0.31'
port = 1234
serverSocket.bind((host, port))

serverSocket.listen(5)
conn, addr = serverSocket.accept()
with conn:
    print('Connected by', addr)
    while True:
        print('Got connection from', addr)
        data = conn.recv(1024)
        print(data)
    # c.send('Thank you for connecting'.encode())


