from machine import Pin, PWM
from time import sleep

# Configurar los pines PWM para los colores rojo, verde y azul
pin_rojo = PWM(Pin(0))
pin_verde = PWM(Pin(1))
pin_azul = PWM(Pin(4))

# Fijar la frecuencia PWM (en Hz)
frecuencia_pwm = 1000
pin_rojo.freq(frecuencia_pwm)
pin_verde.freq(frecuencia_pwm)
pin_azul.freq(frecuencia_pwm)

while True:
    # Cambiar el color gradualmente
    for i in range(0, 65535, 1000):  # Cambiar el valor de 1000 según
                                     #la velocidad deseada de cambio de color
        pin_rojo.duty_u16(i)
        sleep(0.01)  # Tiempo de espera para el cambio gradual
    for i in range(65535, 0, -1000):
        pin_verde.duty_u16(i)
        sleep(0.01)
    for i in range(0, 65535, 1000):
        pin_azul.duty_u16(i)
        sleep(0.01)
    for i in range(65535, 0, -1000):
        pin_rojo.duty_u16(i)
        sleep(0.01)
    for i in range(0, 65535, 1000):
        pin_verde.duty_u16(i)
        sleep(0.01)
    for i in range(65535, 0, -1000):
        pin_azul.duty_u16(i)
        sleep(0.01)
