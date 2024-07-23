import network
import machine
import socket

pinLed = machine.Pin(14, machine.Pin.OUT)

ssid = 'RouterArriba'
password = '56412BTH266'
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected():
    pass

print("Conexión establecida!")
print("Dirección IP:", sta.ifconfig()[0])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 80))
server.listen(5)

# Inicialmente, el LED está apagado
estado = 0

print("Esperando conexiones...")

while True:
    conn, addr = server.accept()
    print("Conexión establecida desde:", addr)

    while True:
        request = conn.recv(1024).decode()
        print("Solicitud recibida:", request)
        if not request:
            break
        
        # Si la solicitud es para encender el LED
        if "LED=ON" in request:
            estado = 1
            pinLed.value(estado)  # Encender el LED
        
        # Si la solicitud es para apagar el LED
        elif "LED=OFF" in request:
            estado = 0
            pinLed.value(estado)  # Apagar el LED

        response = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Control de LED</title>
</head>
<body style='font-family: Arial, sans-serif; background-color: #f2f2f2; text-align: center;'>
    <h1 style='color: #0099cc; font-size: 24px;'>Control de LED</h1>
    <p style='font-size: 18px; margin-top: 20px;'>Estado actual: <span style='color: #33cc33; font-weight: bold;'>""" + ('ENCENDIDO' if estado == 1 else 'APAGADO') + """</span></p>
    <p>
        <a href='/LED=ON' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border: 1px solid #0066cc; border-radius: 5px;'>Encender</a>
        <a href='/LED=OFF' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border: 1px solid #0066cc; border-radius: 5px;'>Apagar</a>
    </p>
</body>
</html>

"""
        conn.send(response)
        print("Respuesta enviada")
        break    
    conn.close()