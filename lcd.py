from network import *
from time import *
from socket import *
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

sta_if=WLAN(STA_IF)
sta_if.active(True)
print("Activando como station")
sleep(1)

if sta_if.active():
    print('Dispositivo Activado!')
else:
    print('Dispositivo No Activado!')
    
redes=sta_if.scan()
print('Escaneando redes...')
sleep(5)

for red in redes:
    print(red)
    
ssid='RouterArriba'
password='56412BTH266'

sta_if.connect(ssid,password)
print('Conectando...')
sleep(10)

if sta_if.isconnected():
    print('Dispositivo conectado!!')
else:
    print('Desconectado:', 'Cambiarse a mecatronica')
    
print(sta_if.ifconfig())
print('Direccion IP:', sta_if.ifconfig()[0])

DEFAULT_I2C_ADDR = 0x27

i2c = I2C(0,scl=Pin(1), sda=Pin(0), freq=400000) #Bus 0
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
while True:
        lcd.move_to(0, 0)
        lcd.putstr(sta_if.ifconfig()[0])


