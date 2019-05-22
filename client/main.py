import connection
import keyboard_input as keyboard
import camera.client_video as video
import threading


def main():
    connection.connect()
    threading.Thread(target=keyboard.start_input).start()
    video.run_show_image()


main()
