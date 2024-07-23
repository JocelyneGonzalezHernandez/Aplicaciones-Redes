from network import *
from time import *
from socket import *

ap_if=WLAN(AP_IF)
ap_if.config(ssid='RouterArriba', password='56412BTH266')
print('Configurando...')
sleep(1)
ap_if.active(True)
print('Activando...')
sleep(1)
  
print('Access Point Status:', ap_if.active())
print('Direccion IP:', ap_if.ifconfig()[0])

miSocket=socket(AF_INET, SOCK_STREAM)
miSocket.bind(('', 8001))
miSocket.listen()

print("Escuchando conexion...")

while True:
    cliente,ip = miSocket.accept()
    print("Conexion recibida de", ip)
    request = cliente.recv(1024).decode()
    print("Solicitud recibida:")
    print(request)
    
    response='HTTP/1.1 200 Ok\n'
    response+='Content-Type: text/html\n\n'
    response+=' <html><body bgcolor=#bdecb6><h1>HOLA SOY EL SERVIDOR(ACCESS POINT) DE JOS</hl></body></html>'
    cliente.send(response.encode())
    
    print('Respuesta enviada:')
    print(response)
    cliente.close()