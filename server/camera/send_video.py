import socket
import threading
from . import Connection

# Create socket and listen on port 5005
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("", 5005))
server_socket.listen(5)

opened_cameras = {}


def signal_handler(signal=None, frame=None):
    exit(0)

def start_connections():
    # Loop and check for new connections
    print("Receiving connections for video")
    while 1:
        try:
            client_socket, address = server_socket.accept()
            print("Connected to - ", address, "\n")
            cam_url = client_socket.recv(1024)
            # if camera url does not exsists in oppened camera, open new connection,
            # or else just append client params and pass to Connection thread
            if cam_url not in opened_cameras:
                client = Connection.Connection([client_socket, cam_url])
                opened_cameras[cam_url] = client
                threading.Thread(target=client.capture, args=opened_cameras).start()

            else:
                opened_cameras[cam_url].addConnection(client_socket)

        except socket.timeout:
            continue
        except KeyboardInterrupt:
            server_socket.close()

            del connections
            exit(0)