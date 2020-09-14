#!/usr/bin/python3

""" TODO write docstring"""


from datetime import datetime
from random import seed, randint
from paho.mqtt.publish import single

from mqtt import MQTTClient


potential_topics = ["hello", "world", "how", "are", "you", "today"]

if __name__ == "__main__":
    """ TODO write docstring"""
    print("Starting program")

    seed(datetime.now())
    print()

    client = MQTTClient("test")
    with client.wait_for_message(topic="how", payload=None, timeout=2):
        for i in range(0, 10):
            random_index = randint(0, len(potential_topics)-1)
            random_topic = potential_topics[random_index]
            single(random_topic)
        print("STEP 2")
