import connection
import keyboard_input as keyboard
import camera.client_video as video
import threading
import socket


def main():
    ADDRESS = ("192.168.0.31", 1235)
    s = socket.socket()
    s.connect(ADDRESS)
    connection.clientSocket = s
    threading.Thread(target=keyboard.start_input).start()
    video.run_show_image(s)


main()
