from pubsub import pub
from server.bus_listener import BusListener


controlTopic = 'controlTopic'
speedTopic = 'speedTopic'
busListener = BusListener()


def init_buses():
    pub.subscribe(busListener.process_control_event, controlTopic)
    pub.subscribe(busListener.process_speed_event, speedTopic)
    print('Registered pubsub system')
