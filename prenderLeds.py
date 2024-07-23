from machine import *
from time import *

class ej1():
    def __init__(self):
        self.pines = [0, 1, 2, 3, 4, 5, 6, 7]
        
    def PrenderApagar(self, x):
        led = Pin(x, Pin.OUT)
        led.value(1)  # Encender el LED
        sleep(0.25)
        led.value(0)  # Apagar el LED
        sleep(0.25)
        
    def RecorrerPines(self):
        for x in self.pines:
            self.PrenderApagar(x)
        
        for x in reversed(self.pines):
            self.PrenderApagar(x)
            
    def PrenderTodos(self, x,v):
        led = Pin(x, Pin.OUT)
        led.value(v) #f
        sleep(0.25)
        led.value(v) #t
        sleep(0.25)
        
    def RecorrerPines2(self):
        for x in self.pines:
            self.PrenderTodos(x,1)
        
        for x in reversed(self.pines):
            self.PrenderTodos(x,0)
        
            
led=ej1()

while True:
    
    led.RecorrerPines2()
    led.RecorrerPines()
