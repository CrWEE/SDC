import connection
import keyboard_input as keyboard
import camera.receive_video as video

def main():
    connection.connect()
    keyboard.start_input()
    video.startReceive()

main()
