from pubsub.mqtt.connection_manager import ConnectionManager
from pubsub.mqtt.topic_manager import TopicManager
from gpiozero import MotionSensor
from configparser import ConfigParser

import time

pir_pin = 0 #TODO

pir = MotionSensor(pin=pir_pin)
mgr = ConnectionManager.MqttManager("mac_test2", "test.mosquitto.org", 1883)

cm = ConfigParser()
cm.read()

tm = TopicManager()

pir.when_activated = mgr.publish("house/lounge/motion", "Motion started")
pir.when_deactivated = mgr.publish("house/lounge/motion", "Motion ended")
time.sleep(5)