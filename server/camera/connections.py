import socket
import select
from pubsub import pub
import bus


def start_video_connection():
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
                    connection_list.append(sockfd)
                    print("Client connected: ", addr)
                    pub.sendMessage(bus.socketTopic, msg=sockfd, msg_type='ADD')
                # Handle messages
                else:
                    try:
                        data = sock.recv(recv_buffer)
                        if data:
                            data_string = data.decode('utf-8')
                            print(data_string)
                            pub.sendMessage(bus.controlTopic, msg=data_string)
                    # On connection reset etc. remove the socket from the list
                    except:
                        sock.close()
                        connection_list.remove(sock)
                        print("Client disconnected: ", addr)
                        pub.sendMessage(bus.socketTopic, msg=sockfd, msg_type='REMOVE')
                        continue

    except Exception as e:
        print("Error occured: ", e)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print("Couldn't get IP address: ", e)
    finally:
        s.close()



