from pubsub import pub
from pubsub.utils import notification

controlTopic = 'controlTopic'
speedTopic = 'speedTopic'


def init_buses(bus_listener):
    pub.subscribe(bus_listener.process_control_event, controlTopic)
    pub.subscribe(bus_listener.process_speed_event, speedTopic)
    print('Registered pubsub system')
    # To debug the pubsub system. Writes to console by default
    # notification.useNotifyByWriteFile()
