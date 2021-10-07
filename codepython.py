from machine import Pin
import time
gpio4=Pin(4,Pin.OUT)
i=0
number = input("Enter ").split(" ")
for num in number:
    num = list(num)
    value = 0
    for i in range(len(num)):
        digit= num.pop()
        if digit == "1":
            value = value + pow(2,i)

    value = value/10
    gpio4.value(True)
    time.sleep(value)
    gpio4.value(False)
    time.sleep(0.5)