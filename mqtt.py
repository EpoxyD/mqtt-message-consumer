""" TODO write docstring"""


from contextlib import contextmanager
from paho.mqtt.client import Client


class MQTTClient(Client):
    """ TODO write docstring"""

    def __init__(self, client_id):
        super().__init__(client_id=client_id)

    @contextmanager
    def wait_for_message(self, topic, payload=None, timeout=2):
        print("STEP 1")
        yield
        print("STEP 3")
