from network import *
from time import *
from socket import *

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

miServer=socket(AF_INET, SOCK_STREAM)
miServer.bind(('', 8000))
miServer.listen()

print("Escuchando conexion...")

while True:
    cliente,ip = miServer.accept()
    print("Conexion recibida de", ip)
    request = cliente.recv(1024).decode()
    print("Solicitud recibida:")
    print(request)
    
    response ='HTTP/1.1 200 Ok\n'
    response+='Content-Type: text/html\n\n'
    response+=' <html><body bgcolor=#bdecb6><h1>HOLA SOY EL SERVIDOR DE JOS</hl></body></html>'
    cliente.send(response.encode())
    
    print('Respuesta enviada:')
    print(response)
    cliente.close()