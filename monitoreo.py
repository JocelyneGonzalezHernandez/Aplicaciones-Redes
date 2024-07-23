from machine import ADC, Pin
from time import sleep
import socket
import network

# Configuración del pin del sensor de temperatura
sensor_temp = ADC(4)
conversion_temp = 3.3 / 65535

# Configuración del pin del sensor de humedad
sensor_humedad = ADC(Pin(27))

def conectar_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        print('Conectando a la red WiFi...')
        station.active(True)
        station.connect(ssid, password)
        while not station.isconnected():
            pass
    print('Conexión WiFi establecida:', station.ifconfig())

def leer_sensor():
    global temp, hum
    # Lectura del sensor de temperatura
    reading_temp = sensor_temp.read_u16()
    convertir_voltaje_temp = reading_temp * conversion_temp
    temp = 27 - (convertir_voltaje_temp - 0.706) / 0.001721
    
    # Lectura del sensor de humedad
    lectura_adc = sensor_humedad.read_u16()  # Lectura del valor ADC
    
    # Convertir la lectura ADC a un valor de humedad
    hum = 100 - ((lectura_adc / 65535.0) * 100)  # Invertir el cálculo

def pagina_web():
    html = """<!DOCTYPE HTML><html>
<head>
  <meta http-equiv=\"refresh\" content=\"10\">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 2.0rem; }
    p { font-size: 2.0rem; }
    .units { font-size: 1.2rem; }
    .bme-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
  </style>
</head>
<body>
  <h2>Sensor de Temperatura y Humedad</h2>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="bme-labels">Temperatura:</span> 
    <span>"""+str(temp)+"""</span>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="bme-labels">Humedad:</span>
    <span>"""+str(hum)+"""</span>
  </p>
</body>
</html>"""
    return html

conectar_wifi('RouterArriba', '56412BTH266')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conexion, direccion = s.accept()
    request = conexion.recv(1024)
    leer_sensor()
    respuesta = pagina_web()
    conexion.send('HTTP/1.1 200 OK\n')
    conexion.send('Content-Type: text/html\n')
    conexion.send('Connection: close\n\n')
    conexion.sendall(respuesta)
    conexion.close()
