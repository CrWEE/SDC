import connection
import keyboard_input as keyboard
import camera.client_video as video
import threading
import socket


def main():
    ADDRESS = ("192.168.0.31", 1235)
    socket_command = socket.socket()
    socket_command.connect(ADDRESS)
    socket_command.sendall('CONTROL'.encode('utf-8'))
    connection.clientSocket = socket_command
    threading.Thread(target=keyboard.start_input).start()

    socket_video = socket.socket()
    socket_video.connect(ADDRESS)
    socket_video.sendall('VIDEO'.encode('utf-8'))
    video.run_show_image(socket_video)


main()
