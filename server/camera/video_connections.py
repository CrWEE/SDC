import socket
from .camera import CameraFeed

def start_video_connection():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = '192.168.0.31'
    port = 1235
    server_socket.bind((host, port))

    server_socket.listen(5)
    conn, address = server_socket.accept()
    print("Connected to - ", address, "\n")

    CameraFeed(conn).send_images()



