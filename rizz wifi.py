import network
from time import sleep

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()
sta_if.connect("Redmi", "#&RIZZERIO ALEXANDER004@7202&#")
sleep(2)
if sta_if.isconnected():
    print("Connected to wiFi!")
else:
    print("Try again bruh!") 