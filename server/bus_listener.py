from payloads import ControlPayload
from server import controller as ctrl


class BusListener:
    def process_control_event(self, msg):
        print('Method Listener.process_control_event received: ', repr(msg))
        if ControlPayload.FORWARD == msg:
            ctrl.forward()
        if ControlPayload.STOP == msg:
            ctrl.stop()
        if ControlPayload.LEFT == msg:
            ctrl.left()
        if ControlPayload.RIGHT == msg:
            ctrl.right()

    def process_speed_event(self, msg):
        print('Method Listener.process_speed_event received: ', repr(msg))

    def __call__(self, **kwargs):
        print('BusListener instance received: ', kwargs)