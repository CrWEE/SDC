import socket
from pubsub import pub
import bus


def start_receiving():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = '192.168.0.31'
    port = 1234
    server_socket.bind((host, port))

    server_socket.listen(5)
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            data_string = data.decode('utf-8')
            print(data_string)
            pub.sendMessage(bus.controlTopic, msg=data_string)
        # c.send('Thank you for connecting'.encode())


