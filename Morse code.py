from machine import Pin
from time import sleep

p4 = Pin(4, Pin.OUT)

inp = input("enter a morse code")
p4.value(False)

for item in inp:
    if item==0:
        #blink for 0.2 sec
        p4.value(True)
        sleep(0.2)
        p4.value(False)
        sleep(0.1)
        
    else:
        p4.value(True)
        sleep(0.8)
        p4.value(False)
        sleep(0.1)