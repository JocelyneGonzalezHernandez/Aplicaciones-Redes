from network import *
from time import *

sta_if=WLAN(STA_IF)
sta_if.active(True)
print ("Activando como station")
sleep(1)

if sta_if.active():
    print("Dispositivo activado!")
else:
    print("Dispositivo no activado")

redes=sta_if.scan()
print("Escaneando redes...")
sleep(5)

for red in redes:
    print(red)
    
ssid='Ami'
password='bwdr3482'

sta_if.connect(ssid,password)
print('Conectando...')
sleep(10)

if sta_if.isconnected():
    print('Conectando...')
else:
    print('Desconectado:(', 'Cambiarse a mecatrónica')
    
print(sta_if.ifconfig())
print('Dirección IP:', sta_if.ifconfig()[0])