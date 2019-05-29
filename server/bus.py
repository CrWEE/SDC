from pubsub import pub


controlTopic = 'controlTopic'
speedTopic = 'speedTopic'
socketTopic = 'socketTopic'


def init_buses(bus_listener):
    pub.subscribe(bus_listener.process_control_event, controlTopic)
    pub.subscribe(bus_listener.process_speed_event, speedTopic)
    pub.subscribe(bus_listener.process_socket_event, socketTopic)
    print('Registered pubsub system')
