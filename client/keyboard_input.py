import keyboard
from pubsub import pub
from payloads import ControlPayload
from server import bus


def send_control_event(event):
    pub.sendMessage(bus.controlTopic, msg=event)


def send_speed_event(event):
    pub.sendMessage(bus.speedTopic, msg=event)


def print_pressed_keys(e):
    print(e)
    if '8' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.FORWARD)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STOP)
    if '2' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.BACKWARD)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STOP)
    if '4' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.LEFT)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STRAIGHT)
    if '6' == e.name:
        if 'down' == e.event_type:
            send_control_event(ControlPayload.RIGHT)
        if 'up' == e.event_type:
            send_control_event(ControlPayload.STRAIGHT)

def start_input():
    keyboard.hook(print_pressed_keys)
    keyboard.wait()
