import socket
from .camera import CameraFeed


def start_video_connection():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = get_ip_address()
    port = 1235
    server_socket.bind((host, port))

    server_socket.listen(5)
    conn, address = server_socket.accept()
    print("Connected to - ", address, "\n")

    CameraFeed(conn).send_images()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print("Couldn't get IP address: ", e)
    finally:
        s.close()



