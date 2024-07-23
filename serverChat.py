import socket as sock

miSocket = sock.socket(sock.AF_INET,sock.SOCK_STREAM)

miSocket.bind(('localhost',8000)) #Asociando al puerto 8000
miSocket.listen()

while True:
    con,addr = miSocket.accept()

    print("Conexión recibida de: ", addr)
    
    while True:
        
        mensajeCliente =con.recv(1024).decode()
        print("Cliente: ", mensajeCliente)
        
        if mensajeCliente == 'bye':
            break  
        else:
             mensaje= input("Tú mensaje:")
             con.send(mensaje.encode())

    print("Terminando conexión")
    con.close() #Finalizar conexión Socket
