from machine import Pin
from time import sleep
gpio4 = Pin(4, Pin.OUT)
while(True):
    gpio4.value(True)
    sleep(0.5)
    gpio4.value(False)
    sleep(0.5)