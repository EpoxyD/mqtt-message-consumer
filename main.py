#!/usr/bin/python3

""" TODO write docstring"""

from mqtt import MQTTClient

if __name__ == "__main__":
    """ TODO write docstring"""
    print("Starting program")

    client = MQTTClient("test")
    with client.wait_for_message(topic="my_topic", payload=None, timeout=5):
        print("STEP 2")
