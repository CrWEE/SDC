from payloads import ControlPayload
import controller

class BusListener:
    def __init__(self, camera_feed):
        self.camera_feed = camera_feed

    def process_control_event(self, msg):
        print('Method Listener.process_control_event received: ', repr(msg))
        #enumValue = ControlPayload(msg)
        if 'FORWARD' == msg:
            controller.forward()
        if 'STOP' == msg:
            controller.stop()
        if 'BACKWARD' == msg:
            controller.backward()
        if 'LEFT' == msg:
            controller.left()
        if 'RIGHT' == msg:
            controller.right()
        if 'STRAIGHT' == msg:
            controller.straight()

    def process_socket_event(self, msg, msg_type):
        if msg_type == 'ADD':
            self.camera_feed.add_socket(msg)
        elif msg_type == 'REMOVE':
            self.camera_feed.remove_socket(msg)

    def process_speed_event(self, msg):
        print('Method Listener.process_speed_event received: ', repr(msg))

    def __call__(self, **kwargs):
        print('BusListener instance received: ', kwargs)