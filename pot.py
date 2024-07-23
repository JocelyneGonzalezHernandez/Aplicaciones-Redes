from machine import *
from time import *

pot=ADC(27)
f_16=(5/65535)

while True:
    reading=pot.read_u16() *f_16
    print("ADC: ",reading)
    sleep(0.2)