import socket as sock
import sys

cliente=sock.socket(sock.AF_INET, sock.SOCK_STREAM)
cliente.connect(('localhost', 8000))

while True:

    mensaje= input("Tú mensaje:")
    
    if mensaje != 'bye':
        cliente.send(mensaje.encode())
        respuesta= cliente.recv(1024).decode()
        print("Servidor:",respuesta)
        
    else:
        cliente.send(mensaje.encode())
        print("Terminando Conexión")
        cliente.close()
        sys.exit() #Para salir inmediatamente