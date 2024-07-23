from machine import Pin, PWM
import network
import socket

# Configurar el pin del buzzer
buzzer_pin = 0  # El pin GPIO al que está conectado el buzzer
buzzer = PWM(Pin(buzzer_pin))
buzzer.freq(1000)  # Frecuencia del PWM

# Configurar la conexión WiFi
ssid = 'RouterArriba'
password = '56412BTH266'
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

print('Conectado a la red WiFi')
print('Dirección IP:', sta_if.ifconfig()[0])

def buzzer_on():
    buzzer.duty_u16(32768)  # Establecer el ciclo de trabajo del PWM para encender el buzzer al 50%

def buzzer_off():
    buzzer.duty_u16(0)  # Apagar el buzzer configurando el ciclo de trabajo del PWM en 0

# Configurar el servidor web
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 80))
server_socket.listen(5)
    
print('Servidor iniciado. Escuchando en el puerto 80...')
    
while True:
    client_socket, addr = server_socket.accept()
    print('Conexión establecida desde:', addr)
        
    request = client_socket.recv(1024).decode()
    print('Solicitud recibida:', request)
        
    if 'GET /?action=on' in request:
        buzzer_on()
    elif 'GET /?action=off' in request:
        buzzer_off()
        
    response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
    response += '<!DOCTYPE html><html><body>'
    response += '<h1>Servidor de control de buzzer</h1>'
    response += '<p>Haga clic en los botones para encender o apagar el buzzer:</p>'
    response += '<a href="/?action=on"><button>Encender Buzzer</button></a>'
    response += '<a href="/?action=off"><button>Apagar Buzzer</button></a>'
    response += '</body></html>'
        
    client_socket.send(response)
    client_socket.close()