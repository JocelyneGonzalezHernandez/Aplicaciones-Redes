from machine import *
from time import *
led=Pin(0,Pin.OUT)
while True:
    led.value(1) #True
    sleep(0.5)
    led.value(0) #False
    sleep(0.5)
