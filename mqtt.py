""" TODO write docstring"""


from contextlib import contextmanager
from queue import Queue, Empty
from time import sleep
from threading import Event

from paho.mqtt.client import Client

_subscribe = Event()


class Pipeline(Queue):
    """ TODO write docstring"""

    def __init__(self):
        super().__init__(maxsize=10)


def client_on_connect(client, userdata, flags, rc):
    """ Callback function """
    print("CON", client, userdata, flags, rc)


def client_on_message(client, userdata, message):
    """ Callback function """
    print("MSG", client, userdata, message.payload.decode("utf-8"))


def client_on_subscribe(client, userdata, mid, granted_qos):
    """ Callback function """
    print("SUB", client, userdata, mid, granted_qos)


class MQTTClient(Client):
    """ TODO write docstring"""

    def __init__(self, client_id):
        self.buffer = Pipeline()
        super().__init__(client_id=client_id, userdata=self.buffer)
        self.on_connect = client_on_connect
        self.on_message = client_on_message
        self.on_subscribe = client_on_subscribe
        self.connect("localhost")
        self.loop_start()
        sleep(5)

    @contextmanager
    def wait_for_message(self, topic, payload=None, timeout=2):
        print("Setup queue for checking")
        self.subscribe(topic)
        while not self.buffer.empty():
            self.buffer.get()
        yield
        print("Print received calls")
        try:
            rec_topic, rec_payload = self.buffer.get(timeout=timeout)
            if rec_topic == topic and rec_payload == payload:
                print(rec_topic, rec_payload)
        except Empty:
            print("Waiting period timed out")
        finally:
            self.unsubscribe(topic)
