from machine import Pin, ADC
from time import sleep

# Configuración del pin del sensor de humedad
pin_sensor_humedad = Pin(27)  # Ejemplo: GPIO 26
sensor_humedad = ADC(pin_sensor_humedad)

while True:
    # Lectura del sensor de humedad
    lectura_adc = sensor_humedad.read_u16()  # Lectura del valor ADC
    
    # Convertir la lectura ADC a un valor de humedad
    humedad = (lectura_adc / 65535.0) * 100
    
    
    # Imprimir el valor de humedad
    print("Humedad: {:.2f}%".format(humedad))
    
    # Esperar un tiempo antes de realizar la siguiente lectura
    sleep(2)  # Espera de 2 segundos entre lecturas
