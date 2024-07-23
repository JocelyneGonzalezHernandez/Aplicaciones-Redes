from machine import Pin, PWM
import network
import socket

# Configurar el pin del servo
servo_pin = 0  # El pin GPIO al que está conectado el servo
servo = PWM(Pin(servo_pin))
servo.freq(50)  # Frecuencia del PWM

# Configurar la conexión WiFi
ssid='RouterArriba'
password='56412BTH266'
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

print('Conectado a la red WiFi')
print('Dirección IP:', sta_if.ifconfig()[0])

def set_servo_angle(angle):
     ton = ((angle + 45) * 100000) / 9
     servo.duty_ns(int(ton))
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
        
        if 'GET /?angle=' in request:
            angle = int(request.split('GET /?angle=')[1].split(' ')[0])
            set_servo_angle(angle)
        
        response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
        response += '<!DOCTYPE html><html><body>'
        response += '<h1>Servidor de control de servo</h1>'
        response += '<p>Ingrese el ángulo deseado del servo:</p>'
        response += '<form action="/" method="get">'
        response += '<input type="number" name="angle" min="0" max="180">'
        response += '<input type="submit" value="Enviar">'
        response += '</form>'
        response += '</body></html>'
        
        client_socket.send(response)
        client_socket.close()
