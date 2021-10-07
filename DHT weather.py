import machine
import network

import urequests
import dht
import time

#initializing pin and dht sensor
led = machine.Pin(4,machine.Pin.OUT)
d = dht.DHT11(machine.Pin(14))

#Connection to wifi

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()
sta_if.connect("Redmi", "#&RIZZERIO ALEXANDER004@7202&#")

if sta_if.isconnected():
    print("Connected to wiFi!")
else:
    print("Try again bruh!") 







#sta = network.WLAN(network.STA_IF);
#if not sta.isconnected():
 #   print('connecting to wifi network...')
  #  sta.active(True)
   # sta.connect("wifi_credentials.Redmi", "wifi_credentials.#&RIZZERIO ALEXANDER004@7202&#")
    #while not sta.isconnected():
     #   pass
    #print('network config:', sta.ifconfig())
    
#Constants and variables
HTTP_HEADERS = {'Content-Type': 'application/json'}
THINGSPEAK_WRITE_API_KEY = '5FQ3K6D7VD3NKSFD'
UPDATE_TIME_INTERVAL = 5000 #IN ms
last_update = time.ticks_ms()


#Main loop:
while True:
     if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL:
         d.measure()
         t=d.temperature()
         h=d.humidity()
         
         dht_readings = {'field1':t, 'field2':h}
         request = urequests.post(
             'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY,
             json = dht_readings,
             headers = HTTP_HEADERS)
         request.close()
         print(dht_readings)
         
         led.value(not led.value())
         last_update = time.tricks_ms()
     
     
     