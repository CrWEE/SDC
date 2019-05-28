import socket
import socketserver
from .camera import CameraFeed


class UDPSocketHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        super(UDPSocketHandler, self).__init__(request, client_address, server)

    def handle(self):
        current_socket = self.request[1]
        print("{} connected".format(self.client_address[0]))
        self.camera_feed.add_socket_connection(current_socket)


def start_video_connection():
    try:
        host = get_ip_address()
        port = 1235

        camera_feed = CameraFeed()
        camera_feed.send_images()
        with socketserver.UDPServer((host, port), UDPSocketHandler) as server:
            server.camera_feed = camera_feed
            server.serve_forever()

    except Exception as e:
        print(e)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print("Couldn't get IP address: ", e)
    finally:
        s.close()



