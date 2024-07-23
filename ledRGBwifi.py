import network
import machine
import socket

# Define los pines GPIO para cada color del LED RGB
pinLedRojo = machine.Pin(14, machine.Pin.OUT)
pinLedVerde = machine.Pin(12, machine.Pin.OUT)
pinLedAzul = machine.Pin(13, machine.Pin.OUT)

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
estadoRojo = 0
estadoVerde = 0
estadoAzul = 0

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
        if "LED_ROJO=ON" in request:
            estadoRojo = 1
            pinLedRojo.value(estadoRojo)  # Encender el LED rojo
        elif "LED_VERDE=ON" in request:
            estadoVerde = 1
            pinLedVerde.value(estadoVerde)  # Encender el LED verde
        elif "LED_AZUL=ON" in request:
            estadoAzul = 1
            pinLedAzul.value(estadoAzul)  # Encender el LED azul
        
        # Si la solicitud es para apagar el LED
        elif "LED_ROJO=OFF" in request:
            estadoRojo = 0
            pinLedRojo.value(estadoRojo)  # Apagar el LED rojo
        elif "LED_VERDE=OFF" in request:
            estadoVerde = 0
            pinLedVerde.value(estadoVerde)  # Apagar el LED verde
        elif "LED_AZUL=OFF" in request:
            estadoAzul = 0
            pinLedAzul.value(estadoAzul)  # Apagar el LED azul

        # Genera la respuesta HTML con el estado actual de los LEDs
        response = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Control de LED RGB</title>
</head>
<body style='font-family: Arial, sans-serif; background-color: #f2f2f2; text-align: center;'>
    <h1 style='color: #0099cc; font-size: 24px;'>Control de LED RGB</h1>
    <p style='font-size: 18px; margin-top: 20px;'>Estado actual:</p>
    <p>Rojo: <span style='color: """ + ("red;" if estadoRojo == 1 else "black;") + """'>""" + ("ENCENDIDO" if estadoRojo == 1 else "APAGADO") + """</span></p>
    <p>Verde: <span style='color: """ + ("green;" if estadoVerde == 1 else "black;") + """'>""" + ("ENCENDIDO" if estadoVerde == 1 else "APAGADO") + """</span></p>
    <p>Azul: <span style='color: """ + ("blue;" if estadoAzul == 1 else "black;") + """'>""" + ("ENCENDIDO" if estadoAzul == 1 else "APAGADO") + """</span></p>
    <p>
        <a href='/LED_ROJO=ON' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border-radius: 5px;'>Encender Rojo</a>
        <a href='/LED_ROJO=OFF' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border-radius: 5px;'>Apagar Rojo</a><br>
        <a href='/LED_VERDE=ON' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border-radius: 5px;'>Encender Verde</a>
        <a href='/LED_VERDE=OFF' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border-radius: 5px;'>Apagar Verde</a><br>
        <a href='/LED_AZUL=ON' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border-radius: 5px;'>Encender Azul</a>
        <a href='/LED_AZUL=OFF' style='text-decoration: none; color: #0066cc; margin: 0 10px; padding: 5px 10px; border-radius: 5px;'>Apagar Azul</a>
    </p>
</body>
</html>
"""
        conn.send(response)
        print("Respuesta enviada")
        break
    conn.close()