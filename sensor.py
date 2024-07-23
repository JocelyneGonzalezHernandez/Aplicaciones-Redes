from machine import *
from time import *

sensor=machine.ADC(26)
conversion=3.3/65535

while True:
    reading=sensor.read_u16()
    convertir_voltaje=reading*conversion
    temp=convertir_voltaje*1000
    
    print("Temperatura: ", temp, "C", sep="")
    sleep(2)