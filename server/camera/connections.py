import socket
import select
from pubsub import pub
import bus
import threading
import struct


def start_video_connection(camera_feed):
    try:
        connection_list = []
        recv_buffer = 4096
        host = get_ip_address()
        port = 1235

        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))

        connection_list.append(server_socket)

        server_socket.listen(5)

        while 1:
            # Wait for one of the sockets to have data
            read_sockets, write_sockets, error_sockets = select.select(connection_list, [], [])

            for sock in read_sockets:
                # New connection
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    data = sockfd.recv(recv_buffer)
                    if data:
                        data_string = data.decode('utf-8')
                        print("Client connected: ", addr, "with type: ", data_string)
                        if data_string == 'VIDEO':
                            threading.Thread(target=send_stream_to_client, args=[sockfd, camera_feed]).start()
                    connection_list.append(sockfd)
                # Handle messages
                else:
                    try:
                        data = sock.recv(recv_buffer)
                        if data:
                            data_string = data.decode('utf-8')
                            print("Received command: ", data_string)
                            pub.sendMessage(bus.controlTopic, msg=data_string)
                    # On connection reset etc. remove the socket from the list
                    except:
                        sock.close()
                        connection_list.remove(sock)
                        print("Client disconnected (start_video_connection): ", addr)
                        continue

    except Exception as e:
        print("Error occurred (start_video_connection): ", e)


# Runs in a new thread, send the actual captured image to a single client
def send_stream_to_client(socket_c, camera_feed):
    while 1:
        try:
            image = camera_feed.image[:]
            length_bytes = struct.pack('!i', len(image))
            socket_c.send(length_bytes)
            socket_c.send(image)
        except:
            socket_c.close()
            print("Client disconnected (send_stream_to_client): ", socket_c)
            return


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print("Couldn't get IP address: ", e)
    finally:
        s.close()



