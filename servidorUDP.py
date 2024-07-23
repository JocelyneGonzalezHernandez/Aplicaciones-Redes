import socket
 
# Creamos un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Enlazamos el socket al puerto y dirección IP
server_address = ('localhost', 5000)
sock.bind(server_address)
 
# Escuchamos las peticiones entrantes
while True:
    print('Esperando a recibir un mensaje...')
    data, address = sock.recvfrom(1024)
 
    print('Recibido {} bytes de la dirección {}'.format(len(data), address))
    print(data.decode())
 
    # Enviamos una respuesta al cliente
    message = 'Respuesta desde el servidor Jos'
    sock.sendto(message.encode(), address)