import socket as sock

cliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
cliente.connect(('localhost', 8000))

# Solicitud HTTP básica
solicitud= """GET / HTTP/1.1
Host: localhost:8000

"""

cliente.sendall(solicitud.encode())

respuesta = cliente.recv(1024)
print('Respuesta recibida:')
print(respuesta.decode())