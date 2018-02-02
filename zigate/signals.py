from blinker import signal

SIGNAL_ATTRIBUTE_CHANGED = signal('zigate_attribute_changed')
SIGNAL_ENDPOINT_CHANGED = signal('zigate_endpoint_changed')
SIGNAL_DEVICE_ANNOUNCE = signal('zigate_device_announce')
