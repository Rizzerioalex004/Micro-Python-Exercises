from machine import Pin
from time import sleep

p4 = Pin(4,Pin.OUT)
p4.value(False)
p2 = Pin(2,Pin.OUT)
p2.value(False)
p14 = Pin(14,Pin.OUT)
p14.value(False)

while True:
        p4.value(True)
        sleep(0.2)
        p4.value(False)
        sleep(0.1)
        p2.value(True)
        sleep(0.2)
        p2.value(False)
        sleep(0.1)
        p14.value(True)
        sleep(0.2)
        p14.value(False)
        sleep(0.1)