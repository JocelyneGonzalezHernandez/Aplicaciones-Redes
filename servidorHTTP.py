import socket as sock

servidor = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
servidor.bind(('localhost', 8000))
servidor.listen()

print(f'Servidor activo en localhost:8000')

while True:
    con, addr = servidor.accept()
    with con:
        print(f'Conexión recibida de {addr}')
        data = con.recv(1024)
        if data:
            print('Solicitud recibida:')
            print(data.decode())

            # Respuesta HTTP básica
            respuesta= """HTTP/1.1 200 OK
Content-Type: text/html

<html>
<body>
<h1>Hola, soy Jocelyne</h1>
</body>
</html>
"""
            con.sendall(respuesta.encode())
