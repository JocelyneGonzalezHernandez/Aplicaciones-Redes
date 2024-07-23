import sys
from Crypto.PublicKey import RSA # Importamos el módulo RSA

# El usuario (o sea nosotros) tiene que pasar un número mayor
# o igual 1024 y usando el objeto 'int' convertirmos un string
# a un entero.
bit_size = int(sys.argv[1])
key_format = sys.argv[2]

# Generamos el par de claves. Dependiendo del tamaño y el
# procesamiento de nuestro computador es lo que podrá tardar.
keys = RSA.generate(bit_size)

print("Clave Pública:")
# Exportamos la clave pública y la imprimimos. Colocamos como
# argumento 'nn' en el parámetro 'end' de la función 'print'
# para imprimir dos saltos de líneas y se vea más legible.
#
# 'key_format' se explicará en unos instantes
#
# Usamos el método '.decode(...)' porque al exportarlos estarán
# en 'bytes' y es mejor (para volverlo legible) tenerlo en 'utf-8'.
print(keys.publickey().export_key(key_format).decode(), end='nn')

print("\nClave Privada:")
# Hacemos prácticamente lo mismo que lo anterior, pero a diferencia
# de la exportación de la clave pública, no se necesita explicitar
# ningún método.
print(keys.export_key(key_format).decode())