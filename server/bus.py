from pubsub import pub


controlTopic = 'controlTopic'
speedTopic = 'speedTopic'


def init_buses(bus_listener):
    pub.subscribe(bus_listener.process_control_event, controlTopic)
    pub.subscribe(bus_listener.process_speed_event, speedTopic)
    print('Registered pubsub system')
