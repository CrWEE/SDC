import keyboard
import connection
from server.payloads import ControlPayload


def send_control_event(event):
    connection.sendEvent(event)


def send_speed_event(event):
    connection.sendEvent(event)


def print_pressed_keys(e):
    print(e)
    if 'up' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.FORWARD)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STOP)
    if 'down' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.BACKWARD)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STOP)
    if 'left' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.LEFT)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STRAIGHT)
    if 'right' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.RIGHT)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STRAIGHT)
    if 'esc' == e.name:
        connection.disconnect()

def start_input():
    keyboard.hook(print_pressed_keys)
    keyboard.wait()
