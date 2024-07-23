#CREAR UN SOCKET
import socket as sock #socket es una biblioteca

#biblioteca.clase(familia de direccion, tipo)
#socket.AF_INET #FAMILIA DE PROTOCOLO DE INTERTNET (IPV4)
#socket.AF_INET6 (IPV6)

#SOCK_STREAM #TCP
#SOCK_DGRAM #UDP
miSocket = sock.socket(sock.AF_INET,sock.SOCK_STREAM)

#CREAR SERVIDOR
miSocket.bind(('localhost',8000)) #Asociando al puerto 8000
miSocket.listen()

print("Escuchando conexión...")

while True: 

    con,addr = miSocket.accept()

    print("Conexión recibida de: ", addr)

    con.send(b"Hola desde el servidor Jos")

    con.close() #Finalizar conexión Socket
