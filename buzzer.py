from machine import Pin, PWM
from time import sleep

# Configurar el pin PWM para el buzzer
pin_pwm = PWM(Pin(0))

# Fijar la frecuencia PWM (en Hz)
frecuencia_pwm = 1000
pin_pwm.freq(frecuencia_pwm)

# Función para tocar una nota con el buzzer
def tocar_nota(frecuencia, duracion):
    pin_pwm.freq(frecuencia)  # Fijar la frecuencia del PWM para la nota
    pin_pwm.duty_u16(32767)  # Fijar el ciclo de trabajo del PWM (50% para un tono medio)
    sleep(duracion)  # Esperar durante la duración especificada
    pin_pwm.duty_u16(0)  # Apagar el PWM para silenciar el buzzer

# Ejemplo de uso para tocar una nota
tocar_nota(440, 0.5)  # Tocar un La4 (440 Hz) durante 0.5 segundos

